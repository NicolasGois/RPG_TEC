from configs import *
from Player import Player, Inimigos
from mapas import mapa3
from classes import Mesa, Itens, Porta


def sala3():
    pygame.init()
    music = pygame.mixer.Sound('../Sons/musica.mp3')
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('RPG')

    # Imagens
    room = pygame.image.load('../Assets/Mapa/lv3.png')
    game = True

    # Desenhar a tela do jogo na tela
    def tela_jogo():
        tela.fill(PRETO)
        tela.blit(room, (fx, fy))
        personagem.draw(tela)
        porta.draw(tela, fx, fy)
        mesas.draw(tela, mapa3, mesa, personagem, LARGURA_BLK, ALTURA_BLK)
        chave1.keyDraw(tela, personagem, keyRed, True)
        chave2.keyDraw(tela, personagem, keyGreen, False)
        chave3.keyDraw(tela, personagem, keyBlue, False)
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
    chave1 = Itens(610, 335)
    chave2 = Itens(150, 400)
    chave3 = Itens(610, 460)
    music.play()
    personagem = Player(x1, y1, 32, 32)
    inimigo1 = Inimigos(cx, cy, largura, altura, 610, 0, 6)
    inimigo2 = Inimigos(cx1, cy1, largura, altura, 610, 0, 6)


    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if personagem.rect.colliderect(porta.rect) and chave1.keys >= 1:
            from corrdor import corredorf
            corredorf()
            game = False
        if personagem.rect.colliderect(inimigo1.rect):
            from gameOver import gameOver
            gameOver()
            game = False
        if personagem.rect.colliderect(inimigo2.rect):
            from gameOver import gameOver
            gameOver()
            game = False

        controls(personagem, mesas)

        tela_jogo()

        pygame.time.delay(30)
