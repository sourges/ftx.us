import json
import requests
import time
import hmac
import base64
import hashlib

api_key = ''
api_secret = ''


def call_code(str_to_sign ,data_json=None, order_id=None):
	now = int(time.time() * 1000)
	signature = base64.b64encode(
		hmac.new(api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
	
	HEADERS = {
		"FTXUS-KEY": api_key,
		"FTXUS-SIGN": signature,
		"FTXUS-T": str(now),
	}
	return HEADERS


def account_info():
	now = int(time.time() * 1000)
	str_to_sign = str(now) + 'GET' + '/wallet/coins'
	HEADERS = call_code(str_to_sign)
	url = ' https://ftx.us/api/wallet/coins'
	response = requests.get(url, headers = HEADERS)
	print(response.status_code)
	print(response.json())

account_info()


# https://ftx.us/api
# /wallet/coins