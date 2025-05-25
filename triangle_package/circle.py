import math

def print_circle(radius):
    for i in range(2 * radius + 1):
        for j in range(2 * radius + 1):
            distance = math.sqrt((i - radius)**2 + (j - radius)**2)
            if abs(distance - radius) < 0.5:
                print("*", end=" ")
            else:
                print(" ", end="")
        print()