from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    
    for word in strs:
        key = "".join(sorted(word))
        anagrams[key].append(word)
        
    return list(anagrams.values())
