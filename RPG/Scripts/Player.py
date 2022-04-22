from configs import *

# Classe do Jogador
class Player(object):
    def __init__(self, X, Y, width, height):
        self.x = X
        self.y = Y
        self.largura = width
        self.altura = height
        self.vel = vel
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.hitbox = (self.x, self.y, 32, 32)

    def draw(self, screen):
        if self.walkCount == 3:
            self.walkCount = 0
        if self.left:
            screen.blit(walkLeft[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            screen.blit(walkRight[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        elif self.up:
            screen.blit(walkUp[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        elif self.down:
            screen.blit(walkDown[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        else:
            screen.blit(parado, (self.x, self.y))
        self.hitbox = (self.x, self.y, 32, 32)
