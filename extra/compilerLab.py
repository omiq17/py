# ::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::
# ::: Predictive Parsing
#
print("Predictive Persing:")
parseTable = {  'i':  {'E':'TD', 'T':'FS', 'F':'i'},
                '(':  {'E':'TD', 'T':'FS', 'F':'(E)'},
                '+':  {'D':'+TD', 'S':''},
                ')':  {'D':'', 'S':''},
                '$':  {'D':'', 'S':''},
                '*':  {'S':'*FS'}
                }

tree = "i+i*i$"
stack = "E$"


for i in range(10000):
    if(stack[0] == tree[0]):
        stack = stack[1:]
        tree = tree[1:]
        if(stack == "" and tree == ""):
            print("Given grammar is Accepted")
            break

    if tree[0] in parseTable.keys():
        if stack[0] in parseTable[tree[0]].keys():
            stack = parseTable[tree[0]][stack[0]] + stack[1:]
            # print(stack)
        else:
            print("Given grammar is Rejected")
            break
    else:
        print("Given grammar is Rejected")
        break


# ::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::
# ::: DFA code
#
# def checkState(current, i):
#     if(i!="a" and i!="b" and i!="c"):
#         return 5
#     if(current == 0):
#         if(i == "a"):
#             return 0
#         elif(i == "b"):
#             return 1
#         elif(i == "c"):
#             return 2
#     elif(current == 1):
#         if(i == "a"):
#             return 2
#         elif(i == "b"):
#             return 0
#         elif(i == "c"):
#             return 1
#     elif(current == 2):
#         if(i == "a"):
#             return 0
#         elif(i == "b"):
#             return 3
#         elif(i == "c"):
#             return 1
#     elif(current == 3):
#         if(i == "a"):
#             return 0
#         elif(i == "b"):
#             return 0
#         elif(i == "c"):
#             return 1
#
# while True:
#     currentState = 0
#     sentence = input()
#     if(sentence == "end"):
#         break
#
#     for i in sentence:
#         currentState = checkState(currentState, i)
#         if(currentState == 5):
#             break
#
#     if(currentState == 3):
#         print("Accepted")
#     else:
#         print("Rejected")


# :::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::
# :::Regular Expression for finding Keywords in C Source Code
print("\n")
print("Symbol Table:")
import re

def checkRegex(i):
    regex1 = r"\D\d\D"
    regex2 = r"\d\d+"
    regex3 = r"int|if|else if|else|while|for|return"
    regex4 = r"<=|>=|<|>|!=|!"
    regex5 = r"\+|\/|\%|\-|\*|\\"
    regex6 = r"\".+\""
    regex7 = r"#.+<.+>"
    regex8 = r"[a-z]+[(].*[)]"
    regex9 = r"[A-Za-z]+[A-Za-z0-9]*\s*=|[A-Za-z]+[A-Za-z0-9],"

    r = ""

    match = re.findall(regex1, i)
    print("Digits: ")
    for m in match:
        print ( m[1] , end="\t")
    print("\n")

    match = re.findall(regex2, i)
    print("Numbers: ")
    for m in match:
        print (m, end="\t")
    print("\n")

    match = re.findall(regex3, i)
    print("Keywords: ")
    for m in match:
        print (m, end="\t")
    print("\n")

    match = re.findall(regex4, i)
    print("Comparison Operators: ")
    for m in match:
        print (m, end="\t")
    print("\n")

    match = re.findall(regex5, i)
    print("Mathematical Operators: ")
    for m in match:
        print (m, end="\t")
    print("\n")

    match = re.findall(regex6, i)
    print("Strings: ")
    for m in match:
        print (m, end="\t")
    print("\n")

    match = re.findall(regex7, i)
    print("Headers: ")
    for m in match:
        print (m, end="\t")
    print("\n")

    match = re.findall(regex8, i)
    print("Functions: ")
    for m in match:
        print (m, end="\t")
    print("\n")

    match = re.findall(regex9, i)
    symbol = []
    print("Id's: ")
    for m in match:
        print (m[:-1], end="\t")
        symbol.append(m[:-1].strip())
    print("\n")
    print("Symbol Table:")
    symbol = list(set(symbol))
    i = 1
    for s in symbol:
        print(i,"     ",s)
        i=i+1
        print("\n")


i = """
        #include<stdio.h>

        int main() {
           int num, rem, rev = 0;
           int a9b4 = 6;

           printf("Enter any no to be reversed : ");
           scanf("%d", &num);

           while (num >= 1) {
              rem = num % 10;
              rev = rev * 10 + rem;
              num = num / 10;
           }

           printf("\nReversed Number : %d", rev);
           return (0);
        }
    """

result = checkRegex(i)
