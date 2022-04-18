# Váriaveis e constantes usadas no jogo

import pygame

LARGURA_TELA = 800
ALTURA_TELA = 600

PRETO = (0, 0, 0)

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