import requests

# Menentukan API endpoint untuk harga trading pair BTC/ETH
btc_eth_api_url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCETH'

# Menentukan API endpoint untuk harga trading pair ETH/BNB
eth_bnb_api_url = 'https://api.binance.com/api/v3/ticker/price?symbol=ETHBNB'

# Menentukan API endpoint untuk harga trading pair BNB/BTC
bnb_btc_api_url = 'https://api.binance.com/api/v3/ticker/price?symbol=BNBBTC'

# Mengambil data harga untuk trading pair BTC/ETH, ETH/BNB, dan BNB/BTC melalui API Binance
btc_eth_price = float(requests.get(btc_eth_api_url).json()['price'])
eth_bnb_price = float(requests.get(eth_bnb_api_url).json()['price'])
bnb_btc_price = float(requests.get(bnb_btc_api_url).json()['price'])

# Menghitung perbedaan harga untuk triangular arbitrage
price_diff = (1 / btc_eth_price) * eth_bnb_price * bnb_btc_price - 1

# Mencetak hasil perhitungan
print('Perbedaan harga untuk triangular arbitrage: {:.8f}'.format(price_diff))
