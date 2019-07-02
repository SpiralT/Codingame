import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n, m, c = [int(i) for i in input().split()]

devi = dict(zip(range(1,n+1),input().split()))
status = dict(zip(range(1,n+1),[0]*n))

cons = 0
maxcon = 0

for i in input().split():
    if status[int(i)] == 0:
        status[int(i)] = 1
        cons += int(devi[int(i)])
        if maxcon < cons:
            maxcon = cons
    else:
        status[int(i)] = 0
        cons -= int(devi[int(i)])
    
    if cons > c:
       print("Fuse was blown.")
       quit()





# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


print("Fuse was not blown.")
print(f"Maximal consumed current was {maxcon} A.")
