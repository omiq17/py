# -*- coding: utf-8 -*-

# print("আমি ভাত খাই")
print("I %s eat rice." % "always")
mangoes = 11
print("I have %d mangoes" % mangoes)
apples = 15
print("I have %d mangoes and %d apples" % (mangoes, apples))
print("I have total %d fruits" %(mangoes + apples))
# %r prints no matter what the format is
print("I have total %r fruits" %(mangoes + apples))

ques = "Do you eat mango? %r"
ans = True
print (ques % ans)
ques = "Do you eat mango?"
ans = "\nYes"
print(ques + ans)

print("""
        what is that
    """)

ques = "Do you eat mango? %r"
ans = "\nYes"
print(ques % ans)

print("\t|\r")
print("\ahello\\\n")

print("what are you eating?")
eating = input()
print(eating)
