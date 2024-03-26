n = 5
for i in range(n):

    for j in range(i, n):
        print(' ', end=' ')
    for j in range(1,i):
        print("$", end=' ')
    for j in range(i+1):
        print("$", end=' ')
        
    print()

  
#  the diamond pattern
n = 5  

for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))

for i in range(n - 2, -1, -1):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))
