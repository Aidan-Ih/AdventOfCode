#! /usr/bin/env python3

data = open("day3_input1.txt", "r").readline()

cur_row = 0
cur_col = 0

#a dictionary of with row numbers as indicies, containing a list of the columns
#in that row which have presents
rows = {}
rows[0] = [0]
part1_ans = 1

combined_rows = {}
combined_rows[0] = [0]
santa_row = 0
santa_col = 0
robot_row = 0
robot_col = 0
santas_turn = False
part2_ans = 1


for direction in data:
    santas_turn = not santas_turn
    
    if(direction == ">"):
        cur_col += 1
        if(santas_turn):
            santa_col += 1
        else:
            robot_col += 1
    elif(direction == "<"):
        cur_col -= 1
        if(santas_turn):
            santa_col -= 1
        else:
            robot_col -= 1
    elif(direction == "^"):
        cur_row += 1
        if(santas_turn):
            santa_row += 1
        else:
            robot_row += 1
    elif(direction == "v"):
        cur_row -= 1
        if(santas_turn):
            santa_row -= 1
        else:
            robot_row -= 1
        
    if cur_row in rows.keys():
        if cur_col in rows[cur_row]:
            pass
        else:
            rows[cur_row].append(cur_col)
            part1_ans += 1
    else:
        rows[cur_row] = [cur_col]
        part1_ans += 1
        
    if santas_turn:
        if santa_row in combined_rows.keys():
            if santa_col in combined_rows[santa_row]:
                pass
            else:
                combined_rows[santa_row].append(santa_col)
                part2_ans += 1
        else:
            combined_rows[santa_row] = [santa_col]
            part2_ans += 1
            
    else:
        if robot_row in combined_rows.keys():
            if robot_col in combined_rows[robot_row]:
                pass
            else:
                combined_rows[robot_row].append(robot_col)
                part2_ans += 1
        else:
            combined_rows[robot_row] = [robot_col]
            part2_ans += 1
        
print("part 1:", str(part1_ans))
print("part 2:", str(part2_ans))
    