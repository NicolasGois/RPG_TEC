from configs import *
from Player import Player

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
        character.draw(tela)
        portas.draw(tela)
        pygame.display.update()

    class Porta:
        def __init__(self):
            self.hitbox = fx + 26, fy + 510, 40, 30

        def draw(self, screen):
            self.hitbox = fx + 26, fy + 510, 40, 30
            # pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    x = 390
    y = 550
    fx = 241
    fy = 21
    character = Player(x, y, 32, 32)
    portas = Porta()
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        if character.hitbox[1] < portas.hitbox[1] + portas.hitbox[3] and character.hitbox[1] + character.hitbox[3] > \
                character.hitbox[1]:
            if character.hitbox[0] + character.hitbox[2] > portas.hitbox[0] and character.hitbox[0] < portas.hitbox[
                0] + \
                    portas.hitbox[2]:
                game = False
                from roomone import sala
                sala()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and character.x >= fx + (x - x):
            character.x -= character.vel
            fx += vel
            character.left = True
            character.right = False
            character.up = False
            character.down = False
        elif keys[pygame.K_RIGHT] and character.x <= fx + 210:
            character.x += character.vel
            fx -= vel
            character.right = True
            character.left = False
            character.up = False
            character.down = False
        elif keys[pygame.K_UP] and character.y >= 10 + fy:
            character.y -= character.vel
            fy += vel
            character.up = True
            character.right = False
            character.left = False
            character.down = False
        elif keys[pygame.K_DOWN] and character.y <= fy + ALTURA_TELA - 80:
            character.y += character.vel
            fy -= vel
            character.down = True
            character.right = False
            character.left = False
            character.up = False
        else:
            character.walkCount = 0
        tela_jogo()
        pygame.time.delay(30)
corredorf()