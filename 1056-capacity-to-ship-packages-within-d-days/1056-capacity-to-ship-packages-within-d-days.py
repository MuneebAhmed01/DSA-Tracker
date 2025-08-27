class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(weights, days, mid):
            counter = 1
            total = 0
            for n in weights:
                if total + n <= mid:
                    total += n
                else:
                    counter += 1
                    total = n
                    if counter > days:
                        return False
            return True

        start = max(weights)
        end = sum(weights)     
        while start < end:
            mid = (start + end) // 2
            if canShip(weights, days, mid):
                end = mid
            else:
                start = mid + 1
        return start

        