#! /usr/bin/env python3

data = open("day5_input.txt", "r")
lines = data.readlines()

# Nice if:
# at least 3 vowels
# at least one letter that appears twice in a row
# does not contain ab, cd, pq, xy

def is_string_nice_1(s):
    last = None
    vowels = 0
    twice_in_a_row = False
    for c in s:
        if c in "aeiou":
            vowels += 1
        if c == last:
            twice_in_a_row = True
        if last == "a" and c == "b":
            return False
        if last == "c" and c == "d":
            return False
        if last == "p" and c == "q":
            return False
        if last == "x" and c == "y":          
            return False 
        last = c
    
    return vowels >= 3 and twice_in_a_row

def is_string_nice_2(s):
    last = "."
    before_last = "."
    same_one_between = False
    double_repeat = False
    pairs = []
    last_pair = ".."
    
    for c in s:
        if before_last == c:
            same_one_between = True
        
        this_pair = last + c
        if this_pair in pairs:
            double_repeat = True
        
        pairs.append(last_pair)
        last_pair = this_pair
        before_last = last
        last = c
    return same_one_between and double_repeat
        
    

nice_count = 0
nice_count_2 = 0
for word in lines:
    if is_string_nice_1(word):
        nice_count += 1
    if is_string_nice_2(word):
        nice_count_2 += 1
        
print(nice_count)
print(nice_count_2)