from eth_account import Account
from web3 import Web3

# define the path to the seed phrase file
seed_file = 'shuffled_lists.txt'
with open('key.txt') as f:
    key = f.read().strip("\n")

# open the seed phrase file and read its contents
with open(seed_file) as f:
    seed_phrases = f.read().splitlines()

# Set up Web3 connection to the Ethereum network
w3 = Web3(Web3.HTTPProvider(key))
for s in seed_phrases:
    try: 
        # Get the private key from the seed phrase
        Account.enable_unaudited_hdwallet_features()
        private_key = Account.from_mnemonic(s).privateKey.hex()
        if str(w3.eth.account.from_key(private_key)) == '0x2019aBe846f1781546565dd302b24442062D5297':
            print('got it')
            # Create an account object from the private key
            account = w3.eth.account.from_key(private_key)

            # Print the address and balance of the account
            print(f"Address: {account.address}")
            balance = w3.eth.get_balance(account.address)
            print(f"Balance: {balance} Wei ({w3.fromWei(balance, 'ether')} ETH)")
        else: 
            pass
#            print("Thats not the one")
 #           account = w3.eth.account.from_key(private_key)
  #          balance = w3.eth.get_balance(account.address)
    #        print(f"Balance: {balance} Wei ({w3.fromWei(balance, 'ether')} ETH)")
    except:
        pass
