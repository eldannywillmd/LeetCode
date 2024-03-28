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

    def create_cycle(self, pos):
        if pos == -1:
            return  # No cycle requested
        current_node = self.head
        cycle_node = None
        index = 0
        while current_node.next:
            if index == pos:
                cycle_node = current_node
            current_node = current_node.next
            index += 1
        current_node.next = cycle_node  # Create cycle

    def hasCycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            elif fast == None:
                return False


############################
linked_list = LinkedList()
# Example usage:
# Create a linked list and append some elements
head = [3,2,0,-4]
for i in head:
    linked_list.append(i)

# Create a cycle in the linked list (connecting the last node to the second node)
linked_list.create_cycle(0)

print(linked_list.hasCycle())


