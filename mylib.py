# print("welcome everyone! I am so glad to meet you all!")
# x=5000
# y=10000
# # print(x-y)
# # print(x*y)
# # print(x/y)
# r = 1.5
# pi=3.14
# print(pi * r ** 2)
# print(4/3 * pi * r **3)
# # temp = 28
# # print(temp * 9/5 +32)
# first_name = 'Jonny'
# last_name = ' zhu'
# print("*" * 100)
# print("Hello", first_name,  last_name, 279)
# def greet(name):
#     print("Hello" ,name)
# greet("Jon")


# def foo():
#     print()


# def celciusToFarenheit(celcius):
#     f = celcius * 9/5 +32
#     return f

# foo()
# foo()
# foo()
# print("The temperature is: ",celciusToFarenheit(0))

# def farenheitToCelcius(farenheit):


# triple quotes for long, more than 1 line
# items = { "mango": 1, "lemon": 3, "watermelon": 10, "orange": 2}
# myString = """ hey
# 1
# 3
# 7

# hello """
# print(myString)

myString = "Hello, World!"

# def convertString(str):
#     res = ''
#     for i in range(len(str)):
#         if i % 2 == 0:
#             res += str[i].upper()
#         else:
#             res += str[i].lower()
#     return res




#myList = [47,35,4,53,65,7,9,2534,77,3,6,8,65,3,24,5,7,8787]
# print("This is my lib")

def getSmallest(myList):
    smallestValue = myList[0]
    for num in myList:
        if num < smallestValue:
            smallestValue = num
    return smallestValue


def getNewList(num, myList,smallestValue):
    newList = []
    for num in myList:
        if num > smallestValue:
            newList.append(num)
    return newList

def sort(myList, asce=True):
    orderedList = []
    for i in range(len(myList)):
        if len(myList) == 0:
            break
        smallestValue = getSmallest(myList)
        newList = getNewList(smallestValue, myList,smallestValue)
        orderedList.append(smallestValue)
        myList = newList

    return  orderedList if asce else reverseList(orderedList)
    
def reverseList(myList):
    if myList is None:
        return myList
    l = []
    for i in range(len(myList)):
        l.append(myList[len(myList) - 1 - i])
    return l



def main():
    list = [20,4,5,28,41,7,8,24,14,5,52,1,63,634,4.5]
    print(reverseList(list))    

# print("__name__ is: ", __name__)

if __name__ == "__main__":
    main()