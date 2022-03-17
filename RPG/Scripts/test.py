import pygame

from mapas import mapa
from configs import *

pygame.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
entrada = pygame.image.load('../Assets/Mapa/entrada.png')

def carregar_img(image_set, x, y):
    img_orig = image_set.subsurface((x, y), (16, 16))
    img_scale = pygame.transform.scale(img_orig, (LARGURA_BLK, ALTURA_BLK))
    return img_scale


def carregar_car(image_set, x, y):
    img_orig = image_set.subsurface((x, y), (16, 16))
    img_scale = pygame.transform.scale(img_orig, (32, 32))
    return img_scale


step_idx = 0


def draw():
    global step_idx
    tela.blit(entrada, (0, 0))
    if step_idx >= 3:
        step_idx = 0
    if move_down:
        tela.blit(down[step_idx], (X, Y))
        step_idx += 1
    else:
        tela.blit(parado, (X, Y))


tiles = pygame.image.load('../Assets/Mapa/basictiles.png')
tile_grama = carregar_img(tiles, 16, 128)
tile_parede = carregar_img(tiles, 48, 0)

personagens = pygame.image.load('../Assets/Personagens/characters.png').convert_alpha()
parado = carregar_car(personagens, 96, 0)
down_1 = carregar_car(personagens, 112, 0)
down_2 = carregar_car(personagens, 128, 0)
down_3 = carregar_car(personagens, 96, 0)
down = [down_1, down_2, down_3]

up1 = carregar_car(personagens, 96, 48)
up2 = carregar_car(personagens, 112, 48)
up3 = carregar_car(personagens, 128, 48)
up = [up1, up2, up3]
escola = pygame.image.load('../Assets/Mapa/escola.png').convert_alpha()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        draw()
        user_input = pygame.key.get_pressed()

        if user_input[pygame.K_d]:
            X += VEL
            move_right = True
        if user_input[pygame.K_a]:
            X -= VEL
            move_left = True
        if user_input[pygame.K_w]:
            Y -= VEL
            move_up = True
        if user_input[pygame.K_s]:
            Y += VEL
            move_down = True
        else:
            move_left = False
            move_right = False
            move_up = False
            move_down = False
            step_idx = 0
    pygame.display.update()
    clock.tick(60)
