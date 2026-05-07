class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        size = len(strs)
        grouped = []
        for i in range(size):
            sorted_element1 = self.sort(strs[i])
            group = []
            if not(i in grouped):
                group.append(strs[i])
                for j in range(i+1, size):
                    sorted_element2 = self.sort(strs[j])
                    if  not(j in grouped) and (sorted_element1 == sorted_element2):
                        group.append(strs[j])
                        grouped.append(j)
            if group != []:
                res.append(group)
        return res

    def sort(self, str1):
        char_list = list(str1)
        size = len(char_list)
        for i in range(size):
            curr_min = i
            for j in range(i+1, size):
                if char_list[curr_min] > char_list[j] :
                    curr_min = j
            temp = char_list[i]
            char_list[i] = char_list[curr_min]
            char_list[curr_min] = temp
        return "".join(char_list)