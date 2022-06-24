from configs import *
from Player import Player, Inimigos
from mapas import mapa6
from classes import Mesa, Itens
from pygame import mixer


def sala6():
    pygame.init()
    pygame.mixer.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('RPG')

    # Imagens
    room = pygame.image.load('../Assets/Mapa/quadra1.png')
    game = True

    # Desenhar a tela do jogo na tela
    def tela_jogo():
        global walkCount, collideTop
        tela.fill(PRETO)
        tela.blit(room, (fx, fy))
        personagem.draw(tela)
        foe1.draw(tela)
        foe2.draw(tela)
        foe4.draw(tela)
        foe5.draw(tela)
        foe7.draw(tela)
        foe9.draw(tela)
        foe10.draw(tela)
        foe11.draw(tela)
        foe12.draw(tela)
        foe13.draw(tela)
        mesas.draw(tela, mapa6, cones, personagem, 16, 16)
        foe3.draw(tela)
        foe6.draw(tela)
        foe8.draw(tela)
        k1.keyDraw(tela, personagem, keyRed, False)
        k2.keyDraw(tela, personagem, keyBlue, True)
        k3.keyDraw(tela, personagem, keyYellow, False)
        k4.keyDraw(tela, personagem, keyGreen, False)
        personagem.draw(tela)

        # chaves.keyDraw(tela, personagem)
        pygame.display.update()

    # Loop do Jogo
    x1 = 760
    y1 = 300
    fx = 0
    fy = 32
    mesas = Mesa()
    chaves = Itens(610, 335)

    foe1 = Inimigos(110, 590, largura, altura, 540, 1, 6)
    foe2 = Inimigos(80, 610, largura, altura, 540, 1, 6)
    foe3 = Inimigos(500, 110, largura, altura, 580, 0, 4)
    foe4 = Inimigos(220, 530, largura, altura, 330, 1, 6)
    foe5 = Inimigos(215, 475, largura, altura, 420, 1, 6)
    foe6 = Inimigos(340, 110, largura, altura, 420, 0, 4)
    foe7 = Inimigos(390, 412, largura, altura, 500, 1, 6)
    foe8 = Inimigos(270, 530, largura, altura, 360, 0, 4)
    foe9 = Inimigos(40, 280, largura, altura, 150, 1, 6)
    foe10 = Inimigos(350, 280, largura, altura, 470, 1, 6)
    foe11 = Inimigos(110, 210, largura, altura, 540, 1, 6)
    foe12 = Inimigos(80, 230, largura, altura, 540, 1, 6)
    foe13 = Inimigos(80, 140, largura, altura, 540, 1, 9)

    k1 = Itens(40, 200)
    k2 = Itens(40, 270)
    k3 = Itens(40, 340)
    k4 = Itens(40, 410)

    music.play()

    personagem = Player(x1, y1, 32, 32)

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if personagem.rect.colliderect(foe1.rect):
            from gameOver import gameOver
            gameOver()
            game = False
        if personagem.rect.colliderect(foe2.rect):
            from gameOver import gameOver
            gameOver()
            game = False
        if personagem.rect.colliderect(foe3.rect):
            from gameOver import gameOver
            gameOver()
            game = False
        if personagem.rect.colliderect(foe4.rect):
            from gameOver import gameOver
            gameOver()
            game = False
        if personagem.rect.colliderect(foe5.rect):
            from gameOver import gameOver
            gameOver()
            game = False
        if personagem.rect.colliderect(foe6.rect):
            from gameOver import gameOver
            gameOver()
            game = False
        if personagem.rect.colliderect(foe7.rect):
            from gameOver import gameOver
            gameOver()
            game = False
        if personagem.rect.colliderect(foe8.rect):
            from gameOver import gameOver
            gameOver()
            game = False
        if personagem.rect.colliderect(foe9.rect):
            from gameOver import gameOver
            gameOver()
            game = False
        if personagem.rect.colliderect(foe10.rect):
            from gameOver import gameOver
            gameOver()
            game = False
        if personagem.rect.colliderect(foe11.rect):
            from gameOver import gameOver
            gameOver()
            game = False
        if personagem.rect.colliderect(foe12.rect):
            from gameOver import gameOver
            gameOver()
            game = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and mesas.collideLeft == False and personagem.x >=0:
            personagem.x -= personagem.vel
            personagem.left = True
            personagem.right = False
            personagem.up = False
            personagem.down = False
        elif keys[pygame.K_RIGHT] and mesas.collideRight == False and personagem.x <= 770:
            personagem.x += personagem.vel
            chaves.x = chaves.x - vel
            personagem.right = True
            personagem.left = False
            personagem.up = False
            personagem.down = False
        elif keys[pygame.K_UP] and mesas.collideTop == False and personagem.y >= 40:
            personagem.y -= personagem.vel
            chaves.y = chaves.y + vel
            personagem.up = True
            personagem.right = False
            personagem.left = False
            personagem.down = False
        elif keys[pygame.K_DOWN] and mesas.collideBot == False and personagem.y <= 530:
            personagem.y += personagem.vel
            personagem.down = True
            personagem.right = False
            personagem.left = False
            personagem.up = False
        else:
            personagem.walkCount = 1

        tela_jogo()

        pygame.time.delay(30)
