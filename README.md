# Python package for PancakeSwap V0.0.1

![BSC and PancakeSwap logos](images/bsc_pancakeswap.png)


## Description

This repository simplifies the complexity of interacting with the Binance Smart Chain that is a blockchain deployed by Binance. Binance is a cryptocurrency exchange. This library also simplifies interaction with Pancake-swap which is a DeFi exchange.


## Installation

```
git clone https://github.com/deshiyan1010/pyPancakeSwap
cd pyPancakeSwap
python setup.py install
```

## Usage

#### Class Defination

```
class pyPancakSwap.pyPancakeSwap(rpc_endpoint:str=None,testnet:bool=False)
```
Default RPC endpoint:

```

| Testnet   | RPC                                               |
| -----     | ----                                              |
|  False    | 'https://bsc-dataseed.binance.org/'               |
|  True     | 'https://data-seed-prebsc-1-s1.binance.org:8545/' |
| ...       | ...                                               |

Table: Default RPC table
```

#### Connection Check
```
pyPancakeSwap.isConnected(None)
```
Returns True is connected to RPC.


#### Connect Wallet
```
pyPancakeSwap.connect_wallet(self,address:str,private_key:str)
```
Returns True if the public address and private key match eachother and connects wallet.


#### Get Balance
```
pyPancakeSwap.get_balance(self,token_address:str=None,token_abi:str=None)
```
Returns balance of BNB if token address is not mentioned, if mentioned the returns balance of the specified token.
Returns two types of values, true balance and other without decimal.


#### Set Router Address
```
pyPancakeSwap.set_router_address(self,address:str)->None
```
By default PancakeSwap Router is set.


#### Price of token
```
pyPancakeSwap.get_price(self,token:str)->float
```
Returns price of token of the contract address passed.



#### Price of token
```
pyPancakeSwap.get_liquidity(self,token:str)->float
```
Returns liquidity in pool of token of the contract address passed.




#### Buy token
```
pyPancakeSwap.buy_token_with_bnb(self,token_contract_address:str,amount_bnb:float,gas:float=None,gasPrice:float=None,milliseconds_to_expire:int=None,min_tokens_expected:float=None)-> Tuple[TxReceipt, float]
```



#### Approve Transaction
```
approve_token_for_bnb(self,token_contract_address:str,amount_token:float,gas:float=None,gasPrice:float=None) -> Tuple[TxReceipt, float]:
```



#### Sell token
```
pyPancakeSwap.sell_token_for_bnb(self,token_contract_address:str,amount_token:float,gas:float=None,gasPrice:float=None,milliseconds_to_expire:int=None,min_tokens_expected:float=None) -> Tuple[TxReceipt, float]:
```


#### Send BNB
```
pyPancakeSwap.sendBNB(self,amount_bnb:float,receiver_address:str,gas:float=None,gasPrice:float=None,milliseconds_to_expire:int=None) -> Tuple[TxReceipt, float]:
```


## References

- [Web3](https://github.com/ethereum/web3.py)
