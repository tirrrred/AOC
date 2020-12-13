import time

def sort_input(filename):
    groups = []
    f = open(filename)
    lines = f.readlines()
    old = 0
    for i, line in enumerate(lines):
        if line == '\n':
            groups.append(lines[old:i])
            old = i
        if i == len(lines) - 1:
            #Catch the last 'person'
            groups.append(lines[old:])
    groups_filtered = []
    for group in groups:
        new_group = []
        for element in group:
            if element == '\n':
                continue
            else:
                new_element = element.replace('\n', '')
            new_group.append(new_element)
        groups_filtered.append(new_group)
    return groups_filtered

def count_chars(group):
    chars = []
    for answer in group:
        for char in answer:
            if char not in chars:
                chars.append(char)
    return len(chars)

def count_chars_part2(group):
    persons = len(group)
    counts = {}
    for person in group:
        for answer in person:
            if answer in counts:
                counts[answer] += 1
            else:
                counts[answer] = 1
    count = 0
    for item in counts.items():
        if item[1] == persons:
            count += 1
    return count


def part1():
    groups = sort_input('day6_part1_input.txt')
    res = 0
    for group in groups:
        count = count_chars(group)
        res += count
    print(res)

def part2():
    groups = sort_input('day6_part1_input.txt')
    res = 0
    for group in groups:
        count = count_chars_part2(group)
        res += count
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