import time

def sort_input(filename):
    f = open(filename)
    lines = f.readlines()
    return lines

def row_id(boarding_pass):
    bit = ''
    for char in boarding_pass:
        if char == 'B':
            bit += '1'
        if char == 'F':
            bit += '0'
    # print(bit, int(bit,2))
    return int(bit,2)

def col_id(boarding_pass):
    bit = ''
    for char in boarding_pass:
        if char == 'R':
            bit += '1'
        if char == 'L':
            bit += '0'
    # print(bit, int(bit,2))
    return int(bit,2)

def part1():
    b_passes = sort_input('day5_part1_input.txt')
    seats = []
    for b_pass in b_passes:
        row = row_id(b_pass[:7])
        col = col_id(b_pass[7:])
        seat = row * 8 + col
        seats.append(seat)
    print('Highest seat ID: {}'.format(max(seats)))

def part2():
    b_passes = sort_input('day5_part1_input.txt')
    seats = []
    for b_pass in b_passes:
        row = row_id(b_pass[:7])
        col = col_id(b_pass[7:])
        seat = row * 8 + col
        seats.append(seat)
    seats.sort()
    for i in range(1,len(seats)):
        if seats[i] != seats[i-1]+1:
            print('My seat ID is: {}'.format(seats[i]-1))
            print('Seats ID found with a space: {} - # - {} - {}'.format(seats[i-1], seats[i], seats[i+1]))

def main():
    start = time.time()
    print('-------PART 1 START-------')
    part1()
    print('-------PART 1 END-------')
    print('-------PART 2 START-------')
    part2()
    print('-------PART 2 END-------')
    print('---- Completed in {} seconds ----'.format(time.time()-start))

main()