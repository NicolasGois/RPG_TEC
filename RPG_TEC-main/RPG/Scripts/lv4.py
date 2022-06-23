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

    # Desenhar a tela do jogo na tela
    def tela_jogo():
        global walkCount, collideTop
        tela.fill(PRETO)
        tela.blit(room, (fx, fy))
        personagem.draw(tela)
        porta.draw(tela, fx, fy)
        foe1.draw(tela)
        k1.keyDraw(tela, personagem, keyRed, False)
        k2.keyDraw(tela, personagem, keyBlue, True)
        k3.keyDraw(tela, personagem, keyYellow, False)
        k4.keyDraw(tela, personagem, keyGreen, False)
        mesas.draw(tela, mapa4, mesa, personagem, LARGURA_BLK, ALTURA_BLK)
        foe2.draw(tela)
        foe3.draw(tela)
        pygame.display.update()

    # Loop do Jogo
    x1 = 600
    y1 = 220
    fx = 116
    fy = 33
    porta = Porta()
    mesas = Mesa()
    foe1 = Inimigos(300, 230, largura, altura, 420)
    foe2 = Inimigos(300, 470, largura, altura, 420)
    foe3 = Inimigos(200, 340, largura, altura, 525)
    k1 = Itens(365, 370)
    k2 = Itens(365, 450)
    k3 = Itens(230,370)
    k4 = Itens(525,370)

    personagem = Player(x1, y1, 32, 32)

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        controls(personagem, mesas)
        if personagem.rect.colliderect(porta.rect) and k2.keys >= 1:
            game = False
            from corrdor import corredorf
            corredorf()
        if personagem.rect.colliderect(foe1.rect):
            from gameOver import gameOver
            gameOver()
            game = False
        if personagem.rect.colliderect(foe2.rect):
            from gameOver import gameOver
            gameOver()
            game = False

        tela_jogo()

        pygame.time.delay(30)
