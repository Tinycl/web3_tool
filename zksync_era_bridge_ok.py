from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3 import Web3
from zksync2.core.types import Token
from zksync2.module.module_builder import ZkSyncBuilder
from zksync2.provider.eth_provider import EthereumProvider

from termcolor import cprint
import time
import random

'''
pip install web3==6.0.0
pip install zksync2

'''

#Put your PRC provider
#ZKSYNC_URL = "https://mainnet.era.zksync.io"
#ETH_URL = "https://rpc.ankr.com/eth"

ZKSYNC_URL = "https://mainnet.era.zksync.io"
ETH_URL = "https://ethereum.publicnode.com"

# ZKSYNC_URL = "https://zksync2-testnet.zksync.dev"
# ETH_URL = "https://rpc.ankr.com/eth_goerli"

#ZKSYNC_URL = "https://testnet.era.zksync.dev"
#ETH_URL = "https://goerli.blockpi.network/v1/rpc/public"

#Put your transaction price range
MIN_PRICE = 0.001000
MAX_PRICE = 0.001522

# Enter the gwei ammount at which you would like to perform the transaction
GWEI = 300

zksync = ZkSyncBuilder.build(ZKSYNC_URL)
eth_web3 = Web3(Web3.HTTPProvider(ETH_URL))

def deposit(privatekey):

    try:
        amount = round(random.uniform(MIN_PRICE, MAX_PRICE), 8)

        account: LocalAccount = Account.from_key(privatekey)
        eth_provider = EthereumProvider(zksync, eth_web3, account)
        wei_amount = Web3.to_wei(amount, "ether")
        eth_token = Token.create_eth()
        gas_price = eth_web3.eth.gas_price
        operator_tip = eth_provider.get_base_cost(gas_limit=eth_provider.RECOMMENDED_DEPOSIT_L2_GAS_LIMIT, gas_per_pubdata_byte=800,gas_price=gas_price)

        l1_tx_receipt = eth_provider.deposit(token=eth_token,
                                             amount=wei_amount,
                                             gas_per_pubdata_byte=800,
                                             operator_tip=operator_tip)
        
        tx_status = l1_tx_receipt['status']
        if tx_status == 1:
            cprint(f"\n>>> bridge ZkSync Era| Successful transaction! Amount: {amount}, gas price: {eth_web3.from_wei(gas_price, 'gwei')}", "green")
        else:
            cprint(f"\n>>> bridge ZkSync Era| Transaction failed! Tx status: {tx_status}", "red")    

    except Exception as error:
        cprint(f'\n>>> bridge ZkSync Era| {error}', 'red')

if __name__ == "__main__":
    
    '''
    with open("private_keys.txt", "r") as f:
        keys_list = [row.strip() for row in f]
    '''
    keys_list = ['']
    for privatekey in keys_list:
        
        cprint(f'\n=============== start : {privatekey} ===============', 'yellow')
        
        if GWEI == "":
            deposit(privatekey)
        else:     
            stop_this_shit = False
            print(f'Waitting gas value {GWEI}...')
            while not stop_this_shit:
                gas_price = eth_web3.eth.gas_price
                gwei_gas_price = eth_web3.from_wei(gas_price, 'gwei')
                print(gwei_gas_price)
                if gwei_gas_price <= GWEI:    
                    deposit(privatekey)
                    stop_this_shit = True
                else:
                    time.sleep(3)    
        
        time.sleep(random.randint(10, 19)) 