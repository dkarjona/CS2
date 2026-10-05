import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt(
    math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)
)

print("The distance between the two points is:",
      round(distance, 2))

# Reflection:
# The math library makes calculations easier because it provides useful functions like sqrt() and pow(). These functions help me calculate the distance accurately without having to create my own methods for powers and square roots.
