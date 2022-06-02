from configs import *

# Classe do Jogador
class Player(object):
    def __init__(self, X, Y, width, height):
        self.x = X
        self.y = Y
        self.largura = width
        self.altura = height
        self.vel_x = 7
        self.vel_y = 7
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.rect = pygame.Rect((self.x, self.y), (self.largura, self.altura))

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

        self.rect = pygame.Rect((self.x, self.y), (self.largura, self.altura))
        # pygame.draw.rect(screen, VERMELHO, self.rect, 2)
    # Classe Inimigo
class Inimigos(object):
    def __init__(self, a, b, width, height, end):
        self.x = a
        self.y = b
        self.width = width
        self.height = height
        self.end = end
        self.path = [a, end]
        self.walkCount = 0
        self.vel = 7
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))


    def draw(self, win):
        self.movimento()
        if self.walkCount == 3:
            self.walkCount = 0
        if self.vel > 0:
            win.blit(walkRightE[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(walkLeftE[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))

    def movimento(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1] + fundo_x:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 1
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

