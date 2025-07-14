"""Currency Converter."""

import json

import requests

source_code = input().lower()
url = f"http://www.floatrates.com/daily/{source_code}.json"
response = requests.get(url)
data = json.loads(response.text)

rates = {}
if source_code != "usd":
    rates["usd"] = data["usd"]["rate"]
if source_code != "eur":
    rates["eur"] = data["eur"]["rate"]

while target_code := input().lower():
    amount = int(input())

    print("Checking the cache...")
    rate = rates.get(target_code, 0)
    if rate:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        rate = data[target_code]["rate"]
        rates[target_code] = rate

    print(f"You received {amount * rate:.2f} {target_code.upper()}.")
