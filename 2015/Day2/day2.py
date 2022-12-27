#! /usr/bin/env python3

data = open("input1.txt", "r")
lines = data.readlines()

part1_ans = 0
part2_ans = 0

def calc_wrapping_paper(dimensions):
    out = 0
    areas = [dimensions[0] * dimensions[1], dimensions[0] * dimensions[2], dimensions[1] * dimensions[2]]
    for a in areas:
        out += 2 * a
    out += min(areas)

    return out

def calc_ribbon(dimensions):
    out = 0
    volume = dimensions[0] * dimensions[1] * dimensions[2]
    perimiters = [dimensions[0] + dimensions[1], dimensions[0] + dimensions[2], dimensions[1] + dimensions[2]]
    smallest = 2 * min(perimiters)
    out += smallest + volume
    return out
    
for present in lines:
    dimensions = [int(x) for x in present.split("x")]
    part1_ans += calc_wrapping_paper(dimensions)
    part2_ans += calc_ribbon(dimensions)
    
print("part 1 answer: " + str(part1_ans))
print("part 2 answer: " + str(part2_ans))