from configs import *
from mapas import mapa2
from Player import Player, Inimigos
from classes import Itens, Mesa, Porta


def sala2():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('RPG')

    # Imagens
    room = pygame.image.load('../Assets/Mapa/lv2.png')
    game = True

    # Desenhar a tela do jogo na tela
    def tela_jogo():
        global walkCount, collideTop
        tela.fill(PRETO)
        tela.blit(room, (fx, fy))
        personagem.draw(tela)
        porta.draw(tela, fx, fy)
        inimigo1.draw(tela)
        inimigo2.draw(tela)
        mesas.draw(tela, mapa2, mesa, personagem, LARGURA_BLK, ALTURA_BLK)
        chaves.keyDraw(tela, personagem)
        pygame.display.update()

    # Loop do Jogo
    x1 = 550
    y1 = 230
    fx = 116
    fy = 33
    porta = Porta()
    personagem = Player(x1, y1, 32, 32)
    mesas = Mesa()
    chaves = Itens(360, 370)
    inimigo1 = Inimigos(320, 325, largura, altura, 400)
    inimigo2 = Inimigos(320, 420, largura, altura, 400)

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if personagem.rect.colliderect(porta.rect) and chaves.keys >= 1:
                from corrdor import corredorf
                corredorf()
            if personagem.rect.colliderect(inimigo1.rect):
                from gameOver import gameOver
                gameOver()
                game = False
        controls(personagem, mesas)

        tela_jogo()

        pygame.time.delay(30)

