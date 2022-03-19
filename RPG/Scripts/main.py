import pygame
from configs import *

pygame.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))


def carregar_img(image_set, x, y):
    img_orig = image_set.subsurface((x, y), (16, 16))
    img_scale = pygame.transform.scale(img_orig, (LARGURA_BLK, ALTURA_BLK))
    return img_scale


personagem = pygame.image.load('../Assets/Personagens/S1.png').convert_alpha()
personagem = pygame.transform.scale(personagem, (32, 32))
perso_rect = personagem.get_rect(center=(X, Y))

tiles = pygame.image.load('../Assets/Mapa/basictiles.png')
tile_grama = carregar_img(tiles, 16, 128)
tile_parede = carregar_img(tiles, 48, 0)
escola = pygame.image.load('../Assets/Mapa/escola.png').convert_alpha()
entrada = pygame.image.load('../Assets/Mapa/entrada.png')
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    tela.blit(entrada, (0, 0))
    tela.blit(personagem, perso_rect)
    user_input = pygame.key.get_pressed()
    if user_input[pygame.K_d] and perso_rect.right <= 700:
        perso_rect.x += VEL
    if user_input[pygame.K_a] and perso_rect.left >= 100:
        perso_rect.x -= VEL
    if user_input[pygame.K_w] and perso_rect.top >= 245:
        perso_rect.y -= VEL
    if user_input[pygame.K_s] and perso_rect.bottom <= 600:
        perso_rect.y += VEL

    pygame.time.delay(10)
    pygame.display.update()
