from configs import *
from Player import Player
from mapas import mapa6
from classes import Mesa, Itens


def lv6():
    pygame.init()
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
        mesas.draw(tela, mapa6, cones, personagem, 16, 16)
        personagem.draw(tela)
        # chaves.keyDraw(tela, personagem)
        pygame.display.update()

    # Loop do Jogo
    x1 = 750
    y1 = 50
    fx = 0
    fy = 32
    mesas = Mesa()
    chaves = Itens(610, 335)
    personagem = Player(x1, y1, 32, 32)

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            personagem.x -= personagem.vel
            personagem.left = True
            personagem.right = False
            personagem.up = False
            personagem.down = False
        elif keys[pygame.K_RIGHT]:
            personagem.x += personagem.vel
            chaves.x = chaves.x - vel
            personagem.right = True
            personagem.left = False
            personagem.up = False
            personagem.down = False
        elif keys[pygame.K_UP]:
            personagem.y -= personagem.vel
            chaves.y = chaves.y + vel
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
            personagem.walkCount = 1

        tela_jogo()

        pygame.time.delay(30)