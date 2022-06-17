import pygame.font

from configs import *
def menu():
	pygame.init()
	a = 400
	b = 800
	screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
	pygame.display.set_caption('School Escape')

	# images and fonts
	start_img = pygame.image.load('../Assets/startBtn.png').convert_alpha()
	credits_img = pygame.image.load('../Assets/crBtn.png').convert_alpha()
	bg = pygame.image.load('../Assets/Mapa/wasted.png')
	logo = pygame.image.load('../Assets/logo.png')

	# classe
	class Button():
		def __init__(self, x, y, img):
			self.img = img
			self.rect = self.img.get_rect()
			self.rect.center = (x, y)
			self.clicked = False

		def draw(self):
			action = False
			pos = pygame.mouse.get_pos()

			if self.rect.collidepoint(pos):
				if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
					self.clicked = True
					action = True
			if pygame.mouse.get_pressed()[0] == 0:
				self.clicked = False
			screen.blit(self.img, self.rect)

			return action
	def credits():
		game = True
		font = pygame.font.Font('../Fontes/Pixeltype.ttf', 30)
		font1 = pygame.font.Font('../Fontes/Pixeltype.ttf', 60)
		creditos = font1.render('CREDITOS', True, (255, 255, 255))
		t1 = font.render('CODIGO:  Nicolas Gois', True, (255, 255, 255))
		t1_rect = t1.get_rect(center=(400, 550))
		t2 = font.render('                                   Marcos Goncalves', True, (255, 255, 255))
		t2_rect = t2.get_rect(center=(400, 570))
		t3 = font.render('      GRAFICOS: Marcos Eduardo', True, (255, 255, 255))
		t3_rect = t3.get_rect(center=(400, 610))
		t4 = font.render('                                   Marcos Goncalves', True, (255, 255, 255))
		t4_rect = t4.get_rect(center=(400, 630))
		t5 = font.render('                    Nicolas Gois', True, (255, 255, 255))
		t5_rect = t5.get_rect(center=(400, 650))
		t6 = font.render('                PROFESSOR: Pedro Francisco Dias', True, (255, 255, 255))
		t6_rect = t6.get_rect(center=(400, 690))
		t7 = font.render('           RESPONSAVEL', True, (255, 255, 255))
		t7_rect = t7.get_rect(center=(300, 710))
		startTxt = font.render('Press <Space> to continue', True, (255, 238, 47))
		start_rect = startTxt.get_rect(center=(400, 500))

		while game:
			screen.fill(PRETO)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			screen.blit(creditos, (300, 50))
			screen.blit(t1, t1_rect)
			screen.blit(t2, t2_rect)
			screen.blit(t3, t3_rect)
			screen.blit(t4, t4_rect)
			screen.blit(t5, t5_rect)
			screen.blit(t6, t6_rect)
			screen.blit(t7, t7_rect)
			if t1_rect.y >= 110:
				t1_rect.y -= 2
			if t2_rect.y >= 130:
				t2_rect.y -= 2
			if t3_rect.y >= 170:
				t3_rect.y -= 2
			if t4_rect.y >= 190:
				t4_rect.y -= 2
			if t5_rect.y >= 210:
				t5_rect.y -= 2
			if t6_rect.y >= 250:
				t6_rect.y -= 2
			if t7_rect.y >= 270:
				t7_rect.y -= 2
			if t7_rect.y <= 270:
				screen.blit(startTxt, start_rect)

			keys = pygame.key.get_pressed()
			if keys[pygame.K_SPACE]:
				game = False
			pygame.display.update()
			pygame.time.delay(30)

	start_btn = Button(400, 400, start_img)
	credits_btn = Button(400, 500, credits_img)
	running = True

	# game loop
	while running:
		screen.blit(bg, (0, 0))
		screen.blit(logo, (135, 50))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		if start_btn.draw():
			from main import entrada
			entrada()
		if credits_btn.draw():
			credits()

			game = False
		pygame.display.update()
menu()