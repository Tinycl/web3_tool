from web3 import Web3
import json
import requests

# https://ethgasstation.info/

infura_url = 'https://ethereum.publicnode.com'
web3 = Web3(Web3.HTTPProvider(infura_url))

req = requests.get('https://ethgasstation.info/json/ethgasAPI.json')
t = json.loads(req.content)
print('safeLow', t['safeLow'])
print('average', t['average'])
print('fast', t['fast'])
print('fastest', t['fastest'])


#web3.eth.Eth.generateGasPrice
# 1 ETH = 10^18 wei  1,000,000,000,000,000,000
# 1 ETH = 10^9  gwei   gas wei
# 1 gwei = 10^9 wei  1,000,000,000

# total = gas * gasprice (2000gas * 500gwei =1000000 gwei ) 
# gasprice unit is gwei,  one gas how much gwei

gas_price1 = web3.eth.gas_price
print(gas_price1/10**9)