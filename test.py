import json
from web3 import Web3

url = 'https://bsc-dataseed.binance.org'
web3 = Web3(Web3.HTTPProvider(url))

abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"pairAddr","type":"address"},{"internalType":"address","name":"tokenAddr","type":"address"},{"internalType":"address","name":"_WETH","type":"address"},{"internalType":"uint256","name":"wbnbAmountIn","type":"uint256"}],"name":"detectFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"pairAddr","type":"address"},{"internalType":"address","name":"tokenAddr","type":"address"},{"internalType":"address","name":"_WETH","type":"address"},{"internalType":"uint256","name":"wbnbAmountIn","type":"uint256"}],"name":"detectGas","outputs":[{"internalType":"uint256","name":"gasUsedOfBuy","type":"uint256"},{"internalType":"uint256","name":"gasUsedOfSell","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"name":"withdrawBNB","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountOut","type":"uint256"}],"name":"withdrawToken","outputs":[],"stateMutability":"payable","type":"function"}]')
address = '0x4780B172B24cE1fC9e63A4A61378080de4B029B5'
contract = web3.eth.contract(address=address, abi=abi)

#do not modify the above code.

#eth_call example of detect fee.  
#基础币 如:wbnb，usdt,busd
WETH = '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'
#检测的目标币
token_address = '0xc40B6e88FD7b09Eb8F768f402bF5dad6bF2bC622'
#检测的目标币主池子
#pair_address = '0xF63eaC3B0094b1E9751B71ACB8AA487FD96996f8'
pair_address = contract.functions.getPair(WETH,token_address).call()
result = contract.functions.detectFee(pair_address,token_address,WETH,10000000000000000).call()
print(result)

if result==NULL or len(result)!=128:
	print("貔貅")
else:
	print(result)
