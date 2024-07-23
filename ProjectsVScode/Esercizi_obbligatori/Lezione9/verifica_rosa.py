# Data una stringa
# s
# e una lista di stringhe
# wordDict
# , restituisce
# True
# se
# s
# può essere segmentato in una sequenza separata da spazi diuna o più parole del dizionario;
# False
# altrimenti.
# Tieni presente che la stessa parola nel dizionario può essereriutilizzata più volte nella segmentazione.
from collections import defaultdict


def word_break(s:str,wordDict:list[str])->bool:
    for i in wordDict:
        if i in s:
            s= s.replace(i,"")
    if s == "":
        return True
    else:
        return False
    
# print(word_break("leetcode",["leet","code"]))
# print(word_break("applepenapple", ["apple","pen"]))
# print(word_break("catsandog",["cats","dog","sand","and","cat"]))

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
strs = ["eat","tea","tan","ate","nat","bat"]
ok=Solution()
print(ok.groupAnagrams(strs))