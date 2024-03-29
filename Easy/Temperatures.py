import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse

if n == 0:
    clo = 0
else:
    clo = 10000
    
    
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    
    if abs(t) < abs(clo):
        clo = t
    elif abs(t) == abs (clo):
        if t == clo:
            clo = t
        else:
            clo = abs(t)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(clo)


#=========================================================
#Other 1:
input()
T=[int(s) for s in input().split()]
print(T and sorted(sorted(T,reverse=True),key=abs)[0] or 0)


#=========================================================
#Other 2:
input()  # skip
ln = input() or '0'

temps = [int(s) for s in ln.split()]

temps.sort(key = lambda x: (abs(x),-x))

#print(temps, file=sys.stderr)

print(temps[0])
