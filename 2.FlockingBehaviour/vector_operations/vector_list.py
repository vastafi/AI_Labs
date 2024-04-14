class VectorList:
    """Python class that works on simple python lists"""
    def vector_norm(self, vector):
        """Calculate the norm of a vector
        
        Args:
            vector (list): A list of numbers
        
        Returns:
            float: The norm of the vector
        
        """
        return sum([x**2 for x in vector])**0.5
    
    def vector_add(self, vector1, vector2):
        """Add two vectors
        
        Args:
            vector1 (list): A list of numbers
            vector2 (list): A list of numbers
            
        Returns:
            list: A list of numbers
        
        """
        return [x + y for x, y in zip(vector1, vector2)]
    
    def vector_subtract(self, vector1, vector2):
        """Subtract two vectors

        Args:
            vector1 (list): A list of numbers
            vector2 (list): A list of numbers

        Returns:
            list: A list of numbers

        """
        return [x - y for x, y in zip(vector1, vector2)]
    
    def vector_multiply(self, vector, scalar):
        """Multiply a vector by a scalar
        
        Args:
            vector (list): A list of numbers
            scalar (float): A number
            
        Returns:
            list: A list of numbers
        
        """
        return [x * scalar for x in vector]
    
    def vector_division(self, vector, scalar):
        """Divide a vector by a scalar
        
        Args:
            vector (list): A list of numbers
            scalar (float): A number
            
        Returns:
            list: A list of numbers
        
        """
        return [x / scalar for x in vector]
    
    def dot_product(self, vector1, vector2):
        """Calculate the dot product of two vectors
        
        Args:
            vector1 (list): A list of numbers
            vector2 (list): A list of numbers
            
        Returns:
            float: The dot product of the two vectors
        
        """
        return sum([x * y for x, y in zip(vector1, vector2)])
    
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