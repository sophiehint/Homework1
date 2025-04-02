def calculate_rectangle_area(length, width):

    
    return length*width


def calculate_cuboid(length, width, height):
    if height==0:
        return calculate_rectangle_area(length, width), 0
    else:

        
        surface_area = 2 * (length * width + length * height + width * height)
        volume = length * width * height
        return surface_area, volume

"""
def main():
    shape_choice = input("Choose 'rectangle' or 'cuboid' to calculate area/volume: ").lower()

    if shape_choice == 'rectangle':
        length = float(input("Enter the length of the rectangle in meters: "))
        width = float(input("Enter the width of the rectangle in meters: "))
        if length <= 0 or width <= 0:
            print("Invalid input. Length and width must be positive values.")
        else:
            area = calculate_rectangle_area(length, width)
            print(f"The area of the rectangle is {area:.2f} square meters.")

    elif shape_choice == 'cuboid':
        length = float(input("Enter the length of the cuboid in meters: "))
        width = float(input("Enter the width of the cuboid in meters: "))
        height = float(input("Enter the height of the cuboid in meters: "))

        if length <= 0 or width <= 0:
            print("Invalid input. Length and width must be positive values.")
        else:
            if height == 0:
                area = calculate_rectangle_area(length, width)
                print(f"The area of the rectangle is {area:.2f} square meters.")
            else:
                surface_area, volume = calculate_cuboid(length, width, height)
                print(f"The surface area of the cuboid is {surface_area:.2f} square meters.")
                print(f"The volume of the cuboid is {volume:.2f} cubic meters.")

    else:
        print("Invalid choice. Please choose 'rectangle' or 'cuboid'.")
        
   main()     
   """     


