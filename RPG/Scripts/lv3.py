from configs import *
from Player import Player, Inimigos


def sala3():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('RPG')

    # Imagens
    room = pygame.image.load('../Assets/Mapa/lv3.png')
    game = True

    class Porta:
        def __init__(self):
            self.rect = pygame.Rect((523 + fx, 175 + fy), (40, 40))

        def draw(self):
            self.rect = pygame.Rect((523 + fx, 175 + fy), (40, 40))
            pygame.draw.rect(tela, VERMELHO, self.rect, 2)


    # Desenhar a tela do jogo na tela
    def tela_jogo():
        global walkCount, collideTop
        tela.fill(PRETO)
        tela.blit(room, (fx, fy))
        personagem.draw(tela)
        porta.draw()
        inimigo.draw(tela)
        pygame.display.update()

    # Loop do Jogo
    x1 = 400
    y1 = 230
    fx = 116
    fy = 33
    porta = Porta()
    personagem = Player(x1, y1, 32, 32)
    inimigo = Inimigos(e_x, e_y, largura, altura, 700)

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if personagem.rect.colliderect(porta.rect):
                from corrdor import corredorf
                corredorf()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            personagem.x -= personagem.vel
            personagem.left = True
            personagem.right = False
            personagem.up = False
            personagem.down = False
        elif keys[pygame.K_RIGHT]:
            personagem.x += personagem.vel
            personagem.right = True
            personagem.left = False
            personagem.up = False
            personagem.down = False
        elif keys[pygame.K_UP]:
            personagem.y -= personagem.vel
            personagem.up = True
            personagem.right = False
            personagem.left = False
            personagem.down = False
        elif keys[pygame.K_DOWN]:
            personagem.y += personagem.vel
            personagem.down = True
            personagem.right = False
            personagem.left = False
            personagem.up = False
        else:
            personagem.right = False
            personagem.left = False
            personagem.up = False
            personagem.down = False
            personagem.walkCount = 1

        tela_jogo()

        pygame.time.delay(30)
