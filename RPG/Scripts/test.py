import pygame

from configs import *

pygame.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

sala = pygame.image.load('../Assets/Mapa/sala.png')

personagem = pygame.image.load('../Assets/Personagens/S1.png').convert_alpha()
personagem = pygame.transform.scale(personagem, (32, 32))
perso_rect = personagem.get_rect(center=(X, Y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    tela.blit(sala, (0, 0))
    tela.blit(personagem, perso_rect)
    user_input = pygame.key.get_pressed()
    if user_input[pygame.K_d] and perso_rect.right <= 700:
        perso_rect.x += vel
    if user_input[pygame.K_a] and perso_rect.left >= 100:
        perso_rect.x -= vel
    if user_input[pygame.K_w] and perso_rect.top >= 245:
        perso_rect.y -= vel
    if user_input[pygame.K_s] and perso_rect.bottom <= 600:
        perso_rect.y += vel
    pygame.display.update()
    clock.tick(60)
