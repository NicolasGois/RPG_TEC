from pygame import mixer
from lv1 import *

def gameOver():
    pygame.init()
    pygame.mixer.init()
    gta_font = pygame.font.Font('../Fontes/gtaFont.otf', 55)
    pixelFont = pygame.font.Font('../Fontes/Pixeltype.ttf', 30)
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('RPG')
    text = gta_font.render('Wasted', True, (255, 238, 47))
    text_rect = text.get_rect(center=(200, 300))
    startTxt = pixelFont.render('Press <Space> to continue', True, (255, 238, 47))
    start_rect = startTxt.get_rect(center=(400, 500))
    wasted = pygame.image.load('../Assets/Mapa/wasted.png')
    deathSound = mixer.Sound('../Sons/deathSound.mp3')
    deathSound.play()
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        tela.blit(wasted, (0, 0))
        tela.blit(text, text_rect)

        if text_rect.centerx <= 400:
            text_rect.centerx += 1
        else:
            tela.blit(startTxt, start_rect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            import main
            main.running = True
            game = False
        pygame.display.update()
        pygame.time.delay(8)
