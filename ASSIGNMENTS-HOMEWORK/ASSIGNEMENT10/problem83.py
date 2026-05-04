def score_of_parentheses(s):
    stack = [0]
    
    for ch in s:
        if ch == '(':
            stack.append(0)
        else:
            val = stack.pop()
            score = max(2 * val, 1)
            stack[-1] += score
    
    return stack[0]
