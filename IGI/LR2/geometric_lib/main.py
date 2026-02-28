import os
import circle
import square


radius = float(os.getenv("RADIUS", 0))
side = float(os.getenv("SIDE", 0))

print("---функции---")

if radius > 0:
    print(f"круг (R={radius}):")
    print(f"  площадь: {circle.area(radius):.2f}")
    print(f"  периметр: {circle.perimeter(radius):.2f}")

if side > 0:
    print(f"квадрат (A={side}):")
    print(f"  площадь: {square.area(side)}")
    print(f"  периметр: {square.perimeter(side)}")
