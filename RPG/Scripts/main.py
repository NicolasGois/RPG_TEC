from configs import *
from sala import sala
pygame.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('RPG')


# Classe do Jogador
class Player(object):
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.vel = vel
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.hitbox = (self.x, self.y, 32, 32)

    def draw(self, tela):
        if self.walkCount == 3:
            self.walkCount = 0
        if self.left:
            tela.blit(walkLeft[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            tela.blit(walkRight[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        elif self.up:
            tela.blit(walkUp[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        elif self.down:
            tela.blit(walkDown[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        else:
            tela.blit(parado, (self.x, self.y))
        self.hitbox = (self.x, self.y, 32, 32)
        # pygame.draw.rect(tela, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        print('collide')


# Classe da Porta
class Porta:
    def __init__(self):
        self.hitbox = 357, 178, 58, 66

    def draw(self, tela):
        self.hitbox = 357, 178, 58, 66
        # pygame.draw.rect(tela, (255, 0, 0), self.hitbox, 2)


# Imagens
parado = pygame.image.load('../Assets/Personagens/S1.png')
pilar = pygame.image.load('../Assets/Mapa/pilares.png').convert_alpha()
entrada = pygame.image.load('../Assets/Mapa/entrada.png')
sala_img = pygame.image.load('../Assets/Mapa/sala.png')

running = True


# Desenhar a tela do jogo na tela
def tela_jogo():
    global walkCount
    tela.blit(entrada, (0, 0))
    personagem.draw(tela)
    porta.draw(tela)
    pygame.display.update()


# Loop do Jogo
personagem = Player(x, y, 32, 32)
porta = Porta()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if personagem.hitbox[1] < porta.hitbox[1] + porta.hitbox[3] and personagem.hitbox[1] + personagem.hitbox[3] > \
            personagem.hitbox[1]:
        if personagem.hitbox[0] + personagem.hitbox[2] > porta.hitbox[0] and personagem.hitbox[0] < porta.hitbox[0] + \
                porta.hitbox[2]:
            sala()
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        personagem.x -= personagem.vel
        personagem.left = True
    elif keys[pygame.K_RIGHT]:
        personagem.x += personagem.vel
        personagem.right = True
    elif keys[pygame.K_UP]:
        personagem.y -= personagem.vel
        personagem.up = True
    elif keys[pygame.K_DOWN]:
        personagem.y += personagem.vel
        personagem.down = True
    else:
        personagem.right = False
        personagem.left = False
        personagem.up = False
        personagem.down = False
        personagem.walkCount = 0
    tela_jogo()
    pygame.time.delay(30)
