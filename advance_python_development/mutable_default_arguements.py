def create_account(name: str, holder: str, account_holders: list= []):
    account_holders.append(holder)
    
    return {
        'name' : name,
        'main_account_holder': holder,
        'account_holders': account_holders
    }
    
a1 = create_account('savings', 'Akshat')
print(a1)

a2 = create_account('current','mudit')
print(a2)

a3 = create_account('current','parakh',["abc","def"])
print(a3)