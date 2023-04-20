from web3 import Web3
import time

# enter your private key.  Be careful with your private key
private_key = "YOURPRIVATEKEY"

# add your blockchain connection information
infura_url = 'ADDYOURINFURAKEY'
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())

# enter the account that the crypto is being sent from
from_account ="ENTERYOURACCOUNT"

# enter a list of accounts that the crypto is being sent to
to_addresses = ("account1", "account2", "account2")

# get from account balance so you can monitor
sending_account_balance = web3.eth.get_balance(from_account)
balance = web3.fromWei(sending_account_balance, "ether")
print(balance)

# loop through each of the to_addresses and send Ether in the amount designated below
for i in to_addresses:
    print(i)

    nonce = web3.eth.getTransactionCount(from_account)

    tx = {
        'nonce': nonce,
        'to': web3.toChecksumAddress(i),
        'value': web3.toWei(.005, 'ether'),
        'gas': 21000,
        'gasPrice': web3.toWei('50', 'gwei')
    }

# sign the transaction and print on the screen
# wait 5 seconds before processing the next transaction
    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    transaction = web3.toHex(tx_hash)
    print(transaction)
    time.sleep(5)