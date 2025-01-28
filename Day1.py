class Solution:
    def buttonWithLongestTime(self, a: List[List[int]]) -> int:
        d = {a[0][0]:a[0][1]}
        for i in range(1,len(a)):
            b=a[i][1]-a[i-1][1]
            if a[i][0] in d:
                if b > d[a[i][0]]:
                    d[a[i][0]]=b
            else:
                d[a[i][0]]=b
        max_val = max(d.values())
        l = []
        for k, v in d.items():
            if v == max_val:
                l.append(k)

        j = min(l)
        return j

                
