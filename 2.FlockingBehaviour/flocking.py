from vector_operations.vector_list import VectorList

class Boid:
    def __init__(self, position, velocity, max_speed, max_force, separation_radius, alignment_radius, cohesion_radius, evade_radius, attack_radius):
        self.position = position
        self.velocity = velocity
        self.max_speed = max_speed
        self.max_force = max_force
        self.separation_radius = separation_radius
        self.alignment_radius = alignment_radius
        self.cohesion_radius = cohesion_radius
        self.evade_radius = evade_radius
        self.attack_radius = attack_radius
        self.vector_list = VectorList()
    
    def separation(self, boids):
        """Steering behavior that keeps the boids separated from each other
        Args:
            boids (list): A list of boids
        Returns:
            np.array: A numpy array of numbers
        """
        steering = [0, 0]
        count = 0
        for boid in boids:
            distance = self.vector_list.vector_norm(self.vector_list.vector_subtract(self.position, boid.position))
            if distance > 0 and distance < self.separation_radius:
                diff = self.vector_list.vector_subtract(self.position, boid.position)
                diff = self.vector_list.vector_division(diff, distance)
                steering = self.vector_list.vector_add(steering, diff)
                count += 1
        if count > 0:
            steering = self.vector_list.vector_division(steering, count)
        if self.vector_list.vector_norm(steering) > 0:
            steering = self.vector_list.vector_division(steering, self.vector_list.vector_norm(steering))
        return steering
    
    def alignment(self, boids):
        """Steering behavior that keeps the boids aligned with each other
        Args:
            boids (list): A list of boids
        Returns:
            np.array: A numpy array of numbers
        """
        steering = [0, 0]
        count = 0
        for boid in boids:
            distance = self.vector_list.vector_norm(self.vector_list.vector_subtract(self.position, boid.position))
            if distance > 0 and distance < self.alignment_radius:
                steering = self.vector_list.vector_add(steering, boid.velocity)
                count += 1
        if count > 0:
            steering = self.vector_list.vector_division(steering, count)
        if self.vector_list.vector_norm(steering) > 0:
            steering = self.vector_list.vector_division(steering, self.vector_list.vector_norm(steering))
        return steering
    
    def cohesion(self, boids):
        """Steering behavior that keeps the boids together
        Args:
            boids (list): A list of boids
        Returns:
            np.array: A numpy array of numbers
        """
        steering = [0, 0]
        count = 0
        for boid in boids:
            distance = self.vector_list.vector_norm(self.vector_list.vector_subtract(self.position, boid.position))
            if distance > 0 and distance < self.cohesion_radius:
                steering = self.vector_list.vector_add(steering, boid.position)
                count += 1
        if count > 0:
            steering = self.vector_list.vector_division(steering, count)
            steering = self.vector_list.vector_subtract(steering, self.position)
        if self.vector_list.vector_norm(steering) > 0:
            steering = self.vector_list.vector_division(steering, self.vector_list.vector_norm(steering))
        return steering
    
    def calm(self, boids):
        """Steering behavior that keeps the boids calm
        Args:
            boids (list): A list of boids
        Returns:
            np.array: A numpy array of numbers
        """
        separation = self.separation(boids)
        alignment = self.alignment(boids)
        cohesion = self.cohesion(boids)
        separation = self.vector_list.vector_multiply(separation, 1.5)
        alignment = self.vector_list.vector_multiply(alignment, 1.0)
        cohesion = self.vector_list.vector_multiply(cohesion, 1.0)
        steering = self.vector_list.vector_add(separation, alignment)
        steering = self.vector_list.vector_add(steering, cohesion)
        if self.vector_list.vector_norm(steering) > 0:
            steering = self.vector_list.vector_division(steering, self.vector_list.vector_norm(steering))
        return steering
    
    def evade(self, boids):
        """Steering behavior that keeps the boids away from each other
        Args:
            boids (list): A list of boids
        Returns:
            np.array: A numpy array of numbers
        """
        steering = [0, 0]
        count = 0
        for boid in boids:
            distance = self.vector_list.vector_norm(self.vector_list.vector_subtract(self.position, boid.position))
            if distance > 0 and distance < self.evade_radius:
                diff = self.vector_list.vector_subtract(self.position, boid.position)
                diff = self.vector_list.vector_division(diff, distance)
                steering = self.vector_list.vector_add(steering, diff)
                count += 1
        if count > 0:
            steering = self.vector_list.vector_division(steering, count)
        if self.vector_list.vector_norm(steering) > 0:
            steering = self.vector_list.vector_division(steering, self.vector_list.vector_norm(steering))
        return steering
    
    def attack(self, boids):
        """Steering behavior that keeps the boids towards each other
        Args:
            boids (list): A list of boids
        Returns:
            np.array: A numpy array of numbers
        """
        steering = [0, 0]
        count = 0
        for boid in boids:
            distance = self.vector_list.vector_norm(self.vector_list.vector_subtract(self.position, boid.position))
            if distance > 0 and distance < self.attack_radius:
                steering = self.vector_list.vector_add(steering, boid.position)
                count += 1
        if count > 0:
            steering = self.vector_list.vector_division(steering, count)
            steering = self.vector_list.vector_subtract(steering, self.position)
        if self.vector_list.vector_norm(steering) > 0:
            steering = self.vector_list.vector_division(steering, self.vector_list.vector_norm(steering))
        return steering
    