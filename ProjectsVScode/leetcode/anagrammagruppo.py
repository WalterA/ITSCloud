class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         #anagram strings are after sorting the same 
        mp ={}
        for s in strs:
            f=str(sorted(s))
            if f not in mp:
                mp[f]=[]
            mp[f].append(s)
        return list(mp.values())
strs = ["eat","tea","tan","ate","nat","bat"]
d=Solution()
print(d.groupAnagrams(strs))