class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq = [[] for i in range (len(nums)+1)]
        for key, item in count.items():
            freq[item].append(key)
        
        res = []
        j = 0
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return []
        




