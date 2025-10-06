# Name: Ivy Loi
# Class Section: 3
# File Purpose: Calculate circumference and area of a circle

def is_int(radius):
    """ Checking if radius entered is an int """
    try:
        int(radius)
        return True
    except ValueError:
        return False
    
def circumference(*, radius):
    """ calculate circumference of circle """
    if not is_int(radius):
        print("The radius is not a valid number")
        return "error"
    else:
        return (2 * 3.14 * radius)

def area(*, radius):
    """ calculate area of circle """
    if not is_int(radius):
        print("The radius is not a valid number")
        return "error"
    else:
        return (3.14 * radius ** 2)