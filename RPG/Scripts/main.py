from configs import *
from sala import sala
from gameOver import gameOver

pygame.init()
# icone = pygame.image.load('../Assets/R.ico')
clock = pygame.time.Clock()
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('RPG')
# pygame.display.set_icon(icone)
gta_font = pygame.font.Font('../Fontes/gtaFont.otf', 55)


# Classe do Jogador
class Player(object):
    def __init__(self, X, Y, width, height):
        self.x = X
        self.y = Y
        self.largura = width
        self.altura = height
        self.vel = vel
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.hitbox = (self.x, self.y, 32, 32)

    def draw(self, screen):
        if self.walkCount == 3:
            self.walkCount = 0
        if self.left:
            screen.blit(walkLeft[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            screen.blit(walkRight[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        elif self.up:
            screen.blit(walkUp[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        elif self.down:
            screen.blit(walkDown[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        else:
            screen.blit(parado, (self.x, self.y))
        self.hitbox = (self.x, self.y, 32, 32)
        # pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)


# Classe Inimigo
class Inimigos(object):
    def __init__(self, a, b, width, height, end):
        self.x = a
        self.y = b
        self.width = width
        self.height = height
        self.end = end
        self.path = [a, end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x, self.y, 32, 32)

    def draw(self, win):
        self.movimento()
        if self.walkCount == 3:
            self.walkCount = 0
        if self.vel > 0:
            win.blit(walkRightE[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(walkLeftE[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x, self.y, 32, 32)
        # pygame.draw.rect(tela, (255, 0, 0), self.hitbox, 2)

    def movimento(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1] + fundo_x:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0


# Classe da Porta
class Porta:
    def __init__(self):
        self.hitbox = fundo_x + 370, fundo_y + 200, 30, 40

    def draw(self):
        self.hitbox = fundo_x + 370, fundo_y + 200, 30, 40
        # pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)


# Imagens
parado = pygame.image.load('../Assets/Personagens/S1.png')
pilar = pygame.image.load('../Assets/Mapa/pilares.png').convert_alpha()
entrada = pygame.image.load('../Assets/Mapa/entrada1.png')
sala_img = pygame.image.load('../Assets/Mapa/sala.png')

running = True


# Desenhar a tela do jogo na tela
def tela_jogo():
    global walkCount
    tela.fill(PRETO)
    tela.blit(entrada, (fundo_x, fundo_y))
    personagem.draw(tela)
    porta.draw()
    foes.draw(tela)
    pygame.display.update()
    return fundo_x, fundo_y


# Diálogos e história
def caixa_de_texto():
    pass


# Itens
def chaves():
    pass


# Loop do Jogo
personagem = Player(x, y, 32, 32)
porta = Porta()
foes = Inimigos(e_x, e_y, largura, altura, 700)
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

    if personagem.hitbox[1] < foes.hitbox[1] + foes.hitbox[3] and personagem.hitbox[1] + personagem.hitbox[3] > \
            foes.hitbox[1]:
        if personagem.hitbox[0] + personagem.hitbox[2] > foes.hitbox[0] and personagem.hitbox[0] < foes.hitbox[0] + \
                foes.hitbox[2]:
            gameOver()
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and personagem.x >= fundo_x:
        personagem.x -= personagem.vel
        fundo_x += vel
        foes.x = foes.x + vel
        personagem.left = True
        personagem.right = False
        personagem.up = False
        personagem.down = False
    elif keys[pygame.K_RIGHT] and personagem.x <= LARGURA_TELA + fundo_x - largura:
        personagem.x += personagem.vel
        fundo_x -= vel
        foes.x = foes.x - vel
        personagem.right = True
        personagem.left = False
        personagem.up = False
        personagem.down = False
    elif keys[pygame.K_UP] and personagem.y >= 240 + fundo_y:
        personagem.y -= personagem.vel
        fundo_y += vel
        foes.y = foes.y + vel
        personagem.up = True
        personagem.right = False
        personagem.left = False
        personagem.down = False
    elif keys[pygame.K_DOWN] and personagem.y <= ALTURA_TELA + fundo_y - 40:
        personagem.y += personagem.vel
        fundo_y -= vel
        foes.y = foes.y - vel
        personagem.down = True
        personagem.right = False
        personagem.left = False
        personagem.up = False
    else:
        personagem.right = False
        personagem.left = False
        personagem.up = False
        personagem.down = False
        personagem.walkCount = 0
    tela_jogo()
    pygame.time.delay(30)
