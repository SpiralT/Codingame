import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

expression = input()

opens = tuple("{[(")
close = tuple("}])")
match = dict(zip(opens,close))
check = []


for i in expression:
    #print("i is",i)
    if i in opens:
        check.append(match[i])
        #print("check append",i,check)
    elif i in close:
        if not check or i!= check.pop():
            print("false")
            quit()

if not check:
    print("true")
else:
    print("false")
        
        
    
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
