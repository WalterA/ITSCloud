class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Insieme per tenere traccia dei caratteri nella finestra corrente
        char_set = set()
        # Inizio della finestra
        start = 0
        # Lunghezza massima della sottostringa senza ripetizioni
        max_length = 0
        for end in range(len(s)):
            # Se il carattere è già nel set, rimuovi i caratteri dall'inizio fino a quando non è più nel set
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1
            # Aggiungi il carattere corrente al set
            char_set.add(s[end])
            # Calcola la lunghezza massima della finestra
            max_length = max(max_length, end - start + 1)
        
        return max_length

# Esempio di utilizzo:
s = "abcabcbb"
solution = Solution()
ok = solution.lengthOfLongestSubstring(s)
print(ok)  # Output: 3
