class VectorList:
    """Python class that works on simple python lists"""

    def vector_norm(self, vector):
        """Calculate the norm of a vector

        Args:
            vector (list): A list of numbers

        Returns:
            float: The norm of the vector

        """
        return sum([x ** 2 for x in vector]) ** 0.5

    def vector_add(self, vector1, vector2):
        """Add two vectors

        Args:
            vector1 (list): A list of numbers
            vector2 (list): A list of numbers

        Returns:
            list: A list of numbers

        """
        return [vector1[i] + vector2[i] for i in range(len(vector1))]

    def vector_subtract(self, vector1, vector2):
        """Subtract two vectors

        Args:
            vector1 (list): A list of numbers
            vector2 (list): A list of numbers

        Returns:
            list: A list of numbers

        """
        return [vector1[i] - vector2[i] for i in range(len(vector1))]

    def vector_multiply(self, vector, scalar):
        """Multiply a vector by a scalar

        Args:
            vector (list): A list of numbers
            scalar (float): A number

        Returns:
            list: A list of numbers

        """
        return [vector[i] * scalar for i in range(len(vector))]

    def vector_division(self, vector, scalar):
        """Divide a vector by a scalar

        Args:
            vector (list): A list of numbers
            scalar (float): A number

        Returns:
            list: A list of numbers

        """
        if scalar != 0:
            return [vector[i] / scalar for i in range(len(vector))]

    def dot_product(self, vector1, vector2):
        """Calculate the dot product of two vectors

        Args:
            vector1 (list): A list of numbers
            vector2 (list): A list of numbers

        Returns:
            float: The dot product of the two vectors

        """
        return sum([vector1[i] * vector2[i] for i in range(len(vector1))])

    def cross_product(self, vector1, vector2):
        """Calculate the cross product of two vectors

        Args:
            vector1 (list): A list of numbers
            vector2 (list): A list of numbers

        Returns:
            list: A list of numbers

        """
        return [vector1[1] * vector2[2] - vector1[2] * vector2[1],
                vector1[2] * vector2[0] - vector1[0] * vector2[2],
                vector1[0] * vector2[1] - vector1[1] * vector2[0]]

# Creating an instance of VectorList
vl = VectorList()

# Testing the methods
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
scalarL = 2

print("Norm of vector1:", vl.vector_norm(vector1))
print("Addition of vector1 and vector2:", vl.vector_add(vector1, vector2))
print("Subtraction of vector1 from vector2:", vl.vector_subtract(vector2, vector1))
print("Multiplication of vector1 by scalar:", vl.vector_multiply(vector1, scalarL))
print("Division of vector2 by scalar:", vl.vector_division(vector2, scalarL))
print("Dot product of vector1 and vector2:", vl.dot_product(vector1, vector2))
print("Cross product of vector1 and vector2:", vl.cross_product(vector1, vector2))