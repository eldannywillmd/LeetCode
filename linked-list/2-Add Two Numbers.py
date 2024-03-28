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

def addTwoNumbers(nodel1, nodel2):

    l3 = LinkedList()
    rest = 0

    while nodel1 is not None or nodel2 is not None:
        if nodel1 is not None and nodel2 is not None:
            if nodel1.data + nodel2.data + rest < 10:
                l3.append(nodel1.data + nodel2.data + rest)
                rest = 0
            else:
                l3.append((nodel1.data + nodel2.data + rest) % 10)
                rest = 1
            nodel1 = nodel1.next
            nodel2 = nodel2.next
        elif nodel1 is not None:
            if nodel1.data + rest < 10:
                l3.append(nodel1.data + rest)
                rest = 0
            else:
                l3.append((nodel1.data + rest) % 10)
                rest = 1
            nodel1 = nodel1.next
        elif nodel2 is not None:
            if nodel2.data + rest < 10:
                l3.append(nodel2.data + rest)
                rest = 0
            else:
                l3.append((nodel2.data + rest) % 10)
                rest = 1
            nodel2 = nodel2.next

    if rest == 1:
        l3.append(rest)

    return l3

l1 = LinkedList()
l2 = LinkedList()

nodes_l1 = [2,4,3]
nodes_l2 = [5,6,4]
for i in nodes_l1:
    l1.append(i)
for i in nodes_l2:
    l2.append(i)


l3 = addTwoNumbers(l1.head, l2.head)
l3.print_list()
