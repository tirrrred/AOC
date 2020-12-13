

def part1():
    f = open('day3_part1_input.txt')
    #creates a list of each line of the input. Uses read().splitlines() to remove trailing whitespaces
    fl = f.read().splitlines()
    #calls slope() which is a recursive function which iterates through the input, 'fl', with the given slope of the task (x+3 and y+1)
    slope(0,0,0,fl)

def slope(x, y, count, input):
    x = (x + 3) % len(input[0])
    y += 1
    if input[y][x] == '#':
            count += 1
    if y == (len(input) - 1):
        print('Reach End')
        print(count)
        return count
    else:
        slope(x,y,count,input)

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

def part2():
    f = open('day3_part1_input.txt')
    #creates a list of each line of the input. Uses read().splitlines() to remove trailing whitespaces
    fl = f.read().splitlines()
    #calls slope() which is a recursive function which iterates through the input, 'fl', with the given slope of the task (x+3 and y+1)
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    res = 1
    for s in slopes:
        c = slope_2(0,0,s[0],s[1],0,fl)
        res *= c
    print('Result:', res)

def slope_2(x, y, slope_x, slope_y, count, input):
    x = (x + slope_x) % len(input[0])
    y += slope_y
    if input[y][x] == '#':
            count += 1
    if y == (len(input) - 1):
        print('Completed with slope_x {} and slope_y {}'.format(slope_x, slope_y))
        print(count)
        return count
    return slope_2(x, y, slope_x, slope_y, count, input)


    

def main():
    print('-------PART 1 START-------')
    part1()
    print('-------PART 1 END-------')
    print('-------PART 2 START-------')
    part2()
    print('-------PART 2 END-------')

main()