import pygame.font

from configs import *
def menu():
	pygame.init()
	screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
	pygame.display.set_caption('School Escape')
	bg = pygame.image.load('../Assets/winScr.png')
	logo = pygame.image.load('../Assets/logo.png')
	pixelFont = pygame.font.Font('../Fontes/Pixeltype.ttf', 30)
	vicFont = pygame.font.Font('../Fontes/The Victory.ttf', 75)
	text = vicFont.render('VITÓRIA', True, (255, 238, 47))
	text_rect = text.get_rect(center=(200, 350))
	startTxt = pixelFont.render('Press <Space> to continue', True, (255, 238, 47))
	start_rect = startTxt.get_rect(center=(400, 500))

	running = True

	# game loop
	while running:
		screen.blit(bg, (0, 0))
		screen.blit(logo, (135, 50))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.blit(text, text_rect)

		if text_rect.centerx <= 400:
			text_rect.centerx += 1
		else:
			screen.blit(startTxt, start_rect)
			game = False
		pygame.display.update()
menu()