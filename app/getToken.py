'''

import datetime
import django
#django.setup()

#from app.models.user import User

'''
import json
import requests
import datetime
from .models import Token,Prices,Trans,Wallet

pancakeAddr='0x10ed43c718714eb63d5aa57b78b54704e256024e'
def test():
    print('sauhuiuadhiwaudh')
    return 0
def is_today(target_date):
    """
    Detects if the date is current date
    :param target_date:
    :return: Boolean
    """
    # Get the year, month and day
    c_year = datetime.datetime.now().year
    c_month = datetime.datetime.now().month
    c_day = datetime.datetime.now().day

    # Disassemble the date
    date_list = target_date.split(" ")[0].split("-")
    print(date_list)
    t_year = int(date_list[0])
    t_month = int(date_list[1])
    t_day = int(date_list[2])

    final = False
    if c_year == t_year and c_month == t_month and c_day == t_day:
        final = True
    print(final)
    return final
'''
狗王0x641ec142e67ab213539815f67e4276975c2f8d50
搬砖0xc4893fea8547fb1a4d860518285af6655424645f
狗撕拉0x7a565284572d03ec50c35396f7d6001252eb43b6
babydoge0xc748673057861a797275cd8a068abb95a902e8de
raca0x12bb890508c125661e03b09ec06e404bc9289040
gmt0x7ddc52c4de30e94be3a6a0a2b259b2850f421989
goma0xab14952d2902343fde7c65d7dc095e5c8be86920
bnx0x8c851d1a123ff703bd1f9dabe631b69902df5f97
bit0xc864019047b864b6ab609a968ae2725dfaee808a
'''
def getOrder(address):
    addressRes='address+'+address
    Token='contractaddress='
    URL='https://api.bscscan.com/api?module=account&action=tokentx&&'+address+'&page=1&offset=50&startblock=0&endblock=99999999999&sort=asc&apikey=TFD2ZDC1W77QAXP38SF9I1Z6T34GBGIGUJ'
    res = requests.get(URL).text
    data=json.loads(res)['result']
    toList=[]
    toNameList=set()
    fromNameList=set()
    bossList=set()
    fromList=[]
    pricesList=[]
    income=0
    expenditure=0
    for item in data:
        if item['from'] == address:
            fromNameList.add(item['contractAddress'])
            fromList.append(item)
        elif item['to'] == address:
            toNameList.add(item['contractAddress'])
            toList.append(item)
    bossList=fromNameList&toNameList
    for i in bossList:
        exSql(i)
    pricesList=Trans
def newData(contenst,yearsAgo,toDate):
    #fromDate = '2022-03-14'
    #toDate = '2022-04-15'
    URL = 'https://api.covalenthq.com/v1/pricing/historical_by_addresses_v2/56/USD/'+contenst+'/?from='+yearsAgo+'&to='+toDate+'&prices-at-asc=true&page-size=1000&key=ckey_c95724e05a2f4802a387160b08e'
    # 输入在浏览器的网址
    res = requests.get(URL).text
    data=json.loads(res)['data'][0]
    priceList = data['prices']
    print()
    tokenOb= Token.objects.create(decimals=int(data['contract_decimals']),name=data['contract_name'],symbol=data['contract_ticker_symbol'],logo_url=data['logo_url'],address=data['contract_address'],update_at=datetime.datetime.strptime(data['update_at'][0:11], "%Y-%m-%dT"),quote_currency=data['quote_currency'])
    for item in priceList:
        print()
        Prices.objects.create(date=datetime.datetime.strptime(item['date'][0:10], "%Y-%m-%d"),price=item['price'], Token=tokenOb)
    print('New Coin Added Successed:',data['contract_ticker_symbol'],data['update_at'])
    return tokenOb
def getData(tokenOb,fromDate,toDate):
    #fromDate = '2022-03-14'
    #toDate = '2022-04-15'
    URL = 'https://api.covalenthq.com/v1/pricing/historical_by_addresses_v2/56/USD/'+tokenOb.address+'/?from='+fromDate+'&to='+toDate+'&prices-at-asc=true&page-size=1000&key=ckey_c95724e05a2f4802a387160b08e'
    # 输入在浏览器的网址
    res = requests.get(URL).text
    data=json.loads(res)['data'][0]['prices']
    for item in data:
        Prices.objects.create(date=datetime.datetime.strptime(item['date'][0:10], "%Y-%m-%d"),price=item['price'], Token=tokenOb)
    return tokenOb

def exSql(contenst):
    timeNow=datetime.datetime.now()
    toDate=timeNow.date().isoformat()
    try:
        tokenOb=Token.objects.get(address=contenst)
        tokenObTime=tokenOb.update_at.date()
        if tokenObTime.__rsub__(timeNow)>1:
            tokenObTime=tokenObTime+ datetime.timedelta(1)
            fromDate=tokenObTime.isoformat()
            data=getData(tokenOb,fromDate,toDate)

        else:
            return 0
    except:
        yearsAgo=(timeNow-datetime.timedelta(days=365)).date().isoformat()
        data=newData(contenst,yearsAgo,toDate)

    # 发送 GET 方式的请求，并把返回的结果(响应)存储在 res 变量里头
    # 答第二个问题，get() 方法需要输入一个网页链接
    return data
