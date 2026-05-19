listofnum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
minNum = listofnum[0]
for i in listofnum:
    if i < minNum:
        minNum = i
print(minNum)