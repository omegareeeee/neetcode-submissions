class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #need to use backet sort
        #first get a count of the values
        my_dict = dict()
        for i in nums:
            my_dict[i] = 1 + my_dict.get(i,0)
        
        buckets = [[] for _ in range(len(nums) + 1)]

        #append the keys from least to greatest to the busckets
        for key, value in my_dict.items():
            buckets[value].append(key)

        #finally loop backwards and append the most used values
        new_list = []
        for num in range(len(buckets) -1, -1, -1):
            for n in buckets[num]: #important to loop through a list
                if len(new_list) == k:
                    break
                new_list.append(n)
        return new_list