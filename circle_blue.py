import os
import sys

for num in range(1, 101):
    if num % 5 == 0 and num % 7 == 0:
        print("Circle Blue")
    elif num % 7 == 0:
        print("Blue")
    elif num % 5 == 0:
        print("Circle")
    else:
        print(num)
