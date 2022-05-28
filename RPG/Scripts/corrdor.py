from configs import *
from Player import Player
import sys


def corredorf():
    pygame.init()
    corredor = pygame.image.load('../Assets/Mapa/corredor1.png')
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('RPG')
    game = True

    def tela_jogo():
        global walkCount
        tela.fill((0, 204, 204))
        tela.blit(corredor, (fx, fy))
        character.draw(tela)
        portas.draw(tela)
        pygame.display.update()

    class Porta:
        def __init__(self):
            self.hitbox0 = pygame.Rect((150 + fx, 550 + fy), (30, 40))
            self.hitbox1 = pygame.Rect((26 + fx, 510 + fy), (40, 30))
            self.hitbox2 = pygame.Rect((26 + fx, 396 + fy), (40, 30))
            self.hitbox3 = pygame.Rect((26 + fx, 282 + fy), (40, 30))
            self.hitbox4 = pygame.Rect((26 + fx, 168 + fy), (40, 30))
            self.hitbox5 = pygame.Rect((26 + fx, 54 + fy), (40, 30))

        def draw(self, screen):
            self.hitbox0 = pygame.Rect((150 + fx, 550 + fy), (30, 40))
            self.hitbox1 = pygame.Rect((26 + fx, 510 + fy), (40, 30))
            self.hitbox2 = pygame.Rect((26 + fx, 396 + fy), (40, 30))
            self.hitbox3 = pygame.Rect((26 + fx, 282 + fy), (40, 30))
            self.hitbox4 = pygame.Rect((26 + fx, 168 + fy), (40, 30))
            self.hitbox5 = pygame.Rect((26 + fx, 54 + fy), (40, 30))
            # pygame.draw.rect(screen, VERMELHO, self.hitbox0, 2)
            # pygame.draw.rect(screen, VERMELHO, self.hitbox1, 2)
            # pygame.draw.rect(screen, VERMELHO, self.hitbox2, 2)
            # pygame.draw.rect(screen, VERMELHO, self.hitbox3, 2)
            # pygame.draw.rect(screen, VERMELHO, self.hitbox4, 2)
            # pygame.draw.rect(screen, VERMELHO, self.hitbox5, 2)

    x = 390
    y = 500
    fx = 241
    fy = 21
    character = Player(x, y, 32, 32)
    portas = Porta()
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if character.rect.colliderect(portas.hitbox0):
                from main import entrada
                game = False
                entrada()
            if character.rect.colliderect(portas.hitbox1):
                from lv1 import sala1
                game = False
                sala1()
            if character.rect.colliderect(portas.hitbox2):
                from lv2 import sala2
                game = False
                sala2()
            if character.rect.colliderect(portas.hitbox3):
                from lv3 import sala3
                game = False
                sala3()
            if character.rect.colliderect(portas.hitbox4):
                from lv4 import sala4
                game = False
                sala4()
            if character.rect.colliderect(portas.hitbox5):
                from lv5 import sala5
                game = False
                sala5()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and character.x >= fx + (x - x):
            character.x -= character.vel
            fx += vel
            character.left = True
            character.right = False
            character.up = False
            character.down = False
        elif keys[pygame.K_RIGHT] and character.x <= fx + 210:
            character.x += character.vel
            fx -= vel
            character.right = True
            character.left = False
            character.up = False
            character.down = False
        elif keys[pygame.K_UP] and character.y >= 10 + fy:
            character.y -= character.vel
            fy += vel
            character.up = True
            character.right = False
            character.left = False
            character.down = False
        elif keys[pygame.K_DOWN] and character.y <= fy + ALTURA_TELA - 80:
            character.y += character.vel
            fy -= vel
            character.down = True
            character.right = False
            character.left = False
            character.up = False
        else:
            character.walkCount = 1
        tela_jogo()
        pygame.time.delay(30)


corredorf()
