import pygame
import time
import random

# Инициализация Pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Определение размеров экрана
screen_width = 800
screen_height = 600

# Создание экрана
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Змейка")

# Определение размера блока и скорости змейки
block_size = 20
snake_speed = 15

# Определение шрифта
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

# Отображение счета
def show_score(score):
    score_value = score_font.render("Счет: " + str(score), True, BLACK)
    screen.blit(score_value, [10, 10])

# Отображение змейки
def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], block_size, block_size])

# Отображение сообщения о проигрыше
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])

# Главная функция игры
def game_loop():
    game_over = False
    game_close = False

    # Начальные координаты змейки
    x1 = screen_width / 2
    y1 = screen_height / 2

    # Изменение координат змейки
    x1_change = 0
    y1_change = 0

    # Создание списка для хранения координат сегментов змейки
    snake_list = []
    snake_length = 1

    # Генерация случайных координат для еды
    food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size

    # Главный игровой цикл
    while not game_over:

        while game_close:
            screen.fill(WHITE)
            message("Вы проиграли! Нажмите Q-Выход или C-Играть снова", RED)
            show_score(snake_length - 1)
            pygame.display.update()

            # Обработка событий при проигрыше
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Обработка событий в игре
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Обновление координат змейки
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(WHITE)

        # Отображение еды
        pygame.draw.rect(screen, RED, [food_x, food_y, block_size, block_size])

        # Добавление новых координат в список сегментов змейки
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Удаление лишних сегментов змейки, если ее длина превышает snake_length
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Проверка на столкновение змейки с самой собой
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Отображение змейки
        draw_snake(block_size, snake_list)

        # Отображение счета
        show_score(snake_length - 1)

        # Обновление экрана
        pygame.display.update()

        # Проверка на съедание еды
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size
            snake_length += 1

        # Определение скорости змейки
        clock = pygame.time.Clock()
        clock.tick(snake_speed)

    # Завершение Pygame
    pygame.quit()


# Запуск игры
game_loop()