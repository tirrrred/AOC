import re

def sort_input(filename):
    #(min, max, letter, password)
    sorted_input = []
    f = open(filename)
    f_lines = f.readlines()
    for l in f_lines:
       sorted_input.append(re.split('-| |: |\n',l))
    # print(sorted_input[0])
    return sorted_input

def part1():
    input = sort_input('day2_part1_input.txt')
    valid = 0
    for x in input:
        letter_count = x[3].count(x[2])
        if int(x[0]) <= letter_count <= int(x[1]):
            valid += 1
    print(valid)

def part2():
    input = sort_input('day2_part1_input.txt')
    valid = 0
    for x in input:
        password = x[3]
        pos1, pos2 = int(x[0])-1, int(x[1])-1
        if password[pos1] == x[2] and password[pos2] != x[2] or password[pos1] != x[2] and password[pos2] == x[2]:
            valid += 1
    print(valid)

def main():
    print('-------PART 1 START-------')
    part1()
    print('-------PART 1 END-------')
    print('-------PART 2 START-------')
    part2()
    print('-------PART 2 END-------')

main()


