list = ["apple", "orange", "cherry"]
print(list)
list.insert(0,"banana")
print(list)
list.insert(len(list), "kiwi")
print(list)
list2 = ["dog", "cat", "bird"]
# list.extend(list2)
# print(list)

# for x in list2:
#     list.append(x)

# print(list)
# list.remove("apple")
# print(list)

# list.pop()
# print(list)

del list[-2]
print(list)

numbers = [1, 2,52, 53,6,14,63]
numbers = [15+x for x in numbers if x > 20 ]

print(numbers)

fruits = []

# for x in range(100):
#     fruits.append("apple")
# print(fruits)

# fruits2 = [f"apple{x}" for x in range(100)]
# print(fruits2)

# def deleteEven(list):
#     newList = []
#     for x in list:
#         if x % 2 == 1:
#             newList.append(x)
#     return newList 

# print(deleteEven(numbers))

numbers.sort(reverse = True)

print(numbers)