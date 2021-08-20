
from pyPancakeSwap.main import pyPancakeSwap

pancake = pyPancakeSwap(testnet=True)
token = '0x7ef95a0fee0dd31b22626fa2e10ee6a223f8a684'
print("Wallet connection status: ",pancake.connect_wallet('0x2bDE868136430996A7355EC07047e8326cD9268D','fa94732d47a3446588078ea9a2de680fc34a3fc89659cf52e1884ee2febf4be4'))
