# Print all factors of a number
# O(n)
def factors(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=" ")

# O(sqrt(n))
import math
def factors2(n):
    last = int(math.sqrt(n)) + 1
    for i in range(1, last):
        if n % i == 0:
            if n // i == i:
                print(i, end= " ")
            else:
                print(i, n // i, end=" ")


n = 45
factors(n)
print()
factors2(n)