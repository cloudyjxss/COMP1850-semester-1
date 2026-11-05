
# function implementation
width = int(input("Enter the width: "))
height = int(input("Enter the height: "))

def rectangle_area(width, height):  # define suitable input data
    area = width*height             # implement the function
    return  area            # return an appropriate value

# testing the function

print(f"Area is {rectangle_area(width, height)}")   # provide suitable data matching your inputs
