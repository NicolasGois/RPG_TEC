from configs import *


def sala():
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

    # Imagens
    parado = pygame.image.load('../Assets/Personagens/S1.png')
    sala = pygame.image.load('../Assets/Mapa/sala.png')

    running = True

    # Desenhar a tela do jogo na tela
    def tela_jogo():
        global walkCount
        tela.blit(sala, (0, 0))
        personagem.draw(tela)
        pygame.display.update()

    # Loop do Jogo
    x = 300
    y = 400
    personagem = Player(x, y, 32, 32)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
