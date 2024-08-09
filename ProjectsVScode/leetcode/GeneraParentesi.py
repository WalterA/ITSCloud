"""22.Date le coppie di parentesi,
scrivi una funzione per generare tutte le combinazioni di parentesi ben formate.n
"""
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        lista = []
        aperto = 0
        chiuso = 0
        while aperto != n:
            lista.append("("*n)
            aperto += 1
            if chiuso < aperto:
                lista.append(")")
                chiuso += 1
        return lista
n=3
sol = Solution()
print(sol.generateParenthesis(n))        