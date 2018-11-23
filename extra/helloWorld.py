# numbers in python
x = int(raw_input("Enter x: "))
y = int(raw_input("Enter y: "))
sum = x+y
print(sum)

#strings in python
# string = "a string in python"
# me = "i am a string"
# if me == string:
#     print("strings equal")
# else:
#     print("strings not equal")
# print(string)
# print(string[3])
# print(me[2:7])
#
# #myLists in Python
# myList = ["Dhaka", "Chittagong", "Mymensingh", "Rajshahi", "Khulna"]
# print myList
# myList.append("Alabama")
# print myList
# myList.remove("Alabama")
# print myList
# myList.sort()
# print myList
# print("")
#
# #myTuple = A data structure which is used to store a group of data
# # A myTuple cannot be modified
# myTuple = ("Alaba", 33, "Rakib", 33);
# print(myTuple[1])
# name,age,country,versity = ("Fedora", 28, "Unknown", "Red Hat")
# print(versity)
# myTuple = myTuple + ("Jon", 3)
# print(myTuple)
# tupleTomyList = list(myTuple)
# print(tupleTomyList)
#
# newTuple = ("Ubuntu", "Mint", "Manjaro")
# tupleToString = " ".join(newTuple)
# print(tupleToString)
# newTuple = tuple(sorted(newTuple))
# print(newTuple)
# print(" ")
#
# #Dictionary = An unordered set of key value pairs
# python = {}
# python['about'] = "A programming language"
# python['version'] = 2
# python[1] = "what the heck?"
# print(python)
# print python['about']
# print python['version']
# print python[1]
#
# del python[1]
# print(python)
# python[1] = "I am back"
# print(python)
# print("")
#
# #datatype casting
# x = 3
# y = 2.15315315313532
# print "We have defined two numbers,"
# print "x = " + str(x)
# print "y = " + str(y)
# print ""
#
# guess = 24
# if guess > 15 and guess < 25:
#     print "The guesss is right"
# else:
#     print "The guess is wrong"
# print ""
#
# #printing location
# x = 3
# print hex(id(x))

# #function work
# def highFive():
#     return 5
# def total(x):
#     return highFive() + x
# print total(7)
#
# #loops in python
# items = ["Abba", "Amma", "Cacha", "Khala"]
# for item in items:
#     print items
#
# for i in range(1, 3):
#     for j in range(1, 3):
#         print("(" + str(i) + "," + str(j) + ")")
#
# #random function in python
# from random import*
# print random()
# print randint(1, 15)
# print uniform(1, 15)
# shuffle(items)
# print items
# x = sample(items, 1)
# print x[0]
# y = sample(items, 3)
# print y

#***Classes & Objects in Python
# class TeaMachine:
#     teaName = ""
#     pati = 0
#     pani = 0
#     __ammount = 0 #private variable (Encapsulation)

#     def __init__(self, tname, pati, pani):
#         self.teaName = tname
#         self.pati = pati
#         self.pani = pani
#         self.__updateAmmount(25)

#     def increasePati(self):
#         self.pati += 1
#     def increasePani(self):
#         self.pani += 50
#     def decreasePati(self):
#         self.pati -= 1
#     def decreasePani(self):
#         self.pani -= 50

#     def printState(self):
#         print "Tea Name : " + self.teaName
#         print "Patir Poriman : " + str(self.pati) + " cha chamos"
#         print "Panir Poriman : " + str(self.pani) + " mL"
#         print str(self.__ammount)

#     def __updateAmmount(self, amm):
#         self.__ammount = amm

# lalCha = TeaMachine("Lal Cha", 1, 150)
# dudCha = TeaMachine("Dud Cha", 2, 150)
# lalCha.decreasePani()
# dudCha.increasePati()
# lalCha.printState()
# dudCha.printState()
# lalCha.__ammount = 55 #won't work as it is private variable
# lalCha.printState()

# #Method Overloading
# class PrintName:
#     def sayHello(self, name="nai"):
#         if name is not "nai":
#             print "Hello "+ name
#         else:
#             print "No Name Found!"
# #Creating Instances
# obj = PrintName()
# #Calling Method
# obj.sayHello()
# #Calling Method With a Parameter
# obj.sayHello("Raqib")
