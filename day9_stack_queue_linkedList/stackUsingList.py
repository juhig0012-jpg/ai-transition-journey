stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

top = stack.pop()

print(top)
print(stack)

#peek top element without removing it
top = stack[-1]
print(top)

#check if stack is empty
if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")

#push more elements
stack.append(40)
stack.append(50)
print(stack)

#pop few elements
stack.pop()
stack.pop()
print(stack)

#print size of stack
print(f"Size of stack: {len(stack)}")