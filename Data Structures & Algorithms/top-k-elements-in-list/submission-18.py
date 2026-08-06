class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        counts = [[] for i in range(len(nums) + 1)]

        for num, count in freq.items():
            counts[count].append(num)
        
        res = []
        for i in range(len(counts)-1, 0, -1):
            if counts[i] != []:
                for num in counts[i]:
                    if k == 0:
                        break
                    res.append(num)
                    k -= 1
        return res




