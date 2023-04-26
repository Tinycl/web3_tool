import time
from web3 import Web3
from eth_account import Account
from eth_account.signers.local import LocalAccount

web3 = Web3(Web3.HTTPProvider('https://ethereum.publicnode.com'))
print(web3.is_connected())
#print(web3.eth.get_block('latest'))
g_count = 0

while True:
    time.sleep(1)
    newaccount1: LocalAccount = Account.create()
    #print(newaccount1.address)
    newp1 = web3.to_hex(newaccount1._private_key)

    newaccount2: LocalAccount = Account.create()
    #print(newaccount2.address)
    newp2 = web3.to_hex(newaccount2._private_key)

    private_key = newp1[:31] + newp2[32:] 
    #print(newp)

    #address 0x_40bit
    #private 0x_64bit
    account: LocalAccount = Account.from_key(private_key)
    balance = web3.eth.get_balance(account.address)
    #print(account.address)
    #print(balance)
    with open("run.log","w") as flog:
        flog.write(str(g_count))
        flog.write("    ")
        flog.write(account.address)
        flog.write("\n")
        flog.close()
        
    if balance > 1000000000000000:
        print(balance)
        with open("hack.txt","a") as f:
            f.write("\n")
            f.write("address:")
            f.write(account.address) 
            f.write("   key:")
            f.write(private_key)
            f.write("\n")
            f.close() 
