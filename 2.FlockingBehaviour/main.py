from Fighting import Vector
from Fighting import Boid
import random

def main():
   # Creating instances of Vector
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])

    # Demonstrating functionalities
    print(f"Norm of v1: {v1.norm():.2f}")
    print(f"Norm of v2: {v2.norm():.2f}")

    print("Adding v1 and v2:", v1.add(v2).values)
    print("Subtracting v2 from v1:", v1.subtract(v2).values)

    print("Multiplying v1 by scalar 2:", v1.multiply_by_scalar(2).values)
    print("Dividing v1 by scalar 2:", v1.divide_by_scalar(2).values)

    print("Dot product of v1 and v2:", v1.dot_product(v2))

    try:
        print("Cross product of v1 and v2:", v1.cross_product(v2).values)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()