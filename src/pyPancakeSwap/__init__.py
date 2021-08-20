from web3 import Web3
from web3.middleware import geth_poa_middleware
from bscscan import BscScan
from typing import Tuple
from decimal import Decimal
import json
import time
from web3.types import TxReceipt, Wei



######  ABI's   ########

panabi_g = '[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_WETH","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"WETH","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"amountADesired","type":"uint256"},{"internalType":"uint256","name":"amountBDesired","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountTokenDesired","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountIn","outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountOut","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsIn","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"reserveA","type":"uint256"},{"internalType":"uint256","name":"reserveB","type":"uint256"}],"name":"quote","outputs":[{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETHSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermit","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermitSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityWithPermit","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapETHForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETHSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'



price_lp_g = '[{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"}]'


sellabi_g = '[{"inputs":[{"internalType":"string","name":"_NAME","type":"string"},{"internalType":"string","name":"_SYMBOL","type":"string"},{"internalType":"uint256","name":"_DECIMALS","type":"uint256"},{"internalType":"uint256","name":"_supply","type":"uint256"},{"internalType":"uint256","name":"_txFee","type":"uint256"},{"internalType":"uint256","name":"_lpFee","type":"uint256"},{"internalType":"uint256","name":"_MAXAMOUNT","type":"uint256"},{"internalType":"uint256","name":"SELLMAXAMOUNT","type":"uint256"},{"internalType":"address","name":"routerAddress","type":"address"},{"internalType":"address","name":"tokenOwner","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"minTokensBeforeSwap","type":"uint256"}],"name":"MinTokensBeforeSwapUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"tokensSwapped","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"ethReceived","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"tokensIntoLiqudity","type":"uint256"}],"name":"SwapAndLiquify","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"enabled","type":"bool"}],"name":"SwapAndLiquifyEnabledUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"_liquidityFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_maxTxAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_taxFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"claimTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tAmount","type":"uint256"}],"name":"deliver","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"excludeFromFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"excludeFromReward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"geUnlockTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"includeInFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"includeInReward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isExcludedFromFee","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isExcludedFromReward","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"time","type":"uint256"}],"name":"lock","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"numTokensSellToAddToLiquidity","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tAmount","type":"uint256"},{"internalType":"bool","name":"deductTransferFee","type":"bool"}],"name":"reflectionFromToken","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"liquidityFee","type":"uint256"}],"name":"setLiquidityFeePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"maxTxPercent","type":"uint256"}],"name":"setMaxTxPercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"swapNumber","type":"uint256"}],"name":"setNumTokensSellToAddToLiquidity","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_enabled","type":"bool"}],"name":"setSwapAndLiquifyEnabled","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"taxFee","type":"uint256"}],"name":"setTaxFeePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"swapAndLiquifyEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rAmount","type":"uint256"}],"name":"tokenFromReflection","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalFees","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"uniswapV2Pair","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"uniswapV2Router","outputs":[{"internalType":"contract IUniswapV2Router02","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"unlock","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'

class pyPancakeSwap:

    def __init__(self,rpc_endpoint:str=None,testnet:bool=False) -> None:
        
        if testnet==False:
            self.rpc = 'https://bsc-dataseed.binance.org/'
            self.web3 = Web3(Web3.HTTPProvider(self.rpc))
            self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
            self.router_address_checksum = self.web3.toChecksumAddress('0x10ed43c718714eb63d5aa57b78b54704e256024e')
            self.WBNB = '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'

        if testnet==True:
            self.rpc = "https://data-seed-prebsc-1-s1.binance.org:8545/"
            self.web3 = Web3(Web3.HTTPProvider(self.rpc))
            self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
            self.router_address_checksum = self.web3.toChecksumAddress('0x9Ac64Cc6e4415144C455BD8E4837Fea55603e5c3')
            self.WBNB = '0xae13d989dac2f0debff460ac112a837c89baa7cd'

        if rpc_endpoint!=None:
            self.rpc = rpc_endpoint

        self.WBNB_CA = self.web3.toChecksumAddress(self.WBNB)
        self.txn_initialized = False
        self.transaction_approved = False

    def isConnected(self)->None:
        return self.web3.isConnected()

    def connect_wallet(self,address:str,private_key:str)->bool:
        if address == self.web3.eth.account.privateKeyToAccount(private_key).address:
            self.address = address
            self.private_key = private_key
            return True
        else:
            return False

    def get_balance(self,token_address:str=None,token_abi:str=None):
        
        if token_address==None:
            balance = self.web3.eth.get_balance(self.address)
            balanceeth = self.web3.fromWei(balance, 'ether')
            return balanceeth,balance
        else:
            if token_abi==None:
                token_abi = sellabi_g
            if token_address==None:
                token_address = self.WBNB

            tokenCA = self.web3.toChecksumAddress(token_address)

            sellTokenContract = self.web3.eth.contract(tokenCA, abi=token_abi)

            decimals = sellTokenContract.functions.decimals().call()
            balance = sellTokenContract.functions.balanceOf(self.address).call()
            true_balance = balance*10**(-decimals)

            return true_balance,balance

    def set_router_address(self,address:str)->None:
        self.router_address_checksum = self.web3.toChecksumAddress(address)
    
    def get_price_lp(self,token:str)->Tuple[float,float]:
        ABI = price_lp_g
        ROUTER_CONTRACT = self.web3.eth.contract(address=self.router_address_checksum, abi=ABI).functions.factory().call()
        ETHER = 10 ** 18

        token = self.web3.toChecksumAddress(token)
        pair = self.web3.eth.contract(address=ROUTER_CONTRACT, abi=ABI).functions.getPair(token, self.WBNB).call()
        pair_contract = self.web3.eth.contract(address=pair, abi=ABI)
        is_reversed = pair_contract.functions.token0().call() == self.WBNB
        decimals = self.web3.eth.contract(address=token, abi=ABI).functions.decimals().call()


        peg_reserve = 0
        token_reserve = 0
        (reserve0, reserve1, _) = pair_contract.functions.getReserves().call()
        
        if is_reversed:
            peg_reserve = reserve0
            token_reserve = reserve1
        else:
            peg_reserve = reserve1
            token_reserve = reserve0
        
        if token_reserve and peg_reserve:
            price = (Decimal(peg_reserve) / ETHER) / (Decimal(token_reserve) / 10 ** decimals)
            
            return float(price),float(peg_reserve/ETHER)
            
        return 0,0

    def get_price(self,token:str)->float:
        return self.get_price_lp(token)[0]

    def get_liquidity(self,token:str)->float:
        return self.get_price_lp(token)[1]

    
    def txn_initializer(self)->None:
        self.panabi = panabi_g
        self.sellabi = sellabi_g
        self.txn_initialized = True


    def buy_token_with_bnb(self,token_contract_address:str,amount_bnb:float,gas:float=None,gasPrice:float=None,milliseconds_to_expire:int=None,min_tokens_expected:float=None)-> Tuple[TxReceipt, float]:
        
        if gas==None:
            gas = 250000
        if gasPrice==None:
            gasPrice = 5
        if milliseconds_to_expire==None:
            milliseconds_to_expire=1000000000
        if min_tokens_expected==None:
            min_tokens_expected = 0
        
        
        tokenCA = self.web3.toChecksumAddress(token_contract_address)
        if self.txn_initialized != True:
            self.txn_initializer()

        contract = self.web3.eth.contract(address=self.router_address_checksum, abi=self.panabi)
        nonce = self.web3.eth.get_transaction_count(self.address)

        pancakeswap2_txn = contract.functions.swapExactETHForTokens(
            min_tokens_expected,
            [self.WBNB_CA, tokenCA],
            self.address,
            (int(time.time()) + milliseconds_to_expire)
        ).buildTransaction({
            'from': self.address,
            'value': self.web3.toWei(amount_bnb, 'ether'),
            'gas': gas,
            'gasPrice': self.web3.toWei(str(gasPrice), 'gwei'),
            'nonce': nonce,
        })

        signed_txn = self.web3.eth.account.sign_transaction(pancakeswap2_txn, private_key=self.private_key)
        tx_token = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        t1 = time.time()
        tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_token)
        t_to_complete = time.time()-t1

        return tx_receipt,t_to_complete

    def approve_token_for_bnb(self,token_contract_address:str,amount_token:float,gas:float=None,gasPrice:float=None) -> Tuple[TxReceipt, float]:
        
        if gas==None:
            gas = 250000
        if gasPrice==None:
            gasPrice = 5
        
        
        tokenCA = self.web3.toChecksumAddress(token_contract_address)
        if self.txn_initialized != True:
            self.txn_initializer()

        sellTokenContract = self.web3.eth.contract(tokenCA, abi=self.sellabi)

        approve = sellTokenContract.functions.approve(str(self.router_address_checksum), amount_token).buildTransaction({
                'from': self.address,
                'gas': gas,
                'gasPrice': self.web3.toWei(gasPrice,'gwei'),
                'nonce': self.web3.eth.get_transaction_count(self.address),
                })

        signed_txn = self.web3.eth.account.sign_transaction(approve, private_key=self.private_key)
        tx_token = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)


        t1 = time.time()
        approval_tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_token)
        approval_time = time.time()-t1
        self.transaction_approved = True
        return approval_tx_receipt,approval_time

    def sell_token_for_bnb(self,token_contract_address:str,amount_token:float,gas:float=None,gasPrice:float=None,milliseconds_to_expire:int=None,min_tokens_expected:float=None) -> Tuple[TxReceipt, float]:
        
        if gas==None:
            gas = 250000
        if gasPrice==None:
            gasPrice = 5
        if milliseconds_to_expire==None:
            milliseconds_to_expire=1000000000
        if min_tokens_expected==None:
            min_tokens_expected = 0
        
        
        tokenCA = self.web3.toChecksumAddress(token_contract_address)

        if self.transaction_approved==False:
            self.approve_token_for_bnb(token_contract_address,amount_token,gas,gasPrice)
        
        self.transaction_approved = False


        contract = self.web3.eth.contract(address=self.router_address_checksum, abi=self.panabi)

        pancakeswap2_txn = contract.functions.swapExactTokensForETH(
                amount_token ,min_tokens_expected, 
                [tokenCA, self.WBNB_CA],
                self.address,
                (int(time.time()) + milliseconds_to_expire)
                )
    
        try:
            gas_limit = Wei(int(Decimal(pancakeswap2_txn.estimateGas({'from': self.address, 'value': Wei(0)})) * Decimal(1.5)))
        except:
            pancakeswap2_txn = contract.functions.swapExactTokensForETHSupportingFeeOnTransferTokens(
                    amount_token ,min_tokens_expected, 
                    [tokenCA, self.WBNB_CA],
                    self.address,
                    (int(time.time()) + milliseconds_to_expire)
                    )
            try:
                    gas_limit = Wei(int(Decimal(pancakeswap2_txn.estimateGas({'from': self.address, 'value': Wei(0)})) * Decimal(1.5)))
            except Exception:
                print('Can\'t get gas estimate, cancelling transaction.')
                return None

        pancakeswap2_txn = pancakeswap2_txn.buildTransaction({
                    'from': self.address,
                    'gas': gas,
                    'gasPrice': self.web3.toWei(str(gasPrice),'gwei'),
                    'nonce': self.web3.eth.get_transaction_count(self.address),
                    })
        signed_txn = self.web3.eth.account.sign_transaction(pancakeswap2_txn, private_key=self.private_key)
        tx_token = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)


        t1 = time.time()
        tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_token)
        sell_time = time.time()-t1
        return tx_receipt,sell_time


    def sendBNB(self,amount_bnb:float,receiver_address:str,gas:float=None,gasPrice:float=None,milliseconds_to_expire:int=None) -> Tuple[TxReceipt, float]:
        if gas==None:
            gas = 250000
        if gasPrice==None:
            gasPrice = 5
        if milliseconds_to_expire==None:
            milliseconds_to_expire=1000000000

        nonce = self.web3.eth.getTransactionCount(self.address)
        receiver = self.web3.toChecksumAddress(receiver_address)
        tx = {
            'nonce':nonce,
            'to':receiver,
            'value':self.web3.toWei(amount_bnb,'ether'),
            'gas':gas,
            'gasPrice': self.web3.toWei(gasPrice,'gwei')
        }

        sign_txn = self.web3.eth.account.signTransaction(tx, self.private_key)   
        txn_hash = self.web3.eth.sendRawTransaction(sign_txn.rawTransaction)
        t1 = time.time()
        tx_receipt = self.web3.eth.wait_for_transaction_receipt(txn_hash)
        txn_time = time.time()-t1

        return tx_receipt,txn_time





    def send_transaction(receiver_address:str,amount:float,token_contract_address:str):
        pass