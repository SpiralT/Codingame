import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r_1 = int(input())
r_2 = int(input())

def sumdigits(num):
    sum = 0
    while num:
        sum += num%10
        num = num//10
    return sum



while r_1!=r_2:
    
    if r_1<r_2:
        r_1 += sumdigits(r_1)
    else:
        r_2 += sumdigits(r_2)
    
print(r_1)    
