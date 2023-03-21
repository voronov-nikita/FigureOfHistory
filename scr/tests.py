import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение размеров экрана
screen_width = 500
screen_height = 500

# Создание окна
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Движущиеся квадраты')

# Определение параметров первого квадрата
square_size = 100
square_x = 100
square_y = 100
square_color = (255, 0, 0)
square_speed = 0.1

# Определение параметров второго квадрата
other_square_size = 100
other_square_x = 200
other_square_y = 50
other_square_color = (0, 255, 0)

# Основной игровой цикл
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Движение квадратов
    square_x += square_speed
    other_square_x -= square_speed

    # Очистка экрана
    screen.fill((255, 255, 255))

    # Отрисовка первого квадрата
    square_surface = pygame.Surface((square_size, square_size))
    square_surface.fill(square_color)
    square_rect = square_surface.get_rect()
    square_rect.x = square_x
    square_rect.y = square_y
    screen.blit(square_surface, square_rect)

    # Отрисовка второго квадрата
    other_square_surface = pygame.Surface((other_square_size, other_square_size))
    other_square_surface.fill(other_square_color)
    other_square_rect = other_square_surface.get_rect()
    other_square_rect.x = other_square_x
    other_square_rect.y = other_square_y
    screen.blit(other_square_surface, other_square_rect)

    # Проверка столкновения квадратов
    if square_rect.colliderect(other_square_rect):
        # Если столкновение произошло, то удаляем первый квадрат
        screen.fill((255, 255, 255), square_rect)

    # Обновление экрана
    pygame.display.update()
