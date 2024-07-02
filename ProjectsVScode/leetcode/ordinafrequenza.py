class Solution:
    def frequencySort(self, s: str) -> str:
        mp:dict={}
        lista:list =[]
        conta = 0
        for i in range(len(s)):
            
                if s[i] == s[i+1]:
                    conta += 1
                    mp[s[i]] = conta
        sorted(mp.items())
        for k in mp.items():
            lista.append(k)
        return str(lista)
s = "tree"
f = Solution()
f.frequencySort(s)