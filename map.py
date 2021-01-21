
import sys

n = 3

for i in range (n):
    for j in range (n - 1):
        print("   |", end = '')
    print("")
    if i < (n-1):
        for j in range (n):
            print("___", end = '')
            if j < (n-1):
                print("|", end = '')
        print("")
for j in range (n - 1):
        print("   |", end='')
print("")
