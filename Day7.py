class Solution:
    def pickGifts(self, s: List[int], k: int) -> int:
        for i in range(k):
            s.sort(reverse=True)
            s[0] = int(s[0] ** 0.5)
        return (sum(s))
            
                
