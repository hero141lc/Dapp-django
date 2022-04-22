import json
from web3 import Web3

url = 'https://bsc-dataseed.binance.org'
web3 = Web3(Web3.HTTPProvider(url))

abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]')
address = '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'

contract = web3.eth.contract(address=address, abi=abi)

#need to put .call() at the end to call the smart contract
totalSupply = contract.functions.totalSupply().call()

#convert supply to Wei witch is 18 decimal places)
print('Total Supply: ', totalSupply/1000000)
print('Contract Name: ', contract.functions.name().call())
print('Symbol: ', contract.functions.symbol().call())

#wallet balance 
balanceOfBNB = web3.eth.get_balance("0x9b7Eb1330a9EE08150E4e79A332A62e54eDBf91C")
print('0x9b7Eb1330a9EE08150E4e79A332A62e54eDBf91C balance: ', balanceOfBNB)

#to check sum address
checkSumAddress = web3.toChecksumAddress("0xbb85a30e1251afd9f438b729d596a669f86868c3")
print(checkSumAddress)
