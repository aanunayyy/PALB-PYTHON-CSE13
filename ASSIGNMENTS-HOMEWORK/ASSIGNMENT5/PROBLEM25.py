def is_palindrome(num):
    return str(num) == str(num)[::-1]

def all_palindrome(arr):
    for num in arr:
        if not is_palindrome(num):
            return False
    return True


print(all_palindrome([111,222,333]))
