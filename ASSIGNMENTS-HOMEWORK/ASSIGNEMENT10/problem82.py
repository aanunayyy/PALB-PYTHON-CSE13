def min_add_to_make_valid(s):
    balance = 0
    add = 0
    
    for ch in s:
        if ch == '(':
            balance += 1
        else:
            if balance > 0:
                balance -= 1
            else:
                add += 1
    
    return add + balance
