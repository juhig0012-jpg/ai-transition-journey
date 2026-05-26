nums = [1, 2, 3, 4, 5, 1, 2, 3]
hashmap = {}
for num in nums:
    hashmap[num] = hashmap.get(num, 0) + 1
grouped_numbers = {}
for num, count in hashmap.items():
    if count not in grouped_numbers:
        grouped_numbers[count] = []
    grouped_numbers[count].append(num)  
print("Numbers grouped by their frequency:", grouped_numbers)