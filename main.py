name = "Rahul"
age = 25
salary = 50000

print(name)
print(age)
print(salary)
name = input("Enter your name: ")
print("Hello", name)
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
for i in range(5):
    print(i)
count = 1

while count <= 5:
    print(count)
    count += 1

def add(a, b):
    return a + b

result = add(5, 10)
print(result)