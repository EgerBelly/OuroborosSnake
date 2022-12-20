import time

import pygame.font

def game():
    import pygame
    import random
    pygame.mixer
    from random import randint
    from copy import deepcopy
    import numpy as np
    from numba import njit
    sound = pygame.mixer.Sound("notification.wav")
    sound2 = pygame.mixer.Sound("ahtung-ahtung.wav")
    sound3 = pygame.mixer.Sound("film-i-televidenie-legkaya-melodiya-otkryivayuschiy-korotkiy-saundtrek-37773.wav")
    sound3.play(-1)

    pygame.init()

    width = 640
    height = 480
    display = pygame.display.set_mode((width, height))
    background = pygame.image.load("fon.png").convert()
    background = pygame.transform.smoothscale(background, display.get_size())
    pygame.display.update()
    pygame.display.set_caption("Змейка")

    colors = {
        "snake_head": (0, 255, 0),
        "snake_tail": (0, 200, 0),
        "apple": (255, 0, 0)
    }


    snake_pos = {
        "x": width / 2 - 10,
        "y": height / 2 - 10,
        "x_change": 0,
        "y_change": 0
    }


    snake_size = (10, 10)


    snake_speed = 10


    snake_tails = []

    snake_pos["x_change"] = -snake_speed
    for i in range(75):
        snake_tails.append([snake_pos["x"] + 10 * i, snake_pos["y"]])

    # food
    food_pos = {
        "x": round(random.randrange(0, width - snake_size[0]) / 10) * 10,
        "y": round(random.randrange(0, height - snake_size[1]) / 10) * 10,
    }

    food_size = (10, 10)
    food_eaten = 0


    game_end = False
    clock = pygame.time.Clock()



    while not game_end:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_end = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_pos["x_change"] == 0:
                    # move left
                    snake_pos["x_change"] = -snake_speed
                    snake_pos["y_change"] = 0

                elif event.key == pygame.K_RIGHT and snake_pos["x_change"] == 0:
                    # move right
                    snake_pos["x_change"] = snake_speed
                    snake_pos["y_change"] = 0

                elif event.key == pygame.K_UP and snake_pos["y_change"] == 0:
                    # move up
                    snake_pos["x_change"] = 0
                    snake_pos["y_change"] = -snake_speed

                elif event.key == pygame.K_DOWN and snake_pos["y_change"] == 0:
                    # move down
                    snake_pos["x_change"] = 0
                    snake_pos["y_change"] = snake_speed

                elif event.key == pygame.K_ESCAPE:
                    # Задаем ширину и высоту экрана

                    sound3.stop()

                    size = [640, 480]
                    screen = pygame.display.set_mode(size)

                    screen.blit(background, (0, 0))

                    # Установить заголовок окна
                    pygame.display.set_caption("Змейка")

                    done = False
                    clock = pygame.time.Clock()

                    # Основной цикл программы
                    while done == False:
                        # Пользователь что-то сделал
                        for event in pygame.event.get():
                            # Реагируем на действия пользователя
                            if event.type == pygame.QUIT:
                                sound3.play()
                                done = True
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    sound3.play()
                                    done = True
                                    break


                        #Тут можно рисовать
                        fontObj = pygame.font.Font('8bitwonderrusbylyajka_nominal.otf', 30)
                        textSurfaceObj1 = fontObj.render('PAUSE', True, (0, 255, 0))
                        textRectObj1 = textSurfaceObj1.get_rect()
                        textSurfaceObj2 = fontObj.render('press ESC to continue', True, (0, 255, 0))
                        textRectObj2 = textSurfaceObj2.get_rect()
                        textRectObj1.center = (width / 2 - 10, height / 2 - 10)
                        textRectObj2.center = (width / 2 - 10, height / 2 + 30)

                        screen.blit(textSurfaceObj1, textRectObj1)
                        screen.blit(textSurfaceObj2, textRectObj2)

                        # Рисунок появится после обновления экрана
                        pygame.display.flip()

                        # Экран будет перерисовываться 30 раз в секунду
                        clock.tick(30)


        # clear screen
        display.blit(background, (0, 0))


        # move snake tails
        ltx = snake_pos["x"]
        lty = snake_pos["y"]

        for i, v in enumerate(snake_tails):
            _ltx = snake_tails[i][0]
            _lty = snake_tails[i][1]

            snake_tails[i][0] = ltx
            snake_tails[i][1] = lty

            ltx = _ltx
            lty = _lty

        # draw snake tails
        for t in snake_tails:
            pygame.draw.rect(display, colors["snake_tail"], [
                t[0],
                t[1],
                snake_size[0],
                snake_size[1]])

        # draw snake
        snake_pos["x"] += snake_pos["x_change"]
        snake_pos["y"] += snake_pos["y_change"]

        # teleport snake, if required
        if (snake_pos["x"] < -snake_size[0]):
            snake_pos["x"] = width

        elif (snake_pos["x"] > width):
            snake_pos["x"] = 0

        elif (snake_pos["y"] < -snake_size[1]):
            snake_pos["y"] = height

        elif (snake_pos["y"] > height):
            snake_pos["y"] = 0

        pygame.draw.rect(display, colors["snake_head"], [
            snake_pos["x"],
            snake_pos["y"],
            snake_size[0],
            snake_size[1]])

        # draw food

        pygame.draw.rect(display, colors["apple"], [
            food_pos["x"],
            food_pos["y"],
            food_size[0],
            food_size[1]])

        # detect collision with food
        if (snake_pos["x"] == food_pos["x"]
                and snake_pos["y"] == food_pos["y"]):
            sound.play()
            food_eaten += 1
            snake_tails.append([food_pos["x"], food_pos["y"]])

            food_pos = {
                "x": round(random.randrange(0, width - snake_size[0]) / 10) * 10,
                "y": round(random.randrange(0, height - snake_size[1]) / 10) * 10,
            }
        # TILE = 10
        # W, H = width // TILE, height // TILE
        # FPS = 30
        # next_field = np.array([[0 for i in range(W)] for j in range(H)])
        # current_field = np.array([[0 for i in range(W)] for j in range(H)])
        #
        # def set_glider_SE(current_field, x, y):
        #     pos = [(x,y), (x+1, y+1), (x-1, y+2), (x, y+2), (x+1, y+2)]
        #     for i, j in pos:
        #         current_field[j][i] = 1
        #     return current_field
        # def set_glider_NW(current_field, x, y):
        #     pos = [(x,y), (x-2, y-1), (x-2, y), (x-2, y+1), (x-1, y-1)]
        #     for i, j in pos:
        #         current_field[j][i] = 1
        #     return current_field
        # for _ in range(5):
        #     i0, j0 = random.randrange(1, W // 2 + W // 4, 1), random.randrange(TILE, H // 2)
        #     current_field =  set_glider_SE(current_field, i0, j0)
        #     i1, j1 = random.randrange(W // 2 - W // 4, W - TILE), random.randrange(H // 2, H - TILE)
        #     current_field = set_glider_NW(current_field, i1, j1)
        #
        # @njit(fastmath=True)
        # def check_cells(current_field, next_field):
        #     res = []
        #     for x in range(W):
        #         for y in range(H):
        #             count = 0
        #             for j in range(y - 1, y + 2):
        #                 for i in range(x - 1, x + 2):
        #                     if current_field[j % H][i % W] == 1:
        #                         count += 1
        #             if current_field[y][x] == 1:
        #                 count-=1
        #                 if count == 2 or count == 3:
        #                     next_field[y][x] = 1
        #                     res.append((x, y))
        #                 else:
        #                     next_field[y][x] == 0
        #             else:
        #                 if count == 3:
        #                     next_field[y][x] = 1
        #                     res.append((x,y))
        #                 else:
        #                     next_field[y][x] = 0
        #     return next_field, res
        #
        # #while True:
        #
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         exit()
        # #  draw life
        # next_field, res = check_cells(current_field, next_field)
        # [pygame.draw.rect(display, pygame.Color(255, 255, 0),
        #                   (x * TILE + 1, y * TILE + 1, TILE - 1, TILE - 1)) for x, y in res]
        # current_field = deepcopy(next_field)
        # pygame.display.flip()
        # #clock.tick(FPS)

        # detect collision with tail
        for i, v in enumerate(snake_tails):
            if (snake_pos["x"] + snake_pos["x_change"] == snake_tails[i][0]
                    and snake_pos["y"] + snake_pos["y_change"] == snake_tails[i][1]):
                #sound2.play()
                snake_tails = snake_tails[:i]
                break

        pygame.display.update()

        # set FPS
        clock.tick(30)

    sound3.stop()
    return 666

