import sys
import pygame
import random as rd
from typing import Tuple

def RandomColor() -> Tuple[int,int,int]:
    R = rd.randrange(0, 255)
    G = rd.randrange(0, 255)
    B = rd.randrange(0, 255)
    return (R, G, B)

def renderer(text: str,font_type: str=None, font_size: int=50, text_color: Tuple[int,int,int]=(220,220,220)) -> pygame.Surface:
    # generate the font object
    font = pygame.font.Font(font_type, font_size)
    # generate the text surface object（value：text, antialias: bool, (R, G, B)）
    text_surface = font.render(text, True, text_color)
    return text_surface

def main():
    # init pygame
    pygame.init()
    # init the display
    width = 600
    height = 600
    main_surface = pygame.display.set_mode((width, height))
    # set the title of main display
    pygame.display.set_caption("DVD Taiki")

    text_color = RandomColor()

    ### DVD ###
    text_surface1 = renderer("DVD", font_size=60, text_color=text_color)
    # set the "DVD" width and height
    dvd_width = text_surface1.get_width()
    dvd_height = text_surface1.get_height()

    ### video ###
    text_surface2 = renderer("video", font_size=30, text_color=text_color)
    # set the "video" width and height
    video_width = text_surface2.get_width()
    video_height = text_surface2.get_height()

    # set the text width and height
    text_width = max(dvd_width, video_width)
    text_height = dvd_height + video_height

    # set the color of main display（value：(R,G,B)）
    main_surface_color = (0, 0, 0)
    main_surface.fill(main_surface_color)
    # set the text on the main display（value：(surface, coordinate)）
    x = rd.randrange(0, width - text_width)
    y = rd.randrange(0, height - text_height)
    main_surface.blit(text_surface1, (x, y))
    main_surface.blit(text_surface2, (x+(dvd_width-video_width)/2, y+dvd_height))
    # update the main display
    pygame.display.update()
    # set the clock object
    clock = pygame.time.Clock()
    # set initial velocity
    vx = 4
    vy = -4

    # flag for loop
    going = True
    ### main loop ###
    while going:
        # get a event
        for event in pygame.event.get():
            # if event type is quit, set the flag False
            if event.type == pygame.QUIT:
                going = False

        # init main surface
        main_surface.fill(main_surface_color)

        # move
        x += vx
        y += vy

        # collision decision
        if x <= 0 or x + text_width >= width:
            vx *= -1
            vx += rd.uniform(-0.5, 0.5)
            text_color = RandomColor()
            text_surface1 = renderer("DVD", font_size=60, text_color=text_color)
            text_surface2 = renderer("video", font_size=30, text_color=text_color)
        if y <= 0 or y + text_height >= height:
            vy *= -1
            vy += rd.uniform(-0.5, 0.5)
            text_color = RandomColor()
            text_surface1 = renderer("DVD", font_size=60, text_color=text_color)
            text_surface2 = renderer("video", font_size=30, text_color=text_color)

        # depict the text
        main_surface.blit(text_surface1, (x, y))
        main_surface.blit(text_surface2, (x+(dvd_width-video_width)/2, y+dvd_height))
        # update the display
        pygame.display.update()

        # set the frame rate
        clock.tick(30)

    # quit
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()