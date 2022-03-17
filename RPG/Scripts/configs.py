LARGURA_TELA = 800
ALTURA_TELA = 600

LARGURA_BLK = LARGURA_TELA // 40
ALTURA_BLK = ALTURA_TELA // 20

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)

X = 400
Y = 300
VEL = 2

move_left = False
move_right = False
move_up = False
move_down = False

step_idx = 0
def controles():
    user_input = pygame.key.get_pressed()
    if user_input[pygame.K_d] and perso_rect.right <= 700:
        perso_rect.x += VEL
    if user_input[pygame.K_a] and perso_rect.left >= 100:
        perso_rect.x -= VEL
    if user_input[pygame.K_w] and perso_rect.top >= 245:
        perso_rect.y -= VEL
    if user_input[pygame.K_s] and perso_rect.bottom <= 600:
        perso_rect.y += VEL
