#! /usr/bin/env python3

data = open("day6_input.txt", "r")
lines = data.readlines()
ON, OFF, TOGGLE = range(3)

bitmap = [[False for i in range(1000)] for j in range(1000)]
bitmap2 = [[0 for i in range(1000)] for j in range(1000)]

def edit(tl_x, tl_y, br_x, br_y, t):
    for col in range(tl_x, br_x + 1):
        for row in range(tl_y, br_y + 1):
            if t == ON:
                bitmap[row][col] = True
            elif t == OFF:
                bitmap[row][col] = False
            elif t == TOGGLE:
                bitmap[row][col] = not bitmap[row][col]
 
def edit2(tl_x, tl_y, br_x, br_y, t):
    for col in range(tl_x, br_x + 1):
        for row in range(tl_y, br_y + 1):
            if t == ON:
                bitmap2[row][col] += 1
            elif t == OFF:
                if bitmap2[row][col] > 0:
                    bitmap2[row][col] -= 1
            elif t == TOGGLE:
                bitmap2[row][col] += 2          

                
for line in lines:
    s = line.split(" ")
    if s[0] == "toggle":
        tl = [int(x) for x in s[1].split(",")]
        br = [int(x) for x in s[3].split(",")]
        edit(tl[0], tl[1], br[0], br[1], TOGGLE)
        edit2(tl[0], tl[1], br[0], br[1], TOGGLE)
    elif s[1] == "on":
        tl = [int(x) for x in s[2].split(",")]
        br = [int(x) for x in s[4].split(",")]
        edit(tl[0], tl[1], br[0], br[1], ON)
        edit2(tl[0], tl[1], br[0], br[1], ON)
    elif s[1] == "off":
        tl = [int(x) for x in s[2].split(",")]
        br = [int(x) for x in s[4].split(",")]
        edit(tl[0], tl[1], br[0], br[1], OFF)
        edit2(tl[0], tl[1], br[0], br[1], OFF)
        
count = 0
count2 = 0
for r in range(1000):
    for c in range(1000):
        if bitmap[r][c] == True:
            count += 1
        count2 += bitmap2[r][c]
            
print(count)
print(count2)