def multiply(a,b):
    return a*b
print(multiply(3,4))

#def wishes():
#    print("My wishes")
#    return "Happy Birthday"
#wishes()

def wishes():
    print("My wishes")
    return "Happy Birthday"
print(wishes())

def hiEverybody(myList):
    for name in myList:
        print("Hi, ", name)
hiEverybody(["Adam", "John", "Lucy"])

def createList(n):
    myList = []
    for i in range(n):
        myList.append(i)
    return myList
print(createList(25))