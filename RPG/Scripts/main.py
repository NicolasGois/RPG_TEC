import pygame
from mapas import mapa
from configs import *

pygame.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))


def carregar_img(image_set, x, y):
    img_orig = image_set.subsurface((x, y), (16, 16))
    img_scale = pygame.transform.scale(img_orig, (LARGURA_BLK, ALTURA_BLK))
    return img_scale


tiles = pygame.image.load('../Assets/Mapa/basictiles.png')
tile_grama = carregar_img(tiles, 16, 128)
tile_parede = carregar_img(tiles, 48, 0)

escola = pygame.image.load('../Assets/Mapa/escola.png').convert_alpha()

for id_linha, linha in enumerate(mapa):
    for id_coluna, caracter in enumerate(linha):
        x = id_coluna * LARGURA_BLK
        y = id_linha * ALTURA_BLK
        tela.blit(escola, (0, 0))
        if caracter == 'p':
            tela.blit(tile_grama, (x, y))
        else:
            tela.blit(tile_parede, (x, y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                X += VEL
    pygame.display.update()
    clock.tick(60)
