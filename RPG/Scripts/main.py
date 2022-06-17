from configs import *
import sys
from Player import Player, Inimigos


def entrada():
    pygame.init()
    pygame.mixer.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('RPG')
    fundo_x = 0
    fundo_y = 0

    # Classe da Porta
    class Porta:
        def __init__(self):
            self.hitbox1 = pygame.Rect((370 + fundo_x, 200 + fundo_y), (30, 40))

        def draw(self, screen):
            self.hitbox1 = pygame.Rect((370 + fundo_x, 200 + fundo_y), (30, 40))
            # pygame.draw.rect(screen, VERMELHO, self.hitbox1, 2)

    # Imagens e Sons
    pilar = pygame.image.load('../Assets/Mapa/pilares.png').convert_alpha()
    entrada = pygame.image.load('../Assets/Mapa/entrada1.png')
    px = 334
    py = 143
    running = True

    # Desenhar a tela do jogo na tela
    def tela_jogo():
        global walkCount
        tela.fill(PRETO)
        tela.blit(entrada, (fundo_x, fundo_y))
        personagem.draw(tela)
        tela.blit(pilar, (px, py))
        porta.draw(tela)
        foes.draw(tela)
        chaves.keyDraw(tela)
        pygame.display.update()
        return fundo_x, fundo_y

    # Itens

    class Itens:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.keys = 0

        def keyDraw(self, scr):
            pixelFont = pygame.font.Font('../Fontes/Pixeltype.ttf', 30)
            keyImg = pygame.image.load('../Assets/Itens/key1.png')
            keyImgRect = keyImg.get_rect(center=(self.x, self.y))
            text = pixelFont.render(f'Keys: {self.keys}', True, (255, 255, 255))
            text_rect = text.get_rect(center=(50, 50))
            scr.blit(text, text_rect)
            if keyImgRect.colliderect(personagem.rect):
                self.keys = self.keys + 1
                print(self.keys)
                self.x = 900
                self.y = 900
            else:
                scr.blit(keyImg, keyImgRect)

    # Loop do Jogo
    x = 375
    y = 490
    personagem = Player(x, y, 32, 32)
    porta = Porta()
    foes = Inimigos(e_x, e_y, largura, altura, 700)
    chaves = Itens(390, 310)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if personagem.rect.colliderect(porta.hitbox1):
            from corrdor import corredorf
            corredorf()
            chaves.keys = chaves.keys - 1

        if personagem.rect.colliderect(foes.rect):
            from gameOver import gameOver
            gameOver()
            running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and personagem.x >= fundo_x:
            personagem.x -= personagem.vel
            fundo_x += vel
            chaves.x = chaves.x + vel
            px = px + vel
            foes.x = foes.x + vel
            personagem.left = True
            personagem.right = False
            personagem.up = False
            personagem.down = False
        elif keys[pygame.K_RIGHT] and personagem.x <= LARGURA_TELA + fundo_x - largura:
            personagem.x += personagem.vel
            fundo_x -= vel
            foes.x = foes.x - vel
            chaves.x = chaves.x - vel
            px = px - vel
            personagem.right = True
            personagem.left = False
            personagem.up = False
            personagem.down = False
        elif keys[pygame.K_UP] and personagem.y >= 240 + fundo_y:
            personagem.y -= personagem.vel
            fundo_y += vel
            foes.y = foes.y + vel
            chaves.y = chaves.y + vel
            py = py + vel
            personagem.up = True
            personagem.right = False
            personagem.left = False
            personagem.down = False
        elif keys[pygame.K_DOWN] and personagem.y <= ALTURA_TELA + fundo_y - 40:
            personagem.y += personagem.vel
            fundo_y -= vel
            chaves.y = chaves.y - vel
            py = py - vel
            foes.y = foes.y - vel
            personagem.down = True
            personagem.right = False
            personagem.left = False
            personagem.up = False
        else:
            personagem.walkCount = 1
        tela_jogo()
        pygame.time.delay(30)

