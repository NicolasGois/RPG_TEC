from configs import *
from Player import Player, Inimigos
from mapas import mapa5
from classes import Mesa, Itens, Porta


def sala5():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('RPG')

    # Imagens
    room = pygame.image.load('../Assets/Mapa/lv4.png')
    game = True

    # Desenhar a tela do jogo na tela
    def tela_jogo():
        global walkCount, collideTop
        tela.fill(PRETO)
        tela.blit(room, (fx, fy))
        personagem.draw(tela)
        porta.draw(tela, fx, fy)
        foe1.draw(tela)
        mesas.draw(tela, mapa5, mesa, personagem, LARGURA_BLK, ALTURA_BLK)
        k1.keyDraw(tela, personagem, keyRed, False)
        k2.keyDraw(tela, personagem, keyBlue, False)
        k3.keyDraw(tela, personagem, keyYellow, False)
        k4.keyDraw(tela, personagem, keyGreen, True)
        foe2.draw(tela)
        pygame.display.update()

    # Loop do Jogo
    x1 = 400
    y1 = 230

    fx = 116
    fy = 33

    porta = Porta()
    mesas = Mesa()
    chaves = Itens(610, 335)
    personagem = Player(x1, y1, 32, 32)
    k1 = Itens(310, 495)
    k2 = Itens(550, 465)
    k3 = Itens(190, 370)
    k4 = Itens(470, 425)
    foe1 = Inimigos(160, 280, largura, altura, 200)
    foe2 = Inimigos(260, 420, largura, altura, 400)

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


sala5()
