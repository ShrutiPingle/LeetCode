class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq=[0]*2001
        for i in arr:
            freq[i+1000]+=1
        seen=set()
        for cnt in freq:
            if cnt!=0:
                if cnt in seen:
                    return False
                seen.add(cnt)
        return True