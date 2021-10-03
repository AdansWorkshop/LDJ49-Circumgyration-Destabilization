import pygame, math

class Body():
    def __init__(self, mass, startpos, startvec, radius, color):
        self.mass = mass
        self.startpos = startpos
        self.x = self.startpos[0]
        self.y = self.startpos[1]
        self.vec = startvec
        self.radius = radius
        self.color = color
    
    def attractandcollide(self, others):
        for i in range(0, len(others)):
            other = others[i]
            dx = (self.x - other.x)
            dy = (self.y - other.y)
            dist = math.hypot(dx, dy)
                
            theta = math.atan2(dy, dx)
            force = 0.125 * self.mass * other.mass / dist ** 2
            self.vec = (theta - 0.5 * math.pi, force/self.mass)
            other.vec = (theta + 0.5 * math.pi, force/other.mass)
            other.accel(other.vec)
            self.accel(self.vec)
    
    def update(self, otherbodies, screen):
        self.attractandcollide(otherbodies)
        self.draw(screen)
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    
    def accel(self, vec):
        vel = (vec[1] * math.cos(vec[0]), vec[1] * math.sin(vec[0]))
        self.x += vel[0]
        self.y += vel[1]