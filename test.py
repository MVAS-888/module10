import pygame

# Ініціалізація Pygame
pygame.init()

# Налаштування вікна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Рух персонажа в Pygame")

# Колір
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Параметри персонажа
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

# Головний цикл гри
running = True
while running:
    pygame.time.delay(30)  # Невелика затримка для керованості
    
    # Перевірка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Отримання натиснутих клавіш
    keys = pygame.key.get_pressed()
    
    # Рух персонажа
    if keys[pygame.K_LEFT] and player_x - player_speed > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_speed < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y - player_speed > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y + player_speed < HEIGHT - player_size:
        player_y += player_speed
    
    # Оновлення екрану
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    pygame.display.update()

# Вихід з гри
pygame.quit()