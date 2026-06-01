class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Search a value
    def search(self, target):
        temp = self.head

        while temp:
            if temp.data == target:
                return True
            temp = temp.next

        return False

    # Delete a node by value
    def delete(self, target):

        if self.head is None:
            return

        # If head contains target
        if self.head.data == target:
            self.head = self.head.next
            return

        prev = None
        curr = self.head

        while curr:
            if curr.data == target:
                prev.next = curr.next
                return

            prev = curr
            curr = curr.next

    # Count nodes
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

    # Reverse linked list
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev

            prev = current
            current = next_node

        self.head = prev

    # Find middle node
    def find_middle(self):

        if self.head is None:
            return None

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    # Display linked list
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# -------------------------
# Driver Code
# -------------------------

ll = LinkedList()

# Insert at end
ll.insert(20)
ll.insert(30)
ll.insert(40)

# Insert at beginning
ll.insert_at_beginning(10)

print("Linked List:")
ll.display()

print("\nSearch 30:", ll.search(30))
print("Search 50:", ll.search(50))

print("\nTotal Nodes:", ll.count_nodes())

print("Middle Node:", ll.find_middle())

ll.delete(30)

print("\nAfter deleting 30:")
ll.display()

ll.reverse()

print("\nAfter reversing:")
ll.display()