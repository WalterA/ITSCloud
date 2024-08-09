"""Scrivere una funzione per trovare la stringa di prefisso 
comune più lunga tra un array di stringhe.

Se non è presente alcun prefisso comune, restituisce una stringa vuota."""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        prefisso = strs[0]
        for s in strs[1:]:
            while s[:len(prefisso)] != prefisso:
                prefisso = prefisso[:-1]
                if not prefisso:
                    return ""
        return prefisso
strs=["flower","flowr","flw","flow"]
sol = Solution()
print(sol.longestCommonPrefix(strs))

