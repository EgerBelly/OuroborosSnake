import pygame
import pygame_menu
import random

from pygame_menu import Theme

pygame.init()
surface = pygame.display.set_mode((640, 480))
bg_image = pygame.image.load("fon.png").convert()
bg_image = pygame.transform.smoothscale(bg_image, surface.get_size())
import main
pygame.mixer
pygame_menufont = pygame_menu.font.FONT_8BIT
pygame_menuframe = pygame_menu.widgets.MENUBAR_STYLE_NONE
mytheme = Theme(
    scrollbar_slider_color=(0, 255, 0),
    scrollbar_slider_hover_color=(0, 255, 0),
    selection_color=(0, 255, 0),
    surface_clear_color=(0, 255, 0),
    scrollbar_color=(0, 0, 0),
    title_bar_style=pygame_menuframe,
    title_font_color=(0, 0, 0),
    widget_font=pygame_menufont

)
mytheme.set_background_color_opacity(0.0)
menu = pygame_menu.Menu('', 640, 480, theme=mytheme)

def getName(s):
    name = s


#menu.add.text_input('Name ', default='player 1', onchange=getName)
menu.add.button('Play', main.game)

menu.add.button('Exit', pygame_menu.events.EXIT)

while True:

    surface.blit(bg_image, (0,0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(surface)

    pygame.display.update()
