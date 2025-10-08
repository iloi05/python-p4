# Name: Ivy Loi
# Class Section: 3
# File Purpose: Calculate sum and average of list

def is_int(list):
    """ Checking if all elements in the list are ints """
    return all(isinstance(item, int) for item in list)

def is_int(avg):
    """ Checking if all elements in the list are ints """
    return all(isinstance(item, int) for item in avg)

def sum_total(*, list):
    """ Adding all elements in the list """
    if not is_int(list):
        print("One of the values entered is not a valid number")
        return "error"
    else:
        return sum(list)

def average(*, list):
    """ Calculating mean of list """
    if not is_int(list):
        print("One of the values entered is not a valid numbr")
        return "error"
    else:
        return sum(list)/len(list)