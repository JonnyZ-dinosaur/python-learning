class Person:
#Universal property of the class, all objects created using this 
#class have this property 
    city = "New York"

    @classmethod
    def printClassCity(cls):
      print("I am from", cls.city)

#self is the independent object that is being created
    def __init__(self, name, age):
      self.name = name 
      self.age = age 

    def getName(self):
       return self.name 
   

    def greet(self):
     print("Hello my name is", self.name)

    def fiveYears(self):
      print(self.age + 5)

    def aboutMe(self):
        print("My name is", self.name)
        print("My age is ", self.age)
       

#    def printCity(self):
#        print("Hello I am from", Person.city)

class Student(Person):
    def __init__(self,name,age,year):
       super().__init__(name,age)
       self.year = year

    def aboutMe(self):
       print("My name is", self.name)
       print("My age is ", self.age)
       print("My graduation year is ", self.year)

myString = "Hello"
print(myString.lower())


# Create an object
person = Person("Jonny", 16)
print(person.name) 
person.greet()
person.fiveYears()
person.aboutMe()
person.printCity()
student = Student("Jonny",16,2028)
student.aboutMe()

person.printCity()


#the Universal property can also be accessed by calling the Person class instead of only 
print(Person.city)
print(person2.city)
Person.city = "Seattle"

print(person.city)
print(person2.city)

#this creates an independent property for the person2 ONLY 
#branches off technically its like writing a new parameter in the __init__ function 

person2.city = "Washington"
#that makes it so that when the universal property is changed, the independent one
#didnt change, therefore person2 city is still Washington 

Person.city = "Seattle"
print(person.city)
print(person2.city)
print(Person.city)

Person.printClassCity()


# Encapsulation 

