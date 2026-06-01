nums = [5, 2, 9, 1]

nums.sort()

print(nums)
nums.sort(reverse=True)
print(nums)
#sort by key
students = [
    ("Rahul", 90),
    ("Ananya", 95),
    ("Amit", 80)
]

students.sort(key=lambda x: x[1])

print(students)