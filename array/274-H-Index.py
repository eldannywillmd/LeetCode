import math
class Solution:
    def hIndex(self, citations):
        halfway = [math.ceil(len(citations) / 2)]
        count = 0
        visited = set()
        hindex = []

        if halfway[0] == 0:
            if citations[0] == 0:
                return 0
            else:
                return 1

        while halfway[-1] != 0:

            for i in range(len(citations)):

                if citations[i] >= halfway[-1] and count < halfway[-1]:
                    count += 1
                if count == halfway[-1]:
                    hindex.append(count)
                    break

            if count >= halfway[-1] and halfway[-1] not in visited:
                count = 0
                visited.add(halfway[-1])
                if len(halfway) > 1 and halfway[-2] > halfway[-1]:
                    new_halfway = math.ceil((halfway[-1] + halfway[-2]) / 2)
                else:
                    new_halfway = halfway[-1] + math.ceil(halfway[-1] / 2)
                while new_halfway in visited and new_halfway != halfway[-1] + 1:
                    new_halfway -= 1
                halfway.append(new_halfway)

            elif count < halfway[-1] and halfway[-1] not in visited:
                count = 0
                visited.add(halfway[-1])
                if len(halfway) > 1 and halfway[-2] < halfway[-1]:
                    new_halfway = (halfway[-1] + halfway[-2]) // 2
                else:
                    new_halfway = halfway[-1] - math.ceil(halfway[-1] / 2)
                while new_halfway in visited and new_halfway != halfway[-1] - 1:
                    new_halfway += 1
                halfway.append(new_halfway)
            else:
                break

        if len(hindex) != 0:
            return max(hindex)
        else:
            return 0

solution = Solution()
citations = [1,1,1,1]
print(solution.hIndex(citations))