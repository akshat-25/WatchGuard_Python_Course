accounts = {
    'current' : 1000.00,
    'saving' : 2000.00
}

def add_balance(amount: float, name: str = 'current') -> float:
    accounts[name] += amount
    return accounts[name]

add_balance(500,'saving')
print(accounts)

add_balance(1000)

print(accounts)

# Any arguement that has default value have to follow the arguements that do not have default values.