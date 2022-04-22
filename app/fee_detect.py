import json
from web3 import Web3
def piXiu(token_address):
	url = 'https://bsc-dataseed.binance.org'
	web3 = Web3(Web3.HTTPProvider(url))
	abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"pairAddr","type":"address"},{"internalType":"address","name":"tokenAddr","type":"address"},{"internalType":"address","name":"_WETH","type":"address"},{"internalType":"uint256","name":"wbnbAmountIn","type":"uint256"}],"name":"detectFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"pairAddr","type":"address"},{"internalType":"address","name":"tokenAddr","type":"address"},{"internalType":"address","name":"_WETH","type":"address"},{"internalType":"uint256","name":"wbnbAmountIn","type":"uint256"}],"name":"detectGas","outputs":[{"internalType":"uint256","name":"gasUsedOfBuy","type":"uint256"},{"internalType":"uint256","name":"gasUsedOfSell","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"name":"withdrawBNB","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountOut","type":"uint256"}],"name":"withdrawToken","outputs":[],"stateMutability":"payable","type":"function"}]')
	# pancake_Factory
	factory_abi = json.loads('[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
	factory_address = '0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73'
	factory_contract = web3.eth.contract(address=factory_address, abi=factory_abi)
	address = '0x4780B172B24cE1fC9e63A4A61378080de4B029B5'
	contract = web3.eth.contract(address=address, abi=abi)

	#returns a address the trading pairs on pancake
	#基础币 如:wbnb，usdt,busd
	WETH = '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'
	#检测的目标币
	#token_address = '0xc40B6e88FD7b09Eb8F768f402bF5dad6bF2bC622'
	#检测的目标币主池子
	pairAddr = factory_contract.functions.getPair(WETH,token_address).call()
	print(pairAddr)
	result = contract.functions.detectFee(pairAddr,token_address,WETH,10000000000000000).call()
	print(result)

	if result==None or len(result)!=2:
		print("貔貅")
		return 1
	else:
		print(result)
		return 0

