class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # the rates will change
        # fastest rate is max/hr (size of the list) will be done in N hours
        #  what is the minimum???

        # once you figure out the min, we can do a bin search to find the hour
        
        # min, max of the rate
        l, r = 1, max(piles)

        res = r

        while (l <= r):
            k = l + ((r - l) // 2) # higher k means faster lower means slower,
            #we want to find least k
            #so if its faster time  dec k
            #if it's a slower time inc k
            total_hours = sum(math.ceil(p / k) for p in piles)
            
            if total_hours <= h: # fast but can we do more? 
                res = k
                r = k - 1
            else : # too slow so increase k
                l = k + 1
                
        # change rate
        
        return res


        

        