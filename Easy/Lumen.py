import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
l = int(input())


# [[0]*5]*5 makes a list with five references to the same list:
sqr = [[0]*n for i in range (n)] 


for i in range(n):
    line = input().split()
    for x in range(0,len(line)):
        if line[x] == "C":
            row_start = max(i-l+1,0)
            row_end = min(i+l-1,n-1)
            col_start = max(x-l+1,0)
            col_end = min(x+l-1,n-1)
            #print("c location:",i,x,n," area:",row_start,row_end,col_start,col_end)
            for y in range(row_start,row_end+1):
                for m in range (col_start,col_end+1):
                    sqr[y][m] = 1
            #print(sqr)


#print(sqr) 

result = 0

for x in sqr:
    result += x.count(0)
    
      
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
print(result)
