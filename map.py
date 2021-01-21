
import sys

n = 3
x = 'X'

for i in range(n):
    # first line of row
    for j in range(n):
        print(" "*3, end='')
        if j < (n - 1):
            print("|", end='')
    print("")

    # second line of row-- with char
    for j in range(n):
        print(f" {x} ", end='')
        if j < (n - 1):
            print("|", end='')
    print("")

    # 3rd line/ divider
    if i < (n - 1):
        for j in range(n):
            print("___", end='')
            if j < (n - 1):
                print("|", end='')
        print("")
for j in range(n - 1):
        print("   |", end='')
print("")
