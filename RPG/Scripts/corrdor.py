from configs import *
from Player import Player
from sala import sala

def corredorf():
    pygame.init()
    corredor = pygame.image.load('../Assets/Mapa/corredor.png')
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('RPG')
    game = True

    def tela_jogo():
        global walkCount
        tela.fill(PRETO)
        tela.blit(corredor, (fx, fy))
        personagem.draw(tela)
        portas.draw(tela)
        pygame.display.update()

    class Porta:
        def __init__(self):
            self.hitbox = fx + 26, fy + 510, 40, 30

        def draw(self, screen):
            self.hitbox = fx + 26, fy + 510, 40, 30
            pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    x = 390
    y = 550
    fx = 241
    fy = 21
    personagem = Player(x, y, 32, 32)
    portas = Porta()
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        keys = pygame.key.get_pressed()

        if personagem.hitbox[1] < portas.hitbox[1] + portas.hitbox[3] and personagem.hitbox[1] + personagem.hitbox[3] > \
                personagem.hitbox[1]:
            if personagem.hitbox[0] + personagem.hitbox[2] > portas.hitbox[0] and personagem.hitbox[0] < portas.hitbox[
                0] + \
                    portas.hitbox[2]:
                game = False
                sala()

        if keys[pygame.K_LEFT] and personagem.x >= fx + 70:
            personagem.x -= personagem.vel
            fx += vel
            personagem.left = True
            personagem.right = False
            personagem.up = False
            personagem.down = False
        elif keys[pygame.K_RIGHT] and personagem.x <= fx + 210:
            personagem.x += personagem.vel
            fx -= vel
            personagem.right = True
            personagem.left = False
            personagem.up = False
            personagem.down = False
        elif keys[pygame.K_UP] and personagem.y >= 10 + fy:
            personagem.y -= personagem.vel
            fy += vel
            personagem.up = True
            personagem.right = False
            personagem.left = False
            personagem.down = False
        elif keys[pygame.K_DOWN] and personagem.y <= fy + ALTURA_TELA - 80:
            personagem.y += personagem.vel
            fy -= vel
            personagem.down = True
            personagem.right = False
            personagem.left = False
            personagem.up = False
        else:
            personagem.right = False
            personagem.left = False
            personagem.up = False
            personagem.down = False
            personagem.walkCount = 0
        tela_jogo()
        pygame.time.delay(30)
