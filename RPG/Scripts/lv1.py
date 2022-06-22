from configs import *
from mapas import mapa1
from Player import Player, Inimigos
from classes import Itens, Mesa, Porta


def sala1():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('RPG')

    # Imagens
    room = pygame.image.load('../Assets/Mapa/lv1.png')
    game = True

    # Desenhar a tela do jogo na tela
    def tela_jogo():
        global walkCount, collideTop
        tela.fill(PRETO)
        tela.blit(room, (fx, fy))
        personagem.draw(tela)
        porta.draw(tela, fx, fy)
        mesas.draw(tela, mapa1, mesa, personagem, LARGURA_BLK, ALTURA_BLK)
        pygame.display.update()

    # Loop do Jogo
    x1 = 550
    y1 = 230
    fx = 116
    fy = 33
    porta = Porta()
    personagem = Player(x1, y1, 32, 32)
    mesas = Mesa()


    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        controls(personagem, mesas)

        tela_jogo()

        pygame.time.delay(30)
