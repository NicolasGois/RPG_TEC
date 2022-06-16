from configs import *
from Player import Player, Inimigos
from mapas import mapa3
from classes import Mesa, Itens, Porta


def sala3():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('RPG')

    # Imagens
    room = pygame.image.load('../Assets/Mapa/lv3.png')
    game = True

    # Desenhar a tela do jogo na tela
    def tela_jogo():
        global walkCount, collideTop
        tela.fill(PRETO)
        tela.blit(room, (fx, fy))
        personagem.draw(tela)
        porta.draw(tela, fx, fy)
        mesas.draw(tela, mapa3, mesa, personagem, LARGURA_BLK, ALTURA_BLK)
        chaves.keyDraw(tela, personagem)
        inimigo1.draw(tela)
        inimigo2.draw(tela)
        pygame.display.update()

    # Loop do Jogo
    x1 = 400
    y1 = 230

    fx = 116
    fy = 33
    cx = 125
    cy = 370
    cx1 = 380
    cy1 = 315
    porta = Porta()
    mesas = Mesa()
    chaves = Itens(610, 335)
    personagem = Player(x1, y1, 32, 32)
    inimigo1 = Inimigos(cx, cy, largura, altura, 610)
    inimigo2 = Inimigos(cx1, cy1, largura, altura, 610)

    while game:
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if personagem.rect.colliderect(porta.rect) and chaves.keys >= 1:
                    game = False
                    from corrdor import corredorf
                    corredorf()
            if personagem.rect.colliderect(inimigo1.rect and inimigo2.rect):
                from gameOver import gameOver
                gameOver()
                game = False

            controls(personagem, mesas)

            tela_jogo()

            pygame.time.delay(30)
sala3()