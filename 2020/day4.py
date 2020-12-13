import time

def sort_input(filename):
    #List to store every passports details, but will include some trash/noise
    #The temp_passports list will be used to store with trash/noise, and than filter it out into a new list 
    #called passorts
    temp_passports = []
    passports = []
    f = open(filename)
    lines = f.readlines()
    old = 0
    for i, line in enumerate(lines):
        if line == '\n':
            #Catch every passport, as they are separeted by a blank line ('\n')
            #This alsoc catches noise like new lines ('\n') and stores the passport in different elements within the list.
            temp_passports.append(lines[old:i])
            old = i
        if i == len(lines) - 1:
            #Catch the last 'passport'
            temp_passports.append(lines[old:])
    for passport in temp_passports:
        #Iteraters over each passport to filter out noise and store the passport as a single string element in the list 'passports'
        new_passport = ''
        for element in passport:
            new_element = element.replace('\n', '')
            new_passport += ' ' + new_element
        passports.append(new_passport)
    return passports

valid_passport_part1 = ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm']

def part1():
    passports = sort_input('day4_part1_input.txt')
    #List of required fields in the passports
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    count = 0
    for passport in passports:
        #Iterate over every passport. Assumes every passport is valid until proven otherwise
        valid = True
        for field in required_fields:
            if passport.find(field) == -1:
                #If one can't find the required field in the passports, it is set to unvalid
                valid = False
                break
        if valid:
            #Check if valid passports and increment counter
            count += 1
    print('Number of valid passports: {}'.format(count))

def part2():
    passports = sort_input('day4_part1_input.txt')
    #List of required fields in the passports
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_hcl_chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    count = 0
    for passport in passports:
        #Iterate over every passport. Assumes every passport is valid until proven otherwise
        valid = True
        # print(passport)
        for field in required_fields:
            if passport.find(field) == -1:
                #If one can't find the required field in the passports, it is set to unvalid
                valid = False
                # print(passport)
                # print('Invalid: Missing required filed {}'.format(field))
                break
        key_vals = passport.split()
        for key_val in key_vals:
            k_v = key_val.split(':')
            if k_v[0] == 'byr':
                byr = int(k_v[1])
                if not 1920 <= byr <= 2002:
                    # print(passport)
                    # print('Invalid: {} is invalid'.format(k_v[0]))
                    valid = False
                    break
            if k_v[0] == 'iyr':
                iyr = int(k_v[1])
                if not 2010 <= iyr <= 2020:
                    # print(passport)
                    # print('Invalid: {} is invalid'.format(k_v[0]))
                    valid = False
                    break 
            if k_v[0] == 'eyr':
                eyr = int(k_v[1])
                if not 2020 <= eyr <= 2030:
                    #print(passport)
                    #print('Invalid: {} is invalid'.format(k_v[0]))
                    valid = False
                    break
            if k_v[0] == 'hgt':
                if k_v[1][-2:] != 'cm' and k_v[1][-2:] != 'in':
                    valid = False
                    break
                if k_v[1][-2:] == 'cm':
                    hgt = int(k_v[1][:-2])
                    if not 150 <= hgt <= 193:
                        #print(passport)
                        #print('Invalid: {} is invalid'.format(k_v[0]))
                        valid = False
                        break
                if k_v[1][-2:] == 'in':
                    hgt = int(k_v[1][:-2])
                    if not 59 <= hgt <= 76:
                        #print(passport)
                        #print('Invalid: {} is invalid'.format(k_v[0]))
                        valid = False
                        break
            if k_v[0] == 'hcl':
                if len(k_v[1]) != 7:
                    #print(passport)
                    #print('Invalid: {} is invalid'.format(k_v[0]))
                    valid = False
                    break
                if k_v[1][0] != '#':
                    #print(passport)
                    #print('Invalid: {} is invalid'.format(k_v[0]))
                    valid = False
                    break
                #Check if hair color only contains hex digits (0-9A-F)
                for char in k_v[1][1:]:
                    if char not in valid_hcl_chars:
                        #print(passport)
                        #print('Invalid: {} is invalid'.format(k_v[0]))
                        valid = False
                        break
            if k_v[0] == 'ecl':
                if k_v[1] not in valid_ecl:
                    #print(passport)
                    #print('Invalid: {} is invalid - got {}'.format(k_v[0], k_v[1]))
                    valid = False
                    break
            if k_v[0] == 'pid':
                if len(k_v[1]) != 9 or k_v[1].isdigit() is False:
                    #print(passport)
                    #print('Invalid: {} is invalid - got {}'.format(k_v[0], k_v[1]))
                    valid = False
                    break
        if valid:
            print('Valid:', passport)
            #Check if valid passports and increment counter
            count += 1
    print('Number of valid passports: {}'.format(count))  

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
