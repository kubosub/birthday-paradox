'''This is a simulation of the birthday paradox (the birthday problem).'''
from random import randint

def get_birthdays(size):
    '''Returns a list of birthday numbers, 1-365'''
    bdays = []
    for _ in range(size):
        bday = randint(1,365)
        bdays.append(bday)
    return bdays

def check_match(bdays):
    '''Check if birthday list equals length of unique-birthdays list (set)'''
    return len(bdays) != len(set(bdays))

def input_valid_integer(prompt):
    '''Validate integer input'''
    while True:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
            if (user_input < 1): raise Exception("Sorry, no numbers below zero")
            return user_input
        except:
            print("Does not compute. Try again.")

def main():
    '''Main program'''
    groups = input_valid_integer("Number of groups: ")
    group_size = input_valid_integer("Number of students in each group: ")

    match_count = 0
    for _ in range(groups):
        bdays = get_birthdays(group_size)
        if check_match(bdays):
            match_count += 1

    print(f"Of {groups} groups with {group_size} people in each group, "\
          f"we found that {match_count} groups had matching birthdays.\n"\
          f"Thats {match_count/groups*100}% of the groups.")

if __name__ == '__main__':
    main()
