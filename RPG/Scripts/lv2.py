from configs import *
from mapas import mapa1
from Player import Player, Inimigos


def sala2():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('RPG')

    # Imagens
    room = pygame.image.load('../Assets/Mapa/lv2.png')
    mesa = pygame.image.load('../Assets/Mapa/mesa2.png')
    game = True

    class Porta:
        def __init__(self):
            self.rect = pygame.Rect((523 + fx, 175 + fy), (40, 40))

        def draw(self):
            self.rect = pygame.Rect((523 + fx, 175 + fy), (40, 40))
            # pygame.draw.rect(tela, VERMELHO, self.rect, 2)

    class Mesa:
        def draw(self, scr):
            self.caracter = None
            for id_linha, linha in enumerate(mapa1):
                for id_coluna, self.caracter in enumerate(linha):
                    if self.caracter == 'm':
                        x = id_coluna * LARGURA_BLK
                        y = id_linha * ALTURA_BLK
                        scr.blit(mesa, (x, y))

    # Desenhar a tela do jogo na tela
    def tela_jogo():
        global walkCount, collideTop
        tela.fill(PRETO)
        tela.blit(room, (fx, fy))
        personagem.draw(tela)
        mesas.draw(tela)
        porta.draw()
        inimigo1.draw(tela)
        pygame.display.update()

    # Loop do Jogo
    x1 = 400
    y1 = 230
    fx = 116
    fy = 33
    porta = Porta()
    personagem = Player(x1, y1, 32, 32)
    mesas = Mesa()
    inimigo1 = Inimigos(150, 450, largura, altura, 600)

    while game:
        collideLeft = False
        collideRight = False
        collideTop = False
        collideBot = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if personagem.rect.colliderect(porta.rect):
                from corrdor import corredorf
                corredorf()
        for id_linha, linha in enumerate(mapa1):
            for id_coluna, caracter in enumerate(linha):
                if caracter == 'm':
                    x2 = id_coluna * LARGURA_BLK
                    y2 = id_linha * ALTURA_BLK
                    r = pygame.Rect((x2, y2), (LARGURA_BLK, ALTURA_BLK))
                    pygame.draw.rect(tela, VERMELHO, r, 2)
                    if r.collidepoint(personagem.rect.midleft):
                        collideLeft = True
                    if r.collidepoint(personagem.rect.midright):
                        collideRight = True
                    if r.collidepoint(personagem.rect.midtop):
                        collideTop = True
                    if r.collidepoint(personagem.rect.midbottom):
                        collideBot = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and collideLeft == False:
            personagem.x -= personagem.vel_x
            personagem.left = True
            personagem.right = False
            personagem.up = False
            personagem.down = False
        elif keys[pygame.K_RIGHT] and collideRight == False:
            personagem.x += personagem.vel_x
            personagem.right = True
            personagem.left = False
            personagem.up = False
            personagem.down = False
        elif keys[pygame.K_UP] and collideTop == False:
            personagem.y -= personagem.vel_y
            personagem.up = True
            personagem.right = False
            personagem.left = False
            personagem.down = False
        elif keys[pygame.K_DOWN] and collideBot == False:
            personagem.y += personagem.vel_y
            personagem.down = True
            personagem.right = False
            personagem.left = False
            personagem.up = False
        else:
            personagem.right = False
            personagem.left = False
            personagem.up = False
            personagem.down = False
            personagem.walkCount = 1

        tela_jogo()

        pygame.time.delay(30)


sala2()
