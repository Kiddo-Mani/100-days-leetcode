class Solution:
    def chalkReplacer(self, c: List[int], k: int) -> int:
        p = len(c)
        k = k % sum(c)
        for i in range(p):
            if k < c[i]:
                return i
            k -= c[i]
            
