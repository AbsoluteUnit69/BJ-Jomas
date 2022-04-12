from cmath import acos, asin, cos, sin
import math
import pygame
import pymunk
import pymunk.pygame_util

pygame.init()

WIDTH, HEIGHT = 1000, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw(space, screen, draw_options):
    screen.fill((0,0,0))
    space.debug_draw(draw_options)
    pygame.display.update()

def create_bollock(space, radius, mass):
    body = pymunk.Body()
    body.position = (100,100)
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (255, 255, 255, 50)
    space.add(body, shape)
    return shape




def main(screen, width, height):
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1 / fps
    space = pymunk.Space()
    space.gravity = (0, 981)

    bollock = create_bollock(space, 25, 10)

    draw_options = pymunk.pygame_util.DrawOptions(screen)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(space, screen, draw_options)
        space.step(dt)
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    main(screen, WIDTH, HEIGHT)