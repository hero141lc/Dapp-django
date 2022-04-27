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
from .models import Token,Prices
# Diy Function
from app.getToken import *
from app.poster import *
import copy
# Create your views here.
pancakeAddr='0x10ed43c718714eb63d5aa57b78b54704e256024e'
def index(request):
    #print(exSql('0x7a565284572d03ec50c35396f7d6001252eb43b6'))
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
        data=eval(res)['data']['items']
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
    context=getOrder(address)
    context_result=copy.deepcopy(context) 
    
    if context_result['firstTime']!='':
        context_result['firstTime'] = str(context_result['firstTime']).replace('-', '年', 1)
        context_result['firstTime'] = context_result['firstTime'].replace('-', '月', 1)+'日'
    print(context)
    response =render(request, 'app/result.html',context_result)
    response.set_cookie('context', str(context), max_age= 60*5, expires=None,domain=None, secure=False, httponly=False, samesite=None)
    print()
    return response

def create(request):
    url='https://api.covalenthq.com/v1/56/networks/pancakeswap_v2/assets/?quote-currency=USD&format=JSON&contract-addresses=0xc4893fEa8547Fb1A4D860518285AF6655424645f&key=ckey_cd901996858f4187b44f93aadac'
    res = json.loads(requests.get(url).text)['data']['items'][0]
    # 发送 GET 方式的请求，并把返回的结果(响应)存储在 res 变量里头
    # 答第二个问题，get() 方法需要输入一个网页链接
    
    cookies = request.COOKIES
    print("cookies",cookies)
    #print(res)
    
    cookie_value = cookies['context']
    cookie_value=eval(cookie_value)
    # for _cookie_key,_cookie_value in cookies.items():
    #     print(_cookie_key,_cookie_value)

    #print("cookie_value['firstTime']",cookie_value['firstTime'])
    if ('profits' in cookie_value) and int(cookie_value['profits'])>0:
        posterUrl=win(cookies)
    else:
        posterUrl=lose(cookies)
    cookie_value['posterUrl']=posterUrl
    cookie_value['houlders']=howManyHoulder()

    # K line
    brickOb=exSql('0xc4893fea8547fb1a4d860518285af6655424645f')
    cookie_value['priceNow']=Prices.objects.filter(Token=brickOb).last().price
    print( cookie_value['priceNow'])
    cookie_value['market']=round(int(res['token_1']['reserve'])*cookie_value['priceNow']/1e18,2)
    cookie_value['priceNow']=round(cookie_value['priceNow'],7)
    #priceList
    cookie_value['price_list']=Prices.objects.filter(Token=brickOb)
    
 
    for i in cookie_value['price_list']:
        i.date=i.date.date().isoformat()
    cookie_value['swap_count_24h']=res['swap_count_24h']
    cookie_value['reserve']=round(int(res['token_0']['reserve'])/1e18,2)
    return render(request, 'app/create.html',cookie_value)

def wait(request):
    return render(request, 'app/wait.html')