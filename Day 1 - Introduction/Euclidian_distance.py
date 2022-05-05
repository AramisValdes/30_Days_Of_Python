# Day 1 Exercise
# Find an Euclidian distance between (2, 3) and (10, 8)
# formula for the Euclidian distance is d = √((x2-x1)**2 + (y2-y1)**2)

import math

print("Let's calculate the distance between two points.\n")

# Asks user for first and second point in one line splits the 2 (x,y) inputs with the ","
x1, y1 = input("Enter the first point x1,y1: ").split(",", 2)
x2, y2 = input("Enter the second point x2,y2: ").split(",", 2)

# Calculates the result using the math module for square root and sets variables as integers.
result = math.sqrt(((int(x2) - int(x1)) ** 2) + ((int(y2) - int(y1)) ** 2))

# Uses f to print multiple variables with single print statement and truncate to 4 decimal spaces.
print(f"The Distance between ({x1},{y1}) and ({x2}, {y2}) is {result:.4f}")
