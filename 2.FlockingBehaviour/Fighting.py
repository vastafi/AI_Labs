import math
import random

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Global variables
canvas_width = 600
canvas_height = 400

#Task 1. Implementing the Vector Class
class Vector:
    def __init__(self, values):
        self.values = values

    def norm(self):
        return math.sqrt(sum(x**2 for x in self.values))

    def add(self, other):
        return Vector([x + y for x, y in zip(self.values, other.values)])

    def subtract(self, other):
        return Vector([x - y for x, y in zip(self.values, other.values)])

    def multiply_by_scalar(self, scalar):
        return Vector([x * scalar for x in self.values])

    def divide_by_scalar(self, scalar):
        if scalar == 0:
            raise ValueError("Cannot divide by zero.")
        return Vector([x / scalar for x in self.values])

    def dot_product(self, other):
        return sum(x * y for x, y in zip(self.values, other.values))

    def cross_product(self, other):
        if len(self.values) != 3 or len(other.values) != 3:
            raise ValueError("Cross product is defined for 3D vectors only.")
        return Vector([
            self.values[1] * other.values[2] - self.values[2] * other.values[1],
            self.values[2] * other.values[0] - self.values[0] * other.values[2],
            self.values[0] * other.values[1] - self.values[1] * other.values[0]
        ])

#Auxiliar methods
    def distance(self, other):
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(self.values, other.values)))

    def limit(self, max_length):
        if self.norm() > max_length:
            return self.normalize().multiply_by_scalar(max_length)
        return self

    def normalize(self):
        norm = self.norm()
        if norm != 0:
            return Vector([x / norm for x in self.values])
        return self

#Task 2. Implementing the Boid Class
class Boid:
    def __init__(self, position, velocity, max_speed, max_force, perception_radius):
        self.position = position
        self.velocity = velocity
        self.max_speed = max_speed
        self.max_force = max_force
        self.acceleration = Vector([0, 0])
        self.perception_radius = perception_radius

    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity = self.velocity.limit(self.max_speed)
        self.position.add(self.velocity)
        self.acceleration.multiply_by_scalar(0)

    def separate(self, boids):
        desired_separation = self.perception_radius * 0.5
        steer = Vector([0, 0])
        total = 0
        for other in boids:
            distance = self.position.distance(other.position)
            if 0 < distance < desired_separation:
                diff = self.position.subtract(other.position).normalize().divide_by_scalar(distance)
                steer.add(diff)
                total += 1
        if total > 0:
            steer = steer.divide_by_scalar(total).normalize().multiply_by_scalar(self.max_speed)
        steer = steer.subtract(self.velocity)
        return steer.limit(self.max_force)

    def align(self, boids):
        neighborhood_radius = self.perception_radius
        avg_velocity = Vector([0, 0])
        total = 0
        for other in boids:
            distance = self.position.distance(other.position)
            if 0 < distance < neighborhood_radius:
                avg_velocity.add(other.velocity)
                total += 1
        if total > 0:
            avg_velocity = avg_velocity.divide_by_scalar(total).normalize().multiply_by_scalar(self.max_speed)
            steer = avg_velocity.subtract(self.velocity)
            return steer.limit(self.max_force)
        return Vector([0, 0])

    def cohesion(self, boids):
        neighborhood_radius = self.perception_radius
        center_of_mass = Vector([0, 0])
        total = 0
        for other in boids:
            distance = self.position.distance(other.position)
            if 0 < distance < neighborhood_radius:
                center_of_mass.add(other.position)
                total += 1
        if total > 0:
            center_of_mass = center_of_mass.divide_by_scalar(total)
            return center_of_mass.subtract(self.position).normalize().multiply_by_scalar(self.max_speed).subtract(
                self.velocity).limit(self.max_force)
        return Vector([0, 0])

    #Task 3. Add the calm flocking behaviour
    def apply_behaviors(self, boids):
        separation_weight = 1.5
        alignment_weight = 1.0
        cohesion_weight = 1.0

        separation = self.separate(boids).multiply_by_scalar(separation_weight)
        alignment = self.align(boids).multiply_by_scalar(alignment_weight)
        cohesion = self.cohesion(boids).multiply_by_scalar(cohesion_weight)

        self.acceleration.add(separation)
        self.acceleration.add(alignment)
        self.acceleration.add(cohesion)

#Task 4.


