class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dt = {}
        for i in range(len(nums)):
            dt[nums[i]] = dt.get(nums[i], 0) + 1
        freq = sorted(dt.items(), key = lambda items : items[1], reverse = True)
        lst = []
        for i in freq:
            lst.append(i[0])
            k -= 1
            if k == 0:
                break
        return lst