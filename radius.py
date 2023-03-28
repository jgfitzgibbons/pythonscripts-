#radius

import math

def main():
    print("This program finds the radius of a circle with a given area")
    print()

    area = float(input("Enter the area of the circle: "))
    pi = math.pi

    radius = math.sqrt(area/pi)

    print()
    print("The radius is:", radius)

main()

    
    
