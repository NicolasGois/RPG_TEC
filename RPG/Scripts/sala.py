from configs import *

def sala():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('RPG')

    # Classe do Jogador
    class Player(object):
        def __init__(self, X, Y, width, height):
            self.x = X
            self.y = Y
            self.largura = width
            self.altura = height
            self.vel = vel
            self.left = False
            self.right = False
            self.up = False
            self.down = False
            self.walkCount = 0
            self.hitbox = (self.x, self.y, 32, 32)

        def draw(self, screen):
            if self.walkCount == 3:
                self.walkCount = 0
            if self.left:
                screen.blit(walkLeft[self.walkCount], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                screen.blit(walkRight[self.walkCount], (self.x, self.y))
                self.walkCount += 1
            elif self.up:
                screen.blit(walkUp[self.walkCount], (self.x, self.y))
                self.walkCount += 1
            elif self.down:
                screen.blit(walkDown[self.walkCount], (self.x, self.y))
                self.walkCount += 1
            else:
                screen.blit(parado, (self.x, self.y))
            self.hitbox = (self.x, self.y, 32, 32)
            # pygame.draw.rect(tela, (255, 0, 0), self.hitbox, 2)

    class Porta:
        def __init__(self):
            self.hitbox = 605 + fundo_x, 175 + fundo_y, 38, 40

        def draw(self, screen):
            self.hitbox = 605 + fundo_x, 175 + fundo_y, 40, 40
            pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    # Imagens
    parado = pygame.image.load('../Assets/Personagens/S1.png')
    room = pygame.image.load('../Assets/Mapa/sala.png')

    game = True

    # Desenhar a tela do jogo na tela
    def tela_jogo():
        global walkCount
        tela.fill(PRETO)
        tela.blit(room, (fundo_x, fundo_y))
        personagem.draw(tela)
        porta.draw(tela)
        pygame.display.update()

    # Loop do Jogo
    x = 400
    y = 230
    fundo_x = 50
    fundo_y = 37
    porta = Porta()
    personagem = Player(x, y, 32, 32)
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if personagem.hitbox[1] < porta.hitbox[1] + porta.hitbox[3] and personagem.hitbox[1] + personagem.hitbox[
                3] > \
                    personagem.hitbox[1]:
                if personagem.hitbox[0] + personagem.hitbox[2] > porta.hitbox[0] and personagem.hitbox[0] < \
                        porta.hitbox[0] + \
                        porta.hitbox[2]:
                    game = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and personagem.x >= fundo_x + 87:
            personagem.x -= personagem.vel
            fundo_x += vel
            personagem.left = True
            personagem.right = False
            personagem.up = False
            personagem.down = False
        elif keys[pygame.K_RIGHT] and personagem.x <= fundo_x + 570:
            personagem.x += personagem.vel
            fundo_x -= vel
            personagem.right = True
            personagem.left = False
            personagem.up = False
            personagem.down = False
        elif keys[pygame.K_UP] and personagem.y >= 170 + fundo_y:
            personagem.y -= personagem.vel
            fundo_y += vel
            personagem.up = True
            personagem.right = False
            personagem.left = False
            personagem.down = False
        elif keys[pygame.K_DOWN] and personagem.y <= fundo_y + ALTURA_TELA - 74 - 40:
            personagem.y += personagem.vel
            fundo_y -= vel
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
sala()