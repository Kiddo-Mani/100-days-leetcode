class Solution:
    def rotate(self, s: List[int], k: int) -> None:
        f = len(s)
        k = k % f 
        s[:] = s[-k:] + s[:-k]
        return s
