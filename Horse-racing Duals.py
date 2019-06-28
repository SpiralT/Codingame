import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
horse = []


for i in range(n):
    pi = int(input())
    horse.append(pi)

horse.sort()

for i in range(0,len(horse)-1):
    diff = int(abs(horse[i]-horse[i+1]))
    
    if i == 0:
        min_diff = diff
    if min_diff > diff:
        min_diff = diff
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(min_diff)


#========================================================
#Other 1:
pi = sorted([int(input()) for i in range(int(input()))])
print(min([j-i for i,j in zip(pi[:-1],pi[1:])]))


#========================================================
#Other 2:
l = sorted([int(input()) for _ in range(int(input()))])
print(min((l[i+1] - l[i] for i in range(len(l) - 1))))
