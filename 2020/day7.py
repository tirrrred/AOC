import time

def sort_input(filename):
    bags = {}
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        bag_content = line.split(' contain ')
        bag = bag_content[0].replace(" bags", "")
        contents = bag_content[1].replace('.\n', '').split(", ")
        if bag in bags:
            continue
        else:
            quantities = {}
            for content in contents:
                if content == "no other bags" or content == "no other bags.":
                    quantities["None"] = "None"
                else:
                    qty_bag = content.split(" ",1)
                    quantities[qty_bag[1].replace(" bags", "").replace(" bag", "")] = qty_bag[0]
            bags[bag] = quantities
    return bags

def find_color(color, bags):
    colors = []
    for bag in bags:
        for bag_color in bags[bag]:
            if bag_color == color:
                colors.append(bag)
                new_colors = find_color(bag, bags)
                colors = colors + new_colors
    return colors

def count_bags(color, bags, count, multiple):
    sub_count = 0
    num_bags = []
    for sub_bags in bags[color].items():
        if sub_bags[0] == 'None':
            return multiple, 'empty'
        quantiy, status = count_bags(sub_bags[0], bags, count, int(sub_bags[1]))
        if status == 'empty':
            if color in num_bags:
                num_bags.remove(color)
        else:
            for i in range(int(sub_bags[1])*multiple):
                num_bags.append(sub_bags[0])
        sub_count += multiple*quantiy
        # print('{} contains {} bags of {}'.format(color, sub_count, sub_bags[0]))
    count += sub_count + len(num_bags)
    # print('sub_count {} + bags {} =  {}'.format(sub_count, len(num_bags), count))
    return count, ''

def part1():
    bags = sort_input('day7_part1_input.txt')
    colors = find_color("shiny gold", bags)
    print(len(set(colors)))

def part2():
    bags = sort_input('day7_part1_input.txt')
    res = count_bags('shiny gold', bags, 0, 1)
    print(res)


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