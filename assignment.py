def func():
    objectList = ['back', 'end', 'front', 'cover', 'cool', 'hot', 'free']

    combinatStr = []

    user = int(input("Do you want to add more items into the Database ? (Type 1 for Yes and 0 for No)"))

    if user==1:
        num = int(input("Enter the number of items you want to input ... "))
        for p in range(0, num):
            items = str(input('Enter the item number ' + str(p+1)))
            objectList.append(items)

    lengthOf = len(objectList)

    for j in range(0, lengthOf):
        for i in range(0, lengthOf):
            combinatStr.append(str(objectList[j]) + str(objectList[i]))


    choice = str(input('Enter your string ... '))

    counterT = 0
    counterF = 0

    for i in range(0, len(combinatStr)):    
        if choice == combinatStr[i]:
            counterT = counterT + 1
            continue
        else:
            counterF = counterF + 1
            continue

    if counterF == len(combinatStr):
        print(False)
    else:
        print(True)

var = func()



