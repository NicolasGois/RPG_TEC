# Váriaveis e constantes usadas no jogo

import pygame
import sys

LARGURA_BLK = 32
ALTURA_BLK = 32
LARGURA_TELA = 800
ALTURA_TELA = 600

PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

x = 300
y = 490
vel = 7


largura = 32
altura = 32

e_x = 100
e_y = 400
fundo_x = 0
fundo_y = 0

move_left = False
move_right = False
move_up = False
move_down = False

step_idx = 0
parado = pygame.image.load('../Assets/Personagens/S1.png')

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

walkRightE = [pygame.image.load('../Assets/Personagens/ER1.png'),
             pygame.image.load('../Assets/Personagens/ER2.png'),
             pygame.image.load('../Assets/Personagens/ER3.png')]

walkLeftE = [pygame.image.load('../Assets/Personagens/EL1.png'),
            pygame.image.load('../Assets/Personagens/EL2.png'),
            pygame.image.load('../Assets/Personagens/EL3.png')]

mesa = pygame.image.load('../Assets/Mapa/mesa2.png')
cones = pygame.image.load('../Assets/Mapa/cones.png')
keyCatch = False

def controls(psg, object):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and object.collideLeft == False and psg.x >= 123:
            psg.x -= psg.vel
            psg.left = True
            psg.right = False
            psg.up = False
            psg.down = False
        elif keys[pygame.K_RIGHT] and object.collideRight == False and psg.x <= 610:
            psg.x += psg.vel
            psg.right = True
            psg.left = False
            psg.up = False
            psg.down = False
        elif keys[pygame.K_UP] and object.collideTop == False and psg.y >= 197:
            psg.y -= psg.vel
            psg.up = True
            psg.right = False
            psg.left = False
            psg.down = False
        elif keys[pygame.K_DOWN] and object.collideBot == False and psg.y <= 510:
            psg.y += psg.vel
            psg.down = True
            psg.right = False
            psg.left = False
            psg.up = False
        else:
            psg.walkCount = 1