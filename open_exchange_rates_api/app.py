import time

from libs.openexchangerates import OpenExchangeClient

APP_ID = "4a56eaa0d4174928a2cbc474554b7b6a"
client = OpenExchangeClient(APP_ID)

usd_amount = 1000

start = time.time()
gbp_amount = client.convert(usd_amount,"USD","GBP")
end = time.time()

print(end-start)

start = time.time()
gbp_amount = client.convert(usd_amount,"USD","GBP")
end = time.time()
print(end-start)

start = time.time()
gbp_amount = client.convert(usd_amount,"USD","GBP")
end = time.time()
print(end-start)

print(f"USD {usd_amount} is GBP {gbp_amount:.2f} ")