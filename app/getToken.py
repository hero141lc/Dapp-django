# -*- coding: utf-8 -*-
'''

import datetime
import django
#django.setup()

#from app.models.user import User

'''
import json
from unittest import result
import requests
import datetime
import asyncio

from sqlalchemy import false
from .models import Token,Prices,Trans,Wallet,Lp
from django.db.models import Q,Max
from web3 import Web3
import time
from multiprocessing.pool import ThreadPool
import multiprocessing
import random

pancakeAddr='0x10ed43c718714eb63d5aa57b78b54704e256024e'


#returns a address the trading pairs on pancake
#基础币 如:wbnb，usdt,busd
WETH = '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'
#USDT = 'xxx'
#BUSD = 'xxx'
url = 'https://bsc-dataseed.binance.org'
web3 = Web3(Web3.HTTPProvider(url))


# pancake abi
isLP_abi = json.loads('[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
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

isLPCache = {}

def detectFee(pair_addr,token_addr,base_token_addr):
    return bot_contract.functions.detectFee(pair_addr,token_addr,base_token_addr,10000000000000000).call()


def getPair(token_addr, baseaddr):
    return factory_contract.functions.getPair(WETH,token_addr).call()


def piXiu(token_address):
    start_time = time.time()
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
        end_time = time.time()
        print("Important:piXiu: {:.2f}S".format(end_time - start_time))
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
    start_time = time.time()
    try:
        tokenOb=Token.objects.get(token_address)
        end_time = time.time()
        print("Important:isPixiu: {:.2f}S".format(end_time - start_time))
        if tokenOb.pixiu == True:
            return 1
# temp Pi xiu save

    except:
        tokenOb=exSql(token_address)
        end_time = time.time()
        print("Important:isPixiu: {:.2f}S".format(end_time - start_time))
        if tokenOb.pixiu == True:
            return 1
        else:
            return 0
        print("no")
# Is_LP

def isLP(addr):
    if addr in isLPCache:
        #print("isLP hit in cache",isLPCache[addr],addr)
        return isLPCache[addr]
    a=Lp.objects.filter(address=addr).count()
    print(a)
    if Lp.objects.filter(address=addr).count()>0:
        #isLPCache[addr] = True
        return True
    try:
        contract = web3.eth.contract(address=addr, abi=isLP_abi)
        #need to put .call() at the end to call the smart contract
        symbol = contract.functions.symbol().call()
        print(symbol)
        if symbol=="Cake-LP":
            Lp.objects.create(address=addr,symbol=symbol)
            isLPCache[addr] = True
            return True
        else:
            isLPCache[addr] = False
            return False
    except:
        return False
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

def getPriceFromPancake(tokenAddr):
    try:
        URL = 'https://api.pancakeswap.info/api/v2/tokens/'+tokenAddr
        res = requests.get(URL).text
        data=json.loads(res)['data']
        return data['price']
    except:
        return -1


def newData(contenst,yearsAgo,toDate):
    start_time = time.time()
    #fromDate = '2022-03-14'
    #toDate = '2022-04-15'
    if contenst == '0x94c168468c2ac83073fb1794a66992e4f41ee7bb':
        print('dd')
    URL = 'https://api.covalenthq.com/v1/pricing/historical_by_addresses_v2/56/USD/'+contenst+'/?from='+yearsAgo+'&to='+toDate+'&prices-at-asc=true&page-size=1000&key=ckey_c95724e05a2f4802a387160b08e'
    # 输入在浏览器的网址
    res = requests.get(URL).text
    data=json.loads(res)['data'][0]
    priceList = data['prices']
    npixiu = False
    if piXiu(contenst) != 0:
        npixiu = True
    print("npixiu",npixiu)
    tokenOb= Token.objects.create(decimals=int(data['contract_decimals']),name=data['contract_name'],symbol=data['contract_ticker_symbol'],logo_url=data['logo_url'],address=data['contract_address'],pixiu=npixiu,update_at=datetime.datetime.strptime(data['update_at'][0:11], "%Y-%m-%dT"),quote_currency=data['quote_currency'])
    
    for item in priceList:
        usedPrice=item['price']        
        Prices.objects.create(date=datetime.datetime.strptime(item['date'][0:10], "%Y-%m-%d"),price=usedPrice, Token=tokenOb)
    print('New Coin Added Successed:',data['contract_ticker_symbol'],data['update_at'])
    end_time = time.time()
    print("Important:newData: {:.2f}S".format(end_time - start_time))
    return tokenOb
def getData(tokenOb,fromDate,toDate):
    start_time = time.time()
    #fromDate = '2022-03-14'
    #toDate = '2022-04-15'
    URL = 'https://api.covalenthq.com/v1/pricing/historical_by_addresses_v2/56/USD/'+tokenOb.address+'/?from='+fromDate+'&to='+toDate+'&prices-at-asc=true&page-size=1000&key=ckey_c95724e05a2f4802a387160b08e'
    # 输入在浏览器的网址
    res = requests.get(URL).text
    data=json.loads(res)['data'][0]['prices']
    for item in data:
        Prices.objects.create(date=datetime.datetime.strptime(item['date'][0:10], "%Y-%m-%d"),price=item['price'], Token=tokenOb)
    end_time = time.time()
    print("Important:getData: {:.2f}S".format(end_time - start_time))
    return tokenOb

async def asyncExSql(addr):
    return exSql(addr)

def exSql(contenst):
    start_time = time.time()
    timeNow=datetime.datetime.now()
    toDate=timeNow.date().isoformat()
    try:
        tokenOb=Token.objects.get(address=contenst)
        tokenObTime=tokenOb.update_at.date()
        #print("how long update:",(timeNow.date()-tokenObTime).days)
        if (timeNow.date()-tokenObTime).days>1:
            tokenOb.update_at=timeNow
            tokenOb.save()
            fromDate=tokenObTime.isoformat()
            data=getData(tokenOb,fromDate,toDate)

        else:
            return tokenOb
    except Exception as e:
        print("exSql failed:",e)
        yearsAgo=(timeNow-datetime.timedelta(days=365)).date().isoformat()
        try: 
            data=newData(contenst,yearsAgo,toDate)
        except:
            return 1

    # 发送 GET 方式的请求，并把返回的结果(响应)存储在 res 变量里头
    # 答第二个问题，get() 方法需要输入一个网页链接
    end_time = time.time()
    print("Important:exSql: {:.2f}S".format(end_time - start_time))
    return data
# spirit data to sellTrxList or buyTrxList
def filterToFrom(item):
    if "to" not in item or "from" not in item:
        return 1

    if "contractAddress" not in item or  item["contractAddress"] in ban_token:
        return 1

    userWalletAddress = item["userAddress"]
    userWalletAddress = userWalletAddress.lower()

    if userWalletAddress == item['to'].lower() and isLP(web3.toChecksumAddress(item['from'])):
        return item

    if userWalletAddress == item['from'].lower() and isLP(web3.toChecksumAddress(item['to'])):
        return item

    return 1

def getOrder(address):
    # Global
    sellTrxList=[]
    buyTrxList=[]
    sellTokenList=set()
    buyTokenList=set()
    start_time = time.time()
    address=address.strip().replace('\n', '').replace('\r', '').lower()
    addressRes='address='+address
    userWalletAddress= address
    Token='contractaddress='
    URL='https://api.bscscan.com/api?module=account&action=tokentx&&'+addressRes+'&page=0&offset=1500&startblock=0&endblock=99999999999&sort=asc&apikey=TFD2ZDC1W77QAXP38SF9I1Z6T34GBGIGUJ'
    res = requests.get(URL).text
    data=json.loads(res)['result']
    simpleSellDict={}
    simpleBuyDict={}
    newDict={}
    allTokens=set()
    toPriceList=[]
    fromPriceList=[]
    pricesList=[]
    income=0
    expenditure=0
    times=0
    maxName=''
    minName=''
    maxBuyAmount=0
    maxSellAmount = 0
    totalSellAmount=0
    totalBuyAmount=0
    profitsMax=0
    profitsMin=0
    minName=''
    maxName=''
    sellAll=[]
    maxPriceSince=0
    maifeiAll=0
    maxMaifeiCoin=''
    maifeiPeak=0
    buyAmountOfMax_Maifei=0
    pixiuKing=[0,0,'']
    latestItem={}
    latestItem['tokenSymbol']=''

    for item in data:
        item["userAddress"] = address

    pool = ThreadPool(multiprocessing.cpu_count()*4)
    data=pool.map(filterToFrom, data)

    end_time = time.time()
    print("Important:filterToFrom: {:.2f}S".format(end_time - start_time))


    #parse all transactions && dispatch trx to right category.
    for item in data:
        if  type(item) is not dict:
            #print("item-data:",type(item),item)
            continue
        times+=1
        #sell token to pancake(pair)
        if item['from'] == address:
            sellTokenList.add(item['contractAddress'])
            item['value']=int(item['value'])
            item['time']=datetime.datetime.fromtimestamp(int(item['timeStamp']))
            sellTrxList.append(item)
        #buy token from pancake
        elif item['to'] == address:
            buyTokenList.add(item['contractAddress'])
            item['value']=int(item['value'])            
            item['time']=datetime.datetime.fromtimestamp(int(item['timeStamp']))
            buyTrxList.append(item)

    end_time = time.time()
    print("Important:Foreach Item: {:.2f}S".format(end_time - start_time))

    #all contract of this wallet.
    allTokens = buyTokenList | sellTokenList

    #save or update token info to db.
    pool.map(exSql, allTokens)

    end_time = time.time()
    print("Important:saveOrupdate token: {:.2f}S".format(end_time - start_time))

    tokenPriceDict = {}
    for _token in allTokens:
        #query token info from mysql.
        toeknObject= exSql(_token)
        if toeknObject.pixiu:
            print("Pixiu",toeknObject)
            continue
        if toeknObject==1:
            print("ERROR",toeknObject)
            continue

        # get price of the token pre day.
        dailyPrices=Prices.objects.filter(Token=toeknObject).values()        
        for dailyPrice in dailyPrices:
            tokenPrices={}
            if _token in tokenPriceDict:
                tokenPrices=tokenPriceDict[_token]
            tokenPrices[dailyPrice['date'].date()] = dailyPrice
            tokenPriceDict[_token] = tokenPrices

    for buyTrx in buyTrxList:
        tokenAddr = buyTrx['contractAddress']
        if tokenAddr in tokenPriceDict and buyTrx['time'].date() in tokenPriceDict[tokenAddr]:
        #and 'LP' not in buyTrx['tokenSymbol']:
            buyPrice = tokenPriceDict[tokenAddr][buyTrx['time'].date()]
        else:
            continue

        try:
            decimal =int(buyTrx["tokenDecimal"])
            buyTrx['amount']=int((buyTrx['value']*buyPrice["price"])/10**decimal)

            totalBuyAmount+=buyTrx['amount']

            if buyTrx['amount'] > maxBuyAmount:
                maxBuyAmount = buyTrx['amount']

            simpleBuy=simpleBuyDict.get(buyTrx['contractAddress'])
            if simpleBuy==None:
                simpleBuyDict[buyTrx['contractAddress']]={
                    'name':buyTrx['tokenSymbol'],
                    'address':buyTrx['contractAddress'],
                    'amount':buyTrx['amount'],
                }
            else:
                simpleBuy['amount']+=buyTrx['amount']

        except Exception as e:
            print("ERROR:",e)
            print("contractAddress:",buyTrx['contractAddress'])
            print("tokenSymbol",buyTrx['tokenSymbol'])
    
    for sellTrx in sellTrxList:
        tokenAddr = sellTrx['contractAddress']

        if tokenAddr in tokenPriceDict and sellTrx['time'].date() in tokenPriceDict[tokenAddr]:
        #and 'LP' not in buyTrx['tokenSymbol']:
            sellPrice = tokenPriceDict[tokenAddr][sellTrx['time'].date()]
        else:
            continue

        maxPriceSince = sellPrice
        
        decimal =int(sellTrx["tokenDecimal"])
        sellTrx['amount']=int((sellTrx['value']*sellPrice["price"])/10**decimal)

        prices = tokenPriceDict[tokenAddr]
        for key in prices:
            if key >=sellTrx['time'].date() and prices[key]["price"]>maxPriceSince["price"]:
                maxPriceSince = prices[key]
        
        #Maifei
        print("maxPriceSince:",maxPriceSince["price"],sellPrice['price'])
        if maxPriceSince['price']/(sellPrice['price']+float("1e-8")) > 50:
            maxPriceSince = sellPrice

        maifeiAmount=int(sellTrx['value']*maxPriceSince["price"])/10**decimal-sellTrx['amount']
        maifeiAll+=maifeiAmount
        print("maifei:",maifeiAmount," totalmaifei",maifeiAll)

        if maifeiAmount > 0 and maifeiAmount > maifeiPeak:
            maifeiPeak = maifeiAmount
            maxMaifeiCoin=sellTrx['tokenSymbol']
            buyAmountOfMax_Maifei=sellTrx['amount']

        totalSellAmount+=sellTrx['amount']
        if sellTrx['amount']>maxSellAmount:
            maxSellAmount=sellTrx['amount']

        simpleSell=simpleSellDict.get(sellTrx['contractAddress'])

        if simpleSell==None:
            simpleSellDict[sellTrx['contractAddress']]={
                'name':sellTrx['tokenSymbol'],
                'address':sellTrx['contractAddress'],
                'amount':sellTrx['amount'],
            }
        else:
            simpleSell['amount']+=sellTrx['amount']

    #First buying Coin 
    buyTrxList.sort(key=lambda x:x['time'])

    latestItem['firstTime'] = ''
    latestItem['amount'] = 0
    
    for buyTrx in buyTrxList:
        if 'amount' in buyTrx.keys():
            latestItem=buyTrx
            latestItem['firstTime']=str(latestItem['time'].date().isoformat())
            break

    end_time = time.time()
    print("Important:Foreach allTokens: {:.2f}S".format(end_time - start_time))
    profits=totalSellAmount-totalBuyAmount

    for j,k in simpleSellDict.items():
        for s,m in simpleBuyDict.items():
            if j == s:
                coninProfits=simpleSellDict[j]['amount']-simpleBuyDict[j]['amount']
                newDict[j]={
                    'name':simpleBuyDict[j]['name'],
                    'address':j,
                    'amount':coninProfits,
                }
                #print("coninProfits>profitsMax",simpleSellDict[j],simpleBuyDict[j],coninProfits,profitsMax)
                if coninProfits>profitsMax:
                    profitsMax=coninProfits
                    maxName=simpleBuyDict[j]['name']
                if coninProfits<profitsMin:
                    profitsMin=coninProfits
                    minName=simpleBuyDict[j]['name']

    end_time = time.time()
    print("Important:Foreach NewsellTrxList: {:.2f}S".format(end_time - start_time))

    months=12


    if profits>0:
        winne=1
    else:
        winne=0
    if abs(int(profits))>5000000:
        profits=(random.randint(1000000,2000000))
    if abs(int(profitsMin))>2000000:
        profitsMin=(random.randint(100000,300000))
    if abs(int(profitsMax))>2000000:
        profitsMax=(random.randint(100000,300000))
    if abs(int(maifeiAll))>5000000:
        maifeiAll=(random.randint(1000000,2000000))
    if abs(int(maifeiPeak))>2000000:
        maifeiPeak=(random.randint(100000,300000))
    brickDays=int(profits/32)
    context={
        'months':months,
        'times':times,
        'profitsMax':abs(int(profitsMax)),
        'profitsMin':abs(int(profitsMin)),
        'minName':minName,
        'maxName':maxName,
        'brickDays':abs(int(brickDays)),
        'maifeiWho':maxMaifeiCoin,
        'maifeiPeak':abs(int(maifeiPeak)),
        'profits':abs(int(profits)),
        'maifei':abs(int(maifeiAll)),
        'winne':winne,
        'howManyPixiu':pixiuKing[0],
        'piXiuName':pixiuKing[2],
        'piXiuPrice':abs(int(pixiuKing[1]/1e18)),
        'buyAmountOfMax_Maifei':abs(int(buyAmountOfMax_Maifei)),
        'firstCoin':latestItem['tokenSymbol'],
        'firstTime':latestItem['firstTime'],
        'firstPrice':round(latestItem['amount'],2),
    }
    end_time = time.time()
    print("Important:Result: {:.2f}S".format(end_time - start_time))
    return context
def howManyHoulder():
    start_time = time.time()
    token_addr="0xc4893fEa8547Fb1A4D860518285AF6655424645f"
    url="https://api.covalenthq.com/v1/56/tokens/"+token_addr+"/token_holders/?quote-currency=USD&format=JSON&page-number=0&page-size=100000&key=ckey_c95724e05a2f4802a387160b08e"
    r = requests.get(url)

    data=r.json()
    holders=data["data"]["items"]
    l=len(holders)
    print("brick holders count:")
    print(l)
    end_time = time.time()
    print("howManyHoulder: {:.2f}S".format(end_time - start_time))
    return l

