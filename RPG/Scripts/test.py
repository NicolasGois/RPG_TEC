from configs import *

pygame.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
corredor = pygame.image.load('../Assets/c')
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

