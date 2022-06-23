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
        tela.fill(PRETO)
        tela.blit(room, (fx, fy))
        personagem.draw(tela)
        porta.draw(tela, fx, fy)
        k1.keyDraw(tela, personagem, keyYellow, True)
        k2.keyDraw(tela, personagem, keyRed, False)
        foe1.draw(tela)
        mesas.draw(tela, mapa1, mesa, personagem, LARGURA_BLK, ALTURA_BLK)
        foe2.draw(tela)
        pygame.display.update()

    # Loop do Jogo
    x1 = 550
    y1 = 230
    fx = 116
    fy = 33
    porta = Porta()
    personagem = Player(x1, y1, 32, 32)
    k1 = Itens(320, 360)
    k2 = Itens(420, 360)
    foe1 = Inimigos(250, 230, largura, altura, 460, 0, 6)
    foe2 = Inimigos(250, 470, largura, altura, 460, 0, 6)
    mesas = Mesa()


    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if personagem.rect.colliderect(porta.rect) and k1.keys >= 1:
            from corrdor import corredorf
            corredorf()
        if personagem.rect.colliderect(foe1.rect):
            from gameOver import gameOver
            gameOver()
        if personagem.rect.colliderect(foe2.rect):
            from gameOver import gameOver
            gameOver()
        controls(personagem, mesas)
        tela_jogo()

        pygame.time.delay(30)
