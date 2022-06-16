import pygame.font

from configs import *

pygame.init()

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
	font = pygame.font.Font('../Fontes/Pixeltype.ttf', 30)
	t1 =
	text_rect = t1.get_rect(center=(400, 550))
	while True:
		screen.fill(PRETO)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.blit(text, text_rect)
		pygame.display.update()

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

	pygame.display.update()