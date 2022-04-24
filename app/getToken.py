# -*- coding: utf-8 -*-
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
import time
pancakeAddr='0x10ed43c718714eb63d5aa57b78b54704e256024e'


#returns a address the trading pairs on pancake
#基础币 如:wbnb，usdt,busd
WETH = '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'
#USDT = 'xxx'
#BUSD = 'xxx'
url = 'https://bsc-dataseed.binance.org'
web3 = Web3(Web3.HTTPProvider(url))

#pancake_Factory
factory_abi = json.loads('[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
factory_address = '0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73'
factory_contract = web3.eth.contract(address=factory_address, abi=factory_abi)
#detect bot 
bot_abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"pairAddr","type":"address"},{"internalType":"address","name":"tokenAddr","type":"address"},{"internalType":"address","name":"_WETH","type":"address"},{"internalType":"uint256","name":"wbnbAmountIn","type":"uint256"}],"name":"detectFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"pairAddr","type":"address"},{"internalType":"address","name":"tokenAddr","type":"address"},{"internalType":"address","name":"_WETH","type":"address"},{"internalType":"uint256","name":"wbnbAmountIn","type":"uint256"}],"name":"detectGas","outputs":[{"internalType":"uint256","name":"gasUsedOfBuy","type":"uint256"},{"internalType":"uint256","name":"gasUsedOfSell","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"name":"withdrawBNB","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountOut","type":"uint256"}],"name":"withdrawToken","outputs":[],"stateMutability":"payable","type":"function"}]')
bot_address = '0x4780B172B24cE1fC9e63A4A61378080de4B029B5'
bot_contract = web3.eth.contract(address=bot_address, abi=bot_abi)
ban_token = ['0xe9e7cea3dedca5984780bafc599bd69add087d56','0x55d398326f99059ff775485246999027b3197955','0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c','0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d','0x1af3f329e8be154074d8769d1ffa4ee058b1dbc3','0x2170ed0880ac9a755fd29b2688956bd959f933f8'
]
def detectFee(pair_addr,token_addr,base_token_addr):
    return bot_contract.functions.detectFee(pair_addr,token_addr,base_token_addr,10000000000000000).call()


def getPair(token_addr, baseaddr):
    return factory_contract.functions.getPair(WETH,token_addr).call()

def piXiu(token_address):
    try:
        #Ban Busd 
        if token_address=='0xe9e7cea3dedca5984780bafc599bd69add087d56':
            return 0
        #ingore lower case
        checksumed_token_address = web3.toChecksumAddress(token_address) 
        pairAddr = getPair(checksumed_token_address,WETH)
        if pairAddr==None:
            print("empty pair address")
            return
            
        print(pairAddr)


        result = detectFee(pairAddr, checksumed_token_address, WETH)
        print(result,type(result))
        if result==None or len(result)!=2:
            print("unsellable")
            return 1
        if result==[0, 0]:
            print("unsellable")
            return 1

        else:
            print(result)
            return 0
    except:
        return 0
#常规检测貔貅
def isPixiu(token_address):
    try:
        tokenOb=Token.objects.get(token_address)
        if tokenOb.pixiu == True:
            return 1
        else:
            return 0
    except:
        tokenOb=exSql(token_address)
        if tokenOb.pixiu == True:
            return 1
        else:
            return 0
        print("no")
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
    npixiu = False
    if piXiu(contenst) != 0:
        npixiu = True
    print("npixiu",npixiu)
    tokenOb= Token.objects.create(decimals=int(data['contract_decimals']),name=data['contract_name'],symbol=data['contract_ticker_symbol'],logo_url=data['logo_url'],address=data['contract_address'],update_at=datetime.datetime.strptime(data['update_at'][0:11], "%Y-%m-%dT"),quote_currency=data['quote_currency'],pixiu=npixiu)
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
        try: 
            data=newData(contenst,yearsAgo,toDate)
        except:
            return 1

    # 发送 GET 方式的请求，并把返回的结果(响应)存储在 res 变量里头
    # 答第二个问题，get() 方法需要输入一个网页链接
    return data
def getOrder(address):
    start_time = time.time()
    address=address.strip().replace('\n', '').replace('\r', '').lower()
    addressRes='address='+address
    Token='contractaddress='
    URL='https://api.bscscan.com/api?module=account&action=tokentx&&'+addressRes+'&page=1&offset=10000&startblock=0&endblock=99999999999&sort=asc&apikey=TFD2ZDC1W77QAXP38SF9I1Z6T34GBGIGUJ'
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
        print("item-data:",item)
    
        if item['contractAddress']!=None and item['contractAddress'] in ban_token:
            continue
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
    #print(bossList,fromNameList,toNameList)
    for i in bossList:
 
        toeknOb=exSql(i)
        if toeknOb==1:
            break
        priceOb=Prices.objects.filter(Token=toeknOb).values()
        for item  in priceOb:
            for item2 in fromList:
                if item2['contractAddress'] == toeknOb.address and 'LP' not in item2['tokenSymbol']:
                    if item2['time'].date()==item['date'].date():
                        try:
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
            
                            if a==None:
                                newFromDict[item2['contractAddress']]={
                                    'name':item2['tokenSymbol'],
                                    'address':item2['contractAddress'],
                                    'price':item2['price'],
                                }
                            else:
                                a['price']+=item2['price']
                        except Exception as e:
                            print("ERROR:",e)
                            print("contractAddress:",item2['contractAddress'])
                            print("tokenSymbol",item2['tokenSymbol'])

                        break
            for item2 in toList:
                if item2['contractAddress'] == toeknOb.address and 'LP' not in item2['tokenSymbol']:
                   
                    if item2['time'].date()==item['date'].date():
                    
                        item2['price']=int(item2['value']*item['price'])
              
                        toMoney+=item2['price']
                        if item2['price']>maxPrice:
                            maxPrice=item2['price']

                        a=newToDict.get(item2['contractAddress'])
              
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
    print(newFromDict)
    print(newToDict)
    for j,k in newToDict.items():
        print("k")
        try:
            a=isPixiu(k['address'])
        except:
            a=0
        if a!=0:
            pixiuKing[0]+=1
            if k['price']>pixiuKing[1]:
                pixiuKing[1]=k['price']
                pixiuKing[2]=k['name']
            break
        for s,m in newFromDict.items():
            if j == s:
                coninProfits=newToDict[j]['price']-newFromDict[j]['price']
                newDict[j]={
                    'name':newFromDict[j]['name'],
                    'address':j,
                    'price':coninProfits,
                }
                print("coninProfits>profitsMax",newToDict[j],newFromDict[j],coninProfits,profitsMax)
                if coninProfits>profitsMax:
                    profitsMax=coninProfits
                    maxName=newFromDict[j]['name']
                if coninProfits<profitsMin:
                    profitsMin=coninProfits
                    minName=newFromDict[j]['name']
    months=12
    brickDays=int(profits/1e19/32)
    if profits>0:
        winne=1
    else:
        winne=0
    context={
        'months':months,
        'times':times,
        'profitsMax':abs(int(profitsMax/1e19)),
        'profitsMin':abs(int(profitsMin/1e19)),
        'minName':minName,
        'maxName':maxName,
        'brickDays':abs(int(brickDays)),
        'maifeiWho':maifeiCoin,
        'maifeiPeak':abs(int(maifeiPeak/1e19)),
        'profits':abs(int(profits/1e19)),
        'maifei':abs(int(maifeiAll/1e19)),
        'winne':winne,
        'howManyPixiu':pixiuKing[0],
        'piXiuName':pixiuKing[2],
        'piXiuPrice':abs(int(pixiuKing[1]/1e19)),
        'maifeiMax':maifeiMax,
    }
    end_time = time.time()
    print("Important:Result: {:.2f}S".format(end_time - start_time))
    return context
def howManyHoulder():
    token_addr="0xc4893fEa8547Fb1A4D860518285AF6655424645f"
    url="https://api.covalenthq.com/v1/56/tokens/"+token_addr+"/token_holders/?quote-currency=USD&format=JSON&page-number=0&page-size=100000&key=ckey_c95724e05a2f4802a387160b08e"
    r = requests.get(url)

    data=r.json()
    holders=data["data"]["items"]
    l=len(holders)
    print("brick holders count:")
    print(l)
    return l

