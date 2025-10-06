# Name: Ivy Loi
# Class Section: 3
# File Purpose: Calculate perimeter and area of a rectangle

def is_int(length):
    """ Checking if length entered is int """
    try:
        int(length)
        return True
    except ValueError:
        return False

def is_int(width):
    """ Checking if width entered is int """
    try:
        int(width)
        return True
    except ValueError:
        return False

def perimeter(*, length, width):
    """ Calculating perimeter  of rectangle """
    if not is_int(length) or not is_int(width):
        print("The length or width is not a valid number")
        return "error"
    elif not is_int(length) and not is_int(width):
        print("Both length and width are not valid numbers")
        return "error"
    else:
        return ((2 * length) + (2 * width))

def area(*, length, width):
    """ Calculating area of rectangle """
    if not is_int(length) or not is_int(width):
        print("The length or width is not a valid number")
        return "error"
    elif not is_int(length) and not is_int(width):
        print("Both length and width are not valid numbers")
        return "error"
    else:
        return (length * width)