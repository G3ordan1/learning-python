# c25834950d044993912434171a0914c1
from eth_account import Account
from web3 import Web3

# Replace with your seed phrase
seed_phrase = "focus crater define tray gadget unfold knee crazy grocery donor ill attack"

# Set up Web3 connection to the Ethereum network
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/c25834950d044993912434171a0914c1'))

# Get the private key from the seed phrase
Account.enable_unaudited_hdwallet_features()
private_key = Account.from_mnemonic(seed_phrase).privateKey.hex()

# Create an account object from the private key
account = w3.eth.account.from_key(private_key)

# Print the address and balance of the account
print(f"Address: {account.address}")
balance = w3.eth.get_balance(account.address)
print(f"Balance: {balance} Wei ({w3.from_wei(balance, 'ether')} ETH)")
