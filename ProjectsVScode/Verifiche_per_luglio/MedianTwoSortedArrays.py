class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Unisce i due array in un unico array ordinato.
        merged = nums1 + nums2

        # Ordina l'array unito.
        merged.sort()

        # Calcola il numero totale di elementi nell'array unito.
        total = len(merged)

        if total % 2 == 1:
            # Se il numero totale di elementi è dispari, restituisce l'elemento centrale come mediana.
            return float(merged[total // 2])
        else:
            # Se il numero totale di elementi è pari, calcola la media dei due elementi centrali come mediana.
            middle1 = merged[total // 2 - 1]
            middle2 = merged[total // 2]
            return (float(middle1) + float(middle2)) / 2.0

nums1 = [1,3] 
nums2 = [2,7]
soluzione = Solution()
ok = soluzione.findMedianSortedArrays(nums1,nums2)
print(ok)