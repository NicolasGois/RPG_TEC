from configs import *
from Player import Player, Inimigos
from classes import Mesa, Porta, Itens
from mapas import mapa4


def sala4():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('RPG')

    # Imagens
    room = pygame.image.load('../Assets/Mapa/lv4.png')
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
        mesas.draw(tela, mapa4, mesa, personagem, LARGURA_BLK, ALTURA_BLK)
        pygame.display.update()

    # Loop do Jogo
    x1 = 400
    y1 = 230
    fx = 116
    fy = 33
    porta = Porta()
    mesas = Mesa()
    personagem = Player(x1, y1, 32, 32)
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if personagem.rect.colliderect(porta.rect):
                game = False
                from corrdor import corredorf
                corredorf()
        controls(personagem, mesas)

        tela_jogo()

        pygame.time.delay(30)
