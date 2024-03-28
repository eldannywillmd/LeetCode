class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        if self.head is None:
            return
        else:
            node = self.head
            while node is not None:
                print(node.data, end=' ')
                node = node.next

class Solution:
    def reverseBetween(self, list, left, right):
        count = 1
        cur = list.head
        while count <= left:
            count += 1
            cur = cur.next
        while count <= right:
            count += 1
            cur.next = cur

            print(cur.data, end=' ')

        return list

solution = Solution()
head = [1,2,3,4,5]
list = LinkedList()
for i in head:
    list.append(i)
left = 2
right = 4
print(solution.reverseBetween(list, left, right).print_list)