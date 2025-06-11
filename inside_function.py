
def calculate_rectangle_area(length, width):
    assert length > 0 and width > 0, "Length and width" + \
                "must be positive"

    area = length * width
    return area


area1 = calculate_rectangle_area(5, 6)
print("Area of rectangle with length 5 and width 6 is", area1)

area2 = calculate_rectangle_area(-5, 6)
print("Area of rectangle with length -5 and width 6 is", area2)