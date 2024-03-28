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
    def mergeTwoLists(self, list1, list2):
        l3 = LinkedList()
        while list1 or list2:
            if list1 and list2:
                if list1.data > list2.data:
                    l3.append(list2.data)
                    list2 = list2.next
                else:
                    l3.append(list1.data)
                    list1 = list1.next
            else:
                if list1:
                    l3.append(list1.data)
                    list1 = list1.next
                else:
                    l3.append(list2.data)
                    list2 = list2.next
        return l3.head

solution = Solution()
l1 = LinkedList()
l2 = LinkedList()

nodes_l1 = []
nodes_l2 = [0]
for i in nodes_l1:
    l1.append(i)
for i in nodes_l2:
    l2.append(i)

