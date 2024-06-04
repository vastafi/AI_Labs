import numpy as np

class VectorNumpy:
    """Python class that works with numpy arrays"""

    def vector_norm(self, vector):
        """Calculate the norm of a vector

        Args:
            vector (np.array): A numpy array of numbers
           # linalg: NumPy module for linear algebra.
        Returns:
            float: The norm of the vector

        """
        return np.linalg.norm(vector)

    def vector_add(self, vector1, vector2):
        """Add two vectors

        Args:
            vector1 (np.array): A numpy array of numbers
            vector2 (np.array): A numpy array of numbers

        Returns:
            np.array: A numpy array of numbers

        """
        return np.add(vector1, vector2)

    def vector_subtract(self, vector1, vector2):
        """Subtract two vectors

        Args:
            vector1 (np.array): A numpy array of numbers
            vector2 (np.array): A numpy array of numbers

        Returns:
            np.array: A numpy array of numbers

        """
        return np.subtract(vector1, vector2)

    def vector_multiply(self, vector, scalar):
        """Multiply a vector by a scalar

        Args:
            vector (np.array): A numpy array of numbers
            scalar (float): A number

        Returns:
            np.array: A numpy array of numbers

        """
        return np.multiply(vector, scalar)

    def vector_division(self, vector, scalar):
        """Divide a vector by a scalar

        Args:
            vector (np.array): A numpy array of numbers
            scalar (float): A number

        Returns:
            np.array: A numpy array of numbers

        """
        return np.divide(vector, scalar)

    def dot_product(self, vector1, vector2):
        """Calculate the dot product of two vectors

        Args:
            vector1 (np.array): A numpy array of numbers
            vector2 (np.array): A numpy array of numbers

        Returns:
            float: The dot product of the two vectors

        """
        return np.dot(vector1, vector2)

    def cross_product(self, vector1, vector2):
        """Calculate the cross product of two vectors

        Args:
            vector1 (np.array): A numpy array of numbers
            vector2 (np.array): A numpy array of numbers

        Returns:
            np.array: A numpy array of numbers

        """
        return np.cross(vector1, vector2)


# Create an instance of VectorNumpy
vn = VectorNumpy()

# Define some vectors
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
scalar = 2

# Test the methods
print("Norm of vector1:", vn.vector_norm(vector1))
print("Addition of vector1 and vector2:", vn.vector_add(vector1, vector2))
print("Subtraction of vector1 from vector2:", vn.vector_subtract(vector2, vector1))
print("Multiplication of vector1 by scalar:", vn.vector_multiply(vector1, scalar))
print("Division of vector2 by scalar:", vn.vector_division(vector2, scalar))
print("Dot product of vector1 and vector2:", vn.dot_product(vector1, vector2))
print("Cross product of vector1 and vector2:", vn.cross_product(vector1, vector2))
