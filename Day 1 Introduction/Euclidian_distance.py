# Day 1 Exercise
# Find an Euclidian distance between (2, 3) and (10, 8)

import math

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))

x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

result = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
print(f"The Distance between ({x1},{y1}) and ({x2}, {y2}) is", result)
