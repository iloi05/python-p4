# Name: Ivy Loi
# Section: 3
# File Purpose: Adding, subtracting, multiplying, and dividing left and right int

def is_int(left):
    """ Checking if left is int """
    try:
        int(left)
        return True
    except ValueError:
        return False
    
def is_int(right):
    """ Checking if right is int """
    try:
        int(right)
        return True
    except ValueError:
        return False

def addition(*, left, right):
    """ Adding left and right int """
    if not is_int(left) or not is_int(right):
        print("Left or right is not a valid number")
        return "error"
    elif not is_int(left) and not is_int(right):
        print("Both left and right are not valid numbers")
        return "error"
    else:
        return left + right

def subtraction(*, left, right):
    """ Subtraction left and right int """
    if not is_int(left) or not is_int(right):
        print("Left or right is not a valid number")
        return "error"
    elif not is_int(left) and not is_int(right):
        print("Both left and right are not valid numbers")
        return "error"
    else:
        return left - right

def multiplication(*, left, right):
    """ Multiplying left and right int """
    if not is_int(left) or not is_int(right):
        print("Left or right is not a valid number")
        return "error"
    elif not is_int(left) and not is_int(right):
        print("Both left and right are not valid numbers")
        return "error"
    else:
        return left * right

def division(*, left, right):
    """ Dividing left and right int """
    if not is_int(left) or not is_int(right):
        print("Left or right is not a valid number")
        return "error"
    elif not is_int(left) and not is_int(right):
        print("Both left and right are not valid numbers")
        return "error"
    else:
        return left / right