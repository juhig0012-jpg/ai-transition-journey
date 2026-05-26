a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
intersection = list(set(a) & set(b))
print("Intersection of the two arrays is:", intersection)   
hashmap = {}
for num in a:
    hashmap[num] = hashmap.get(num, 0) + 1          
intersection = []
for num in b:
    if hashmap.get(num, 0) > 0:
        intersection.append(num)
        hashmap[num] -= 1
print("Intersection of the two arrays is:", intersection)