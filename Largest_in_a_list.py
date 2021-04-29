myList = [17, 3, 11, 5, 1, 19, 7, 15, 103]
largest = myList[0]

for i in range(1, len(myList)):
    if myList[i] > largest:
        largest = myList[i]

print(largest)