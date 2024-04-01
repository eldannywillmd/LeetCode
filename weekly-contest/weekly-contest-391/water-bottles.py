class Solution:
    def maxBottlesDrunk(self, numBottles, numExchange):
        # drink numBottles -> emptyBottles = numBottles
        # if emptyBottles >= numExchange -> emptyBottles-= numExchange | numBottles += 1 and numExchange += 1
        # drink bottels
        bottlesDrunk = emptyBottles = numBottles
        while True:
            if emptyBottles >= numExchange:
                emptyBottles -= numExchange
                bottlesDrunk += 1
                emptyBottles += 1
                print(bottlesDrunk)
            else:
                return bottlesDrunk

numBottles = 10
numExchange = 3

solution = Solution()
print(solution.maxBottlesDrunk(numBottles, numExchange))
