# Name: Ivy Loi
# Class Section: 3
# File Purpose: Calculate sum and average of list

def is_int(total):
    """ Checking if all elements in the list are ints """
    return all(isinstance(item, int) for item in total)

def is_int(avg):
    """ Checking if all elements in the list are ints """
    return all(isinstance(item, int) for item in avg)

def sum_total(*, total):
    """ Adding all elements in the list """
    if not is_int(total):
        print("One of the values entered is not a valid number")
        return "error"
    else:
        return sum(total)

def average(*, avg):
    """ Calculating mean of list """
    if not is_int(avg):
        print("One of the values entered is not a valid numbr")
        return "error"
    else:
        return sum(avg)/len(avg)