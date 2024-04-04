class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        totalBottles = 0
        emptyBottles = 0

        while True:
            if emptyBottles >= numExchange:
                emptyBottles -= numExchange
                numBottles += 1
                numExchange += 1
            elif numBottles > 0:
                emptyBottles += numBottles
                totalBottles += numBottles
                numBottles = 0
            else:
                return totalBottles