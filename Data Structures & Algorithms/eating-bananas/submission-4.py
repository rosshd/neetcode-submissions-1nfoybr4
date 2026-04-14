class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:

            mid = (l + r) // 2
            check = 0

            for p in piles:
                check += math.ceil(p / mid)
            if check <= h :
                res = min(mid, res)
                r = mid - 1
            else:
                l = mid + 1
        return res
