def min_swaps(s1, s2):
    if len(s1) != len(s2):
        return -1
    
    ones1 = s1.count('1')
    ones2 = s2.count('1')
    
    if ones1 != ones2:
        return -1
    
    mismatch1 = []
    mismatch2 = []
    
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if s1[i] == '1':
                mismatch1.append(i)
            else:
                mismatch2.append(i)
    
    return len(mismatch1)
