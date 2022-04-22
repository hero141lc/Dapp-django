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
from django.db.models import Q,Max
from web3 import Web3
pancakeAddr='0x10ed43c718714eb63d5aa57b78b54704e256024e'
def piXiu(token):
	url = 'https://bsc-dataseed.binance.org'
	web3 = Web3(Web3.HTTPProvider(url))
	# pancake_Factory
	factory_abi = json.loads('[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
    token_address = web3.toChecksumAddress(token)
	factory_address = '0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73'
	factory_contract = web3.eth.contract(address=factory_address, abi=factory_abi)


	#returns a address the trading pairs on pancake
	#基础币 如:wbnb，usdt,busd
	WETH = '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'
	#检测的目标币
 
	#token_address = '0xc40B6e88FD7b09Eb8F768f402bF5dad6bF2bC622'
	#检测的目标币主池子
	pairAddr = factory_contract.functions.getPair(WETH,token_address).call()
	print(pairAddr)
	result = factory_contract.functions.detectFee(pairAddr,token_address,WETH,10000000000000000).call()
	print(result)

	if result==None or len(result)!=2:
		print("貔貅")
		return 1
	else:
		print(result)
		return 0


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

def newData(contenst,yearsAgo,toDate):
    #fromDate = '2022-03-14'
    #toDate = '2022-04-15'
    URL = 'https://api.covalenthq.com/v1/pricing/historical_by_addresses_v2/56/USD/'+contenst+'/?from='+yearsAgo+'&to='+toDate+'&prices-at-asc=true&page-size=1000&key=ckey_c95724e05a2f4802a387160b08e'
    # 输入在浏览器的网址
    res = requests.get(URL).text
    data=json.loads(res)['data'][0]
    priceList = data['prices']
    tokenOb= Token.objects.create(decimals=int(data['contract_decimals']),name=data['contract_name'],symbol=data['contract_ticker_symbol'],logo_url=data['logo_url'],address=data['contract_address'],update_at=datetime.datetime.strptime(data['update_at'][0:11], "%Y-%m-%dT"),quote_currency=data['quote_currency'])
    for item in priceList:
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
        print("how long update:",(timeNow.date()-tokenObTime).days)
        if (timeNow.date()-tokenObTime).days>1:
            tokenOb.update_at=timeNow
            tokenOb.save()
            fromDate=tokenObTime.isoformat()
            data=getData(tokenOb,fromDate,toDate)

        else:
            return tokenOb
    except:
        yearsAgo=(timeNow-datetime.timedelta(days=365)).date().isoformat()
        data=newData(contenst,yearsAgo,toDate)

    # 发送 GET 方式的请求，并把返回的结果(响应)存储在 res 变量里头
    # 答第二个问题，get() 方法需要输入一个网页链接
    return data
def getOrder(address):
    addressRes='address='+address
    Token='contractaddress='
    URL='https://api.bscscan.com/api?module=account&action=tokentx&&'+addressRes+'&page=1&offset=50&startblock=0&endblock=99999999999&sort=asc&apikey=TFD2ZDC1W77QAXP38SF9I1Z6T34GBGIGUJ'
    res = requests.get(URL).text
    data=json.loads(res)['result']
    toList=[]
    newToDict={}
    newFromDict={}
    newDict={}
    toNameList=set()
    fromNameList=set()
    bossList=set()
    fromList=[]
    toPriceList=[]
    fromPriceList=[]
    pricesList=[]
    income=0
    expenditure=0
    times=len(data) +1
    maxName=''
    minName=''
    maxPrice=0
    minPrice = 0
    toMoney=0
    fromMoney=0
    profitsMax=0
    profitsMin=0
    minName=''
    maxName=''
    sellAll=[]
    peakPrice=0
    maifeiAll=0
    maifeiCoin=''
    maifeiPeak=0
    maifeiMax=0
    pixiuKing=[0,0,'']

    for item in data:
        #print(address)
        if item['from'] == address:

            fromNameList.add(item['contractAddress'])
            item['value']=int(item['value'])
            item['time']=datetime.datetime.fromtimestamp(int(item['timeStamp']))
            fromList.append(item)

        elif item['to'] == address:
            toNameList.add(item['contractAddress'])
            item['value']=int(item['value'])            
            item['time']=datetime.datetime.fromtimestamp(int(item['timeStamp']))
            toList.append(item)

    bossList=fromNameList&toNameList
    
    for i in bossList:
        #print(i)
        toeknOb=exSql(i)
        priceOb=Prices.objects.filter(Token=toeknOb).values()
        for item in priceOb:
            for item2 in fromList:
                if item2['contractAddress'] == toeknOb.address:
                    if item2['time'].date()==item['date'].date():
                        print("sajkdhaklhdwoajdiwka--------------")
                        item2['price']=int(item2['value']*item['price'])
                        peakPrice=Prices.objects.filter(Q(Token=toeknOb)&Q(date__gt=item['date'])).aggregate(Max('price'))['price__max']
                        #Pric turn to item2['value']*item.price
                        #Maifei
                        maifeitemp=int(item2['value']*peakPrice)-item2['price']
                        maifeiAll+=maifeitemp
                        fromMoney+=item2['price']
                        if item2['price']>minPrice:
                            minPrice=item2['price']
                        if maifeitemp>0 and maifeitemp>maifeiPeak:
                            maifeiPeak=maifeitemp
                            maifeiCoin=item2['tokenSymbol']
                            maifeiMax=item2['price']
                        a=newFromDict.get(item2['contractAddress'])
                        print("a:",item2['contractAddress'])
                        if a==None:
                            newFromDict[item2['contractAddress']]={
                                'name':item2['tokenSymbol'],
                                'address':item2['contractAddress'],
                                'price':item2['price'],
                            }
                        else:
                            a['price']+=item2['price']
                        break
            for item2 in toList:
                if item2['contractAddress'] == toeknOb.address:
                    #print(item2['time'].date(),item['date'].date())
                    if item2['time'].date()==item['date'].date():
                        print("sajkdhaklhdwoajdiwka--------------")
                        item2['price']=int(item2['value']*item['price'])
                        print("item2:",item2['price'])
                        toMoney+=item2['price']
                        if item2['price']>maxPrice:
                            maxPrice=item2['price']

                        a=newToDict.get(item2['contractAddress'])
                        print("a:",a)
                        if a==None:
                            newToDict[item2['contractAddress']]={
                                'name':item2['tokenSymbol'],
                                'address':item2['contractAddress'],
                                'price':item2['price'],
                            }
                        else:
                            a['price']+=item2['price']
                        break
    profits=toMoney-fromMoney
    print(newFromDict,newToDict)
    pixiuKing[0]=0
    pixiuKing[1]=0
    for j,k in newToDict.items():
        print("k")
        if piXiu(k['address'])!=0:
            pixiuKing[0]+=1
            if [k]['price']>pixiuKing[1]:
                pixiuKing[1]=[k]['price']
                pixiuKing[2]=[k]['name']
        for s,m in newFromDict.items():
            if k == m:
                coninProfits=newToDict[k]['price']-newFromDict[k]['price']
                newDict[k]={
                    'name':newFromDict[k]['name'],
                    'address':k,
                    'price':coninProfits,
                }
                if coninProfits>profitsMax:
                    profitsMax=coninProfits
                    maxName=newFromDict[k]['name']
                if coninProfits<profitsMin:
                    profitsMin=coninProfits
                    minName=newFromDict[k]['name']
    months=12
    brickDays=int(profits/32)
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
        'maifeiWho':maifeiCoin,
        'maifeiPeak':abs(int(maifeiPeak)),
        'profits':abs(int(profits)),
        'maifei':abs(int(maifeiAll)),
        'winne':winne,
        'howManyPixiu':pixiuKing[0],
        'piXiuName':pixiuKing[1],
        'piXiuPrice':pixiuKing[2],
        'maifeiMax':maifeiMax,
    }
    return context