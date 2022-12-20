import time

import pygame.font

def game():
    import pygame
    import random
    pygame.mixer

    sound = pygame.mixer.Sound("notification.wav")
    #sound2 = pygame.mixer.Sound("ahtung-ahtung.wav")
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
        "apple": (255, 0, 0),
        "enemy": (0 ,0, 255)
    }


    snake_pos = {
        "x": width / 2 - 10,
        "y": height / 2 - 10,
        "x_change": 0,
        "y_change": 0
    }

    enemy_pos = {
        "x": width / 4,
        "y": height / 4,
        "x_change": 0,
        "y_change": 0
    }

    snake_size = (10, 10)

    enemy_size = (10, 10)

    enemy_speed = 10

    enemy_tails = []

    snake_speed = 10


    snake_tails = []

    snake_pos["x_change"] = -snake_speed
    for i in range(75):
        snake_tails.append([snake_pos["x"] + 10 * i, snake_pos["y"]])

    # enemy_pos["x_change"] = -enemy_speed
    # for i in range(75):
    #     enemy_tails.append([enemy_pos["x"] + 10 * i, enemy_pos["y"]])

    # еда
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
                    # лево
                    snake_pos["x_change"] = -snake_speed
                    snake_pos["y_change"] = 0

                elif event.key == pygame.K_RIGHT and snake_pos["x_change"] == 0:
                    # право
                    snake_pos["x_change"] = snake_speed
                    snake_pos["y_change"] = 0

                elif event.key == pygame.K_UP and snake_pos["y_change"] == 0:
                    # вверх
                    snake_pos["x_change"] = 0
                    snake_pos["y_change"] = -snake_speed

                elif event.key == pygame.K_DOWN and snake_pos["y_change"] == 0:
                    # вниз
                    snake_pos["x_change"] = 0
                    snake_pos["y_change"] = snake_speed

                elif event.key == pygame.K_ESCAPE:

                    sound3.stop()

                    size = [640, 480]
                    screen = pygame.display.set_mode(size)

                    screen.blit(background, (0, 0))

                    pygame.display.set_caption("Змейка")

                    done = False
                    clock = pygame.time.Clock()

                    while done == False:

                        for event in pygame.event.get():

                            if event.type == pygame.QUIT:
                                sound3.play()
                                done = True
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    sound3.play()
                                    done = True



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


        # очистить экран
        display.blit(background, (0, 0))


        # координаты хвоста
        ltx = snake_pos["x"]
        lty = snake_pos["y"]

        for i, v in enumerate(snake_tails):
            _ltx = snake_tails[i][0]
            _lty = snake_tails[i][1]

            snake_tails[i][0] = ltx
            snake_tails[i][1] = lty

            ltx = _ltx
            lty = _lty

        #  рисуем хвост
        for t in snake_tails:
            pygame.draw.rect(display, colors["snake_tail"], [
                t[0],
                t[1],
                snake_size[0],
                snake_size[1]])


        # pygame.draw.rect(display, colors["enemy"], [
        #     t[1],
        #     t[0],
        #     enemy_size[0],
        #     enemy_size[1]])

        # рисуем змею полностью
        snake_pos["x"] += snake_pos["x_change"]
        snake_pos["y"] += snake_pos["y_change"]

        # enemy_pos["x"] += enemy_pos["x_change"]
        # enemy_pos["y"] += enemy_pos["y_change"]

        # телепорт на противоположную сторону
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

        pygame.draw.rect(display, colors["enemy"], [
            enemy_pos["x"],
            enemy_pos["y"],
            enemy_size[0],
            enemy_size[1]])

        # рисуем еду

        pygame.draw.rect(display, colors["apple"], [
            food_pos["x"],
            food_pos["y"],
            food_size[0],
            food_size[1]])

        # столкновение с едой
        if (snake_pos["x"] == food_pos["x"]
                and snake_pos["y"] == food_pos["y"]):
            sound.play()
            food_eaten += 1
            snake_tails.append([food_pos["x"], food_pos["y"]])

            food_pos = {
                "x": round(random.randrange(0, width - snake_size[0]) / 10) * 10,
                "y": round(random.randrange(0, height - snake_size[1]) / 10) * 10,
            }

        # if (snake_pos["x"] == enemy_pos["x"]
        #         and snake_pos["y"] == enemy_pos["y"]):
        #     while True:
        #         sound3.stop()
        #         fontObj2 = pygame.font.Font('8bitwonderrusbylyajka_nominal.otf', 30)
        #         textSurfaceObj3 = fontObj2.render('proigral epta', True, (0, 255, 0))
        #         textRectObj3 = textSurfaceObj3.get_rect()
        #         textRectObj3.center = (width / 2 - 10, height / 2 - 10)
        #         display.blit(textSurfaceObj3, textRectObj3)
        #         pygame.display.flip()
        #         for event in pygame.event.get():
        #             if event.type == pygame.QUIT:
        #                 pygame.quit()
        #
        #             elif event.type == pygame.KEYDOWN:
        #                 if event.key == pygame.K_ESCAPE:
        #                     break


            food_pos = {
                "x": round(random.randrange(0, width - snake_size[0]) / 10) * 10,
                "y": round(random.randrange(0, height - snake_size[1]) / 10) * 10,
            }


        # столкновение с хвостом
        for i, v in enumerate(snake_tails):
            if (snake_pos["x"] + snake_pos["x_change"] == snake_tails[i][0]
                    and snake_pos["y"] + snake_pos["y_change"] == snake_tails[i][1]):
                #sound2.play()
                snake_tails = snake_tails[:i]
                break

        pygame.display.update()

        clock.tick(30)

    sound3.stop()


