class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [ (p,s) for p, s in zip(position, speed)]

        cars.sort(reverse = True)

        stk = collections.deque()

        for car in cars:
            pos = car[0] # in miles
            speed = car[1] # in miles/hr
            time = (target - pos) / speed

            stk.append(time)
            if len(stk) >= 2 and stk[-1]<= stk[-2]:
                stk.pop()

        return len(stk)
