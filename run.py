'''This is a simulation of the birthday paradox (the birthday problem).'''
from sys import exit
from random import randint

def get_birthdays(size):
    '''Returns a list of birthday numbers, 1-365'''
    bdays = []
    for _ in range(size):
        bday = randint(1,366)
        bdays.append(bday)
    return bdays

def check_match(bdays):
    '''Here we do the actual check to see if we have matching birthdays'''
    for _ in bdays:
        bday = bdays.pop(0)
        if bday in bdays:
            return True
    return False

def validate_number(num):
    '''Is it a valid number?'''
    return num.isdigit() and int(num) > 0

def main():
    '''Main program'''
    groups = input("Number of groups: ")
    group_size = input("Number of students in each group: ")

    if not (validate_number(groups) and validate_number(group_size)):
        print("INPUT ERROR")
        exit()

    groups_number = int(groups)
    group_size_number = int(group_size)

    match_count = 0
    for _ in range(groups_number):
        bdays = get_birthdays(group_size_number)
        if check_match(bdays):
            match_count += 1

    print(f"Of {groups_number} groups with {group_size_number} people in each group, "\
          f"we found that {match_count} groups had matching birthdays.\n"\
          f"Thats {match_count/groups_number*100}% of the groups.")

if __name__ == '__main__':
    main()
