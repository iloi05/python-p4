# Name: Ivy Loi
# Class Section: 3
# File Purpose: Calculate surface area and volume of a cube

def is_int(side):
    """ Checking if side entered is an int """
    try:
        int(side)
        return True
    except ValueError:
        return False
    
def surface_area(*, side):
    """ Calculating surface area of cube """
    if not is_int(side):
        print("The side is not a valid number")
        return "error"
    else:
        return (6 * side ** 2)

def volume(*, side):
    """ Calculating volume of cube """
    if not is_int(side):
        print("The side is not a valid number")
        return "error"
    else:
        return (side ** 3)