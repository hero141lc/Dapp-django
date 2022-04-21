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
    context=getOrder(address)
    response =render(request, 'app/result.html',context)
   
    response.set_cookie('context', str(context), max_age=None, expires=None,domain=None, secure=False, httponly=False, samesite=None)

    return response

def create(request):
    cookies = request.COOKIES
    for cookie_key,cookie_value in cookies.items():
        print(cookie_key,cookie_value)
    return render(request, 'app/create.html')

