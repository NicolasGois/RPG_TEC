from configs import *
from Player import Player
from mapas import mapa5
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
        mesas.draw(tela, mapa5, cones, personagem, 16, 16)
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
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False

            controls(personagem, mesas)

            tela_jogo()

            pygame.time.delay(30)
