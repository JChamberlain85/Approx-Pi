import random

INTERVAL = int(input("How Many Points Should be Plotted? "))

i = int(input("How many Tests would you like to run? "))

def approxTri(INTERVAL):
    squareSide = int(input("Enter the side length for our square: "))
    inTri = 0

    for i in range(INTERVAL):
        # Generate random point in square
        x = random.uniform(-squareSide, squareSide)
        y = random.uniform(-squareSide, squareSide)
        
        # Check if point in triangle
        if abs(x) <= (squareSide / 2):
            inTri += 1
        
    estimatedArea = squareSide ** 2 * inTri / INTERVAL
    return estimatedArea

for i in range(i):
    triApprox = approxTri(INTERVAL)
    print("Estimated Area of Triangle:", triApprox)
