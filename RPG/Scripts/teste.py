import pygame
from configs import *

pygame.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

walkRight = [pygame.image.load('../Assets/Personagens/R1.png'),
             pygame.image.load('../Assets/Personagens/R2.png'),
             pygame.image.load('../Assets/Personagens/R3.png')]

walkLeft = [pygame.image.load('../Assets/Personagens/L1.png'),
            pygame.image.load('../Assets/Personagens/L2.png'),
            pygame.image.load('../Assets/Personagens/L3.png')]

walkUp = [pygame.image.load('../Assets/Personagens/U1.png'),
          pygame.image.load('../Assets/Personagens/U2.png'),
          pygame.image.load('../Assets/Personagens/U3.png')]

walkDown = [pygame.image.load('../Assets/Personagens/D1.png'),
            pygame.image.load('../Assets/Personagens/D2.png'),
            pygame.image.load('../Assets/Personagens/S1.png')]

parado = pygame.image.load('../Assets/Personagens/S1.png')

entrada = pygame.image.load('../Assets/Mapa/entrada.png')

running = True
left = False
right = False
up = False
down = False


def redrawGameWindow():
    global walkCount
    tela.blit(entrada, (0, 0))

    if walkCount == 3:
        walkCount = 0

    if left:
        tela.blit(walkLeft[walkCount], (X, Y))
        walkCount += 1
    elif right:
        tela.blit(walkRight[walkCount], (X, Y))
        walkCount += 1
    elif up:
        tela.blit(walkUp[walkCount], (X, Y))
        walkCount += 1
    elif down:
        tela.blit(walkDown[walkCount], (X, Y))
        walkCount += 1
    else:
        tela.blit(parado, (X, Y))

    pygame.display.update()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        X -= VEL
        left = True
    elif keys[pygame.K_RIGHT]:
        X += VEL
        right = True
    elif keys[pygame.K_UP]:
        Y -= VEL
        up = True
    elif keys[pygame.K_DOWN]:
        Y += VEL
        down = True
    else:
        right = False
        left = False
        up = False
        down = False
        walkCount = 0
    redrawGameWindow()
    pygame.time.delay(30)
