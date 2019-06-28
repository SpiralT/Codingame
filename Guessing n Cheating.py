import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = int(input())
start, end = 1, 100

for i in range(r):
    line = input().split()
    #print("line is:",line)
    if line[2] == "high":
        end = min(end,int(line[0])-1)
        #print("round",i,start,end)
    elif line[2] == "low":
        start = max(start,int(line[0])+1)
        #print("round",i,start,end)


    if end < start or (line[2]=="on" and not start <= int(line[0]) <= end):
        print("Alice cheated in round", i+1)
        quit()
    
print("No evidence of cheating")