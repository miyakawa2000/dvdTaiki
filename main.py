import sys
import pygame
import random as rd

def RandomColor():
    R = rd.randrange(0, 255)
    G = rd.randrange(0, 255)
    B = rd.randrange(0, 255)
    return (R, G, B)

def main():
    # init pygame
    pygame.init()
    # init the display
    width = 600
    height = 600
    main_surface = pygame.display.set_mode((width, height))
    # set the title of main display
    pygame.display.set_caption("DVD Taiki")
    # generate the font object（value：(font type, font size)）
    # if font type is "None", it's set as the default font of pygame
    font = pygame.font.Font(None, 60)
    # generate the text surface object（value：text, antialias: bool, (R, G, B)）
    text_color = RandomColor()
    text_surface = font.render("DVD", True, text_color)
    # set the text width and height
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()
    # set the color of main display（value：(R,G,B)）
    white = (220, 220, 220)
    main_surface.fill(white)
    # set the text on the main display（value：(surface, coordinate)）
    x = rd.randrange(0, width - text_width)
    y = rd.randrange(0, height - text_height)
    main_surface.blit(text_surface, (x, y))
    # update the main display
    pygame.display.update()
    # set the clock object
    clock = pygame.time.Clock()
    # set initial velocity
    vx = 4
    vy = -4

    # flag for loop
    going = True
    # main loop
    while going:
        # get a event
        for event in pygame.event.get():
            # if event type is quit, set the flag False
            if event.type == pygame.QUIT:
                going = False

        # init main surface
        main_surface.fill(white)
        # move
        x += vx
        y += vy

        # collision decision
        if x <= 0 or x + text_width >= width:
            vx *= -1
            vx += rd.uniform(-1, 1)
            text_color = RandomColor()
            text_surface = font.render("DVD", True, text_color)
        if y <= 0 or y + text_height >= height:
            vy *= -1
            vy += rd.uniform(-1, 1)
            text_color = RandomColor()
            text_surface = font.render("DVD", True, text_color)

        # depict the text
        main_surface.blit(text_surface, (x, y))
        # update the display
        pygame.display.update()

        # set the frame rate
        clock.tick(30)

    # quit
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()