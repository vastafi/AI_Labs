import numpy as np

class VectorNumpy:
    """Python class that works with numpy arrays"""
    def vector_norm(self, vector):
        """Calculate the norm of a vector
        
        Args:
            vector (np.array): A numpy array of numbers
        
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