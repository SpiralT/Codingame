import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

x_start = 0
y_start = 0
x_end = w - 1
y_end = h - 1

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    
    if "U" in bomb_dir:
        y_end = y0 - 1
    elif "D" in bomb_dir:
        y_start = y0 + 1
    
    if "L" in bomb_dir:
        x_end = x0 - 1
    elif "R" in bomb_dir:
        x_start = x0 + 1
    
    #print(x_start,x_end,y_start,y_end)
    
    x0 = x_start + math.ceil((x_end - x_start)/2)
    y0 = y_start + math.ceil((y_end - y_start)/2)
    
    #print(x0,y0)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # the location of the next window Batman should jump to.
    print(int(x0),int(y0))
