class Solution:
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1
        
        def canMake(bloomDay, m, k, mid):
            bouqet = 0
            counter = 0
            for bloom in bloomDay:
                if bloom <= mid:
                    counter += 1
                    if counter == k:
                        bouqet += 1
                        counter = 0
                else:
                    counter = 0
                if bouqet >= m:
                    return True
            return False
        
        start, end = min(bloomDay), max(bloomDay)
        while start < end:
            mid = (start + end) // 2
            if canMake(bloomDay, m, k, mid):
                end = mid
            else:
                start = mid + 1
        
        return start
