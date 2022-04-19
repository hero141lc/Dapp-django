# -*- coding:utf-8 -*- 
import imp
from sre_constants import SUCCESS
from django.shortcuts import render
import requests
import json
import datetime
from dateutil import rrule,parser
from rx import catch
from sqlalchemy import false, true

# Create your views here.
pancakeAddr='0x10ed43c718714eb63d5aa57b78b54704e256024e'
def index(request):

    return render(request, 'app/index.html')
def connectUs(request):

    return render(request, 'app/connectUs.html')
async def dd():
    print("ss") 
def Kline(contenst):
    peak = 0
    URL = 'https://api.covalenthq.com/v1/56/address/'+contenst+'/portfolio_v2/?quote-currency=USD&format=JSON&key=ckey_c95724e05a2f4802a387160b08e'
    # 输入在浏览器的网址
    res = requests.get(URL).text
    # 发送 GET 方式的请求，并把返回的结果(响应)存储在 res 变量里头
    # 答第二个问题，get() 方法需要输入一个网页链接
    print(contenst)
    #print(json.loads(res)['data']['items'])
    try:
        data=json.loads(res)['data']['items']
        for item in data:
            
            if item['contract_address'] == contenst:
                #print(item)
                for item2 in item['holdings']:
                    print(item2['quote_rate'])
                    if item2['quote_rate'] != None:
                        if eval(str(item2['quote_rate']))>peak:
                            peak=eval(str(item2['quote_rate']))
                       
    except Exception as e:
        peak=0
        print(e)
    print(peak)
    return peak
def result(request):
    address=request.GET['address']
    print(request.GET['address'])
    URL = 'https://api.covalenthq.com/v1/56/address/'+address+'/transactions_v2/?quote-currency=USD&format=JSON&block-signed-at-asc=false&no-logs=false&page-number=0&page-size=1000&key=ckey_c95724e05a2f4802a387160b08e'
    # 输入在浏览器的网址
    res = requests.get(URL).text
    # 发送 GET 方式的请求，并把返回的结果(响应)存储在 res 变量里头
    # 答第二个问题，get() 方法需要输入一个网页链接
    data=json.loads(res)['data']
    # list
    toList=[]
    fromList=[]
    income=0
    expenditure=0
    profits=0
    brickDays=0
    profitsMax=0
    profitsMin=0
    maxTrading={}
    minTrading={}
    maxName=''
    minName=''
    maxMaifei=0
    minMaifei=0
    maxMany=0
    minMany=0
    maifeiWho=''
    winne=1
    minContent=''
    maxContent=''
    d1 = parser.parse(data['items'][-1]['block_signed_at']).date()
    d2 = datetime.datetime.now()
    print(d1,d2)
    months = rrule.rrule(rrule.MONTHLY, dtstart=d1, until=d2).count()+2
    
    print(type(pancakeAddr))
    times= len(data['items'])+1
    for item in data['items']:
       # print(type(item['from_address']))
        if item['from_address']==pancakeAddr:
            fromList.append(item)
            income+=int(item['value_quote'])
            if profitsMax < int(item['value_quote']):
                profitsMax=int(item['value_quote'])
                maxTrading=item
                maxMany=int(item['value_quote'])/int(item['value'])
        if item['to_address']==pancakeAddr:
            toList.append(item)
            expenditure+=int(item['value_quote'])
            if profitsMin < int(item['value_quote']):
                profitsMin=int(item['value_quote'])
                minTrading=item
                minMany=int(item['value_quote'])/int(item['value'])
    profits=int(income-expenditure)
    brickDays=profits/32
    #if 

    print(len(toList),len(fromList),profits,brickDays,profitsMax,profitsMin)

    #If no income
   
    try:
        for item in minTrading['log_events']:
            for item2 in item['decoded']['params']:
                if item2['value'] == address:
                    minName=item['sender_contract_ticker_symbol']
                    minContent=item['sender_address']
                    
    except:
        minName='Null'
        minContent=""
    try:
        for item in maxTrading['log_events']:
            for item2 in item['decoded']['params']:
                if item2['value'] == address:
                    maxName=item['sender_contract_ticker_symbol']
                    maxContent=item['sender_address']
    except:
        maxName='Null'
        maxContent=""
    print("maxContent:",maxContent,minContent)
    maxPeak=Kline(maxContent)
    minPeak=Kline(minContent)
    maxMaifei=maxMany*maxPeak-profitsMax
    minMaifei=minPeak*minMany-profitsMin
    if maxMaifei>minMaifei:
        maifei=maxMaifei
        maifeiWho=maxName
    else:
        maifei=minMaifei
        maifeiWho=minName
    print(minName,maxName,maxPeak,minPeak,maifei)
    #print(data)
    if profits>0:
        winne=1
    else:
        winne=0
    context={
        'months':months,
        'times':times,
        'profitsMax':abs(int(profitsMax)),
        'profitsMin':abs(int(profitsMin)),
        'minName':minName,
        'maxName':maxName,
        'brickDays':abs(int(brickDays)),
        'maifeiWho':maifeiWho,
        'profits':abs(int(profits)),
        'maifei':abs(int(maifei)),
        'winne':winne,
    }
    response =render(request, 'app/result.html',context)
   
    response.set_cookie('context', str(context), max_age=None, expires=None,domain=None, secure=False, httponly=False, samesite=None)

    return response

def create(request):
    cookies = request.COOKIES
    for cookie_key,cookie_value in cookies.items():
        print(cookie_key,cookie_value)
    return render(request, 'app/create.html')

