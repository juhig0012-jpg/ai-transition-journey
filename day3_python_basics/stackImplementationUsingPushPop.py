class Stack:
    def __init__(self):
        self.items = []

    # Push element onto stack
    def push(self, item):
        self.items.append(item)

    # Remove and return top element
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    # Return top element without removing
    def top(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    # Check if stack is empty
    def is_empty(self):
        return len(self.items) == 0


# Example usage
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.top())   # 30
print("Popped:", stack.pop())        # 30
print("Top element:", stack.top())   # 20