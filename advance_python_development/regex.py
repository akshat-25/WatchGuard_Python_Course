import re

email = 'akshat@gmail.com'
expression = '[a-z]+'

matches = re.findall(expression,email)

print(matches)

parts = email.split('@')

name = parts[0]
domain = parts[1]

print(name)
print(domain)


price = 'Price: $1987876.98'

expression1 = 'Price: \$([0-9,]*\.[0-9])'

matches_exp = re.search(expression1,price)
print(matches_exp.group(0)) # entire match
print(matches_exp.group(1)) # first thing in brackets

price_number = float(matches_exp.group(1))
print(price_number)