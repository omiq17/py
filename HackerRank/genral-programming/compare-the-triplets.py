### Global, Local and nonlocal Variables
# The way Python uses global and local variables is maverick. 
# While in many or most other programming languages variables are treated as 
# global if not otherwise declared, Python deals with variables the other way 
# around. They are local, if not otherwise declared. The driving reason behind this 
# approach is that global variables are generally bad practice and should be avoided.
# In most cases where you are tempted to use a global variable, it is better to utilize 
# a parameter for getting a value into a function or return a value to get it out. 
# Like in many other program structures, Python also imposes good programming 
# habit by design.

def compare(a, b):
    global  alice, bob
    if a == b :
        return 
    elif a > b:
        alice = alice + 1
    else :
        bob = bob + 1

def main():
    a0, a1, a2 = map(int, input().split())
    b0, b1, b2 = map(int, input().split())

    global alice, bob
    compare(a0, b0)
    compare(a1, b1)
    compare(a2, b2)

    print(alice , bob)
    

alice = 0; bob = 0
main()


### editorial

# a_triplet = map(int, input().split())
# b_triplet = map(int, input().split())
# alice_points = 0
# bob_points = 0
# for a_val, b_val in zip(a_triplet, b_triplet):
#     if a_val < b_val:
#         bob_points += 1
#     elif a_val > b_val:
#         alice_points += 1
# print(alice_points, bob_points)