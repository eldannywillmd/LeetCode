class Solution:
    def trap(self, height):
        water = 0

        # find local min:
        for h in reversed(range(1, max(height) + 1)):
            water += self.calculate_water_in_line(height, h)

        return water

    def calculate_water_in_line(self, height, h):
        blocks = []
        water = 0

        for index, element in enumerate(height):
            if element >= h:
                blocks.append(index)
                if len(blocks) > 1 and blocks[-1] - blocks[-2] > 1:
                    water += blocks[-1] - blocks[-2] - 1

        return water

    def trap2(self, height):

        reservoir = 0
        water_pot = [0]
        water_tower = [0]

        for step in range(1, len(height)):
            # if goes up the hill
            if height[step] > height[step - 1]:

                water_tower.append(water_tower[-1] - (height[step] - height[step - 1]))
                # water tower cannot be negative
                if water_tower[-1] < 0:
                    water_tower[-1] = 0

                water_pot.append(water_tower[-1])

                # if the hill > water_level -> fill the reservoir / empty the water_pot
                if water_tower[-1] == 0 and len(water_pot) > 0:
                    for i in water_pot:
                        reservoir += i
                    water_pot = [0]

            # if height is the same, water level doesn't change, tower is the same
            elif height[step] == height[step - 1]:
                water_pot.append(water_tower[-1])

            # if goes down the hill, water tower is taller
            else:
                water_tower.append(water_tower[-1] + height[step - 1] - height[step])
                water_pot.append(water_tower[-1])

        # level the water pot to make sure no puddle is left behind
        puddles = 1
        while puddles != 0:
            if len(water_pot) > 1:
                water_pot, puddles = self.add_puddles(water_pot)
                reservoir += puddles
            else:
                puddles = 0

        return reservoir

    def add_puddles(self, water_pot):

        puddles = 0

        # find local maximums
        for i in range(len(water_pot) - 1):
            if water_pot[i] > water_pot[i - 1] and water_pot[i] >= water_pot[i + 1] and water_pot[i] > 1:
                # check which side is higher and choose the lowest
                index = i
                if water_pot[i] == water_pot[i + 1]:
                    while index < len(water_pot) - 2 and water_pot[index] == water_pot[index + 1]:
                        index += 1
                if water_pot[i] > water_pot[index + 1] > water_pot[i - 1]:
                    if water_pot[i] - water_pot[index + 1] > 0:
                        puddles += water_pot[i] - water_pot[index + 1]
                    else: puddles += puddles
                    water_pot[i] = water_pot[index + 1]
                elif water_pot[i] > water_pot[i - 1] >= water_pot[index + 1]:
                    if water_pot[i] - water_pot[i - 1] > 0:
                        puddles += water_pot[i] - water_pot[i - 1]
                    else:
                        puddles += puddles
                    water_pot[i] = water_pot[i - 1]

        return water_pot, puddles

    def trap3(self, height):
        l, r = 0, len(height) - 1
        res = 0
        minmum = min(height[l], height[r])
        while l <= r:
            if height[l] <= height[r]:
                if height[l] < minmum:
                    res += max(0, minmum - height[l])
                else:
                    minmum = min(height[l], height[r])
                l += 1
            else:
                if height[r] < minmum:
                    res += max(0, minmum - height[r])
                else:
                    minmum = min(height[l], height[r])
                r -= 1

        return res




solution = Solution()
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,0,3,2,5]
# height = [4,2,3]
# height = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
# height = [0,1,2,0,3,0,1,2,0,0,4,2,1,2,5,0,1,2,0,2]
# height = [9,6,8,8,5,6,3]
# height = [4,9,4,5,3,2]
print(f'Water Accumulated: {solution.trap3(height)}')