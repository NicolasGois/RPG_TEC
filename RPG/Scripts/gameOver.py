from configs import *


def gameOver():
    pygame.init()
    gta_font = pygame.font.Font('../Fontes/gtaFont.otf', 55)
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('RPG')
    text = gta_font.render('Wasted', True, (255, 238, 47))
    text_rect = text.get_rect(center=(200, 300))
    wasted = pygame.image.load('../Assets/Mapa/wasted.png')
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        tela.blit(wasted, (0, 0))
        tela.blit(text, text_rect)
        if text_rect.x <= 325:
            text_rect.x += 1

        pygame.display.update()
        pygame.time.delay(8)