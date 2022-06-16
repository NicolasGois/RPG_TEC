from configs import *

class Porta:
    def __init__(self):
        self.rect = pygame.Rect((523 + y, 175 + x), (40, 40))

    def draw(self, scr, x, y):
        self.rect = pygame.Rect((523 + x, 175 + y), (40, 40))
        # pygame.draw.rect(scr, VERMELHO, self.rect, 2)


class Itens:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.keys = 0

    def keyDraw(self, scr, psg):
        pixelFont = pygame.font.Font('../Fontes/Pixeltype.ttf', 30)
        keyImg = pygame.image.load('../Assets/Itens/key1.png')
        keyImgRect = keyImg.get_rect(center=(self.x, self.y))
        text = pixelFont.render(f'Keys: {self.keys}', True, (255, 255, 255))
        text_rect = text.get_rect(center=(50, 50))
        scr.blit(text, text_rect)
        if keyImgRect.colliderect(psg.rect):
            self.keys = self.keys + 1
            print(self.keys)
            self.x = 900
            self.y = 900
        else:
            scr.blit(keyImg, keyImgRect)

class Mesa:
    def draw(self, scr, mapa, img, psg, width, height):
        self.caracter = None
        self.collideLeft = False
        self.collideRight = False
        self.collideTop = False
        self.collideBot = False
        for id_linha, linha in enumerate(mapa):
            for id_coluna, self.caracter in enumerate(linha):
                if self.caracter == 'm':
                    self.x = id_coluna * width
                    self.y = id_linha * height
                    scr.blit(img, (self.x, self.y))


        for id_linha, linha in enumerate(mapa):
            for id_coluna, caracter in enumerate(linha):
                if caracter == 'm':
                    self.x2 = id_coluna * width
                    self.y2 = id_linha * height
                    r = pygame.Rect((self.x2, self.y2), (width, height))
                    # pygame.draw.rect(scr, VERMELHO, r, 2)
                    if r.collidepoint(psg.rect.midleft):
                        self.collideLeft = True
                    if r.collidepoint(psg.rect.midright):
                        self.collideRight = True
                    if r.collidepoint(psg.rect.midtop):
                        self.collideTop = True
                    if r.collidepoint(psg.rect.midbottom):
                        self.collideBot = True

