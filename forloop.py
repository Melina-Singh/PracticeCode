# pattern solving
# 1. size (How many rows you want in the pattern)
# every loop is made from right and left triangle pattern

n = 5                     #square pattern
# print("*"*  n)
for i in range(n): #rows
    for i in range(n):  #columns
        print("$", end ='  ')
    print()

print("\nThe next pattern is decreasing triangle pattern\n")


n = 5
for i in range(n):
    for j in range(i,n):
        print("$", end='  ')
    print()

print("\nThis is now the increasing triangle pattern\n")
n = 5
for i in range(n):
    for j in range(i+1):
        print("$", end='  ')
    print()


# Right sided triangle


n = int(input("Enter the number of Rows: "))
for i in range(n):
    for j in range(i, n):
        print(' ', end=' ')
    for j in range(i + 1):
        print("$", end=' ')
    print()



