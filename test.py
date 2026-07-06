# class Person:
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age

#     def printName(self):
#         print(self.name)

# person = Person("Bob", 28)
# person2 = Person("Amy", 32)

# person.printName()
# print(person.age)

# person2.printName()
# print(person2.age)


# dictionary = {"hey": 1,
#               "hello": 2,
#               "whats up": 3}

# print(dictionary.values())
# print(dictionary.get("hello"))

list = [1,2,4,6,6,1,4,5,2,5,7,3]

rooms = {1 :0, 2: 0, 3: 0 ,4 :0,
        5:0 ,6: 0,7: 0, 8: 0,
        9:0,10:0,"more":0}

for item in list:
    rooms[item] += 1

print(rooms)


