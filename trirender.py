import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Triangle Renderer')

def triRender(p1, p2, p3, color, fill):
    xs = []
    ys = []

    def line_eq(x1, y1, x2, y2):
        m = (y2 - y1) / (x2 - x1)
        b = y2 - m * x2
        return m, b

    def graph_line(line, x1, y1, x2, y2):
        m, b = line
        xmin, xmax = min(x1, x2), max(x1, x2)

        for x in range(int(xmin), int(xmax) + 1):
            y = int(m * x + b)
            ys.append(y)
            xs.append(x)
            screen.set_at((x, y), color)

    def fill_triangle():
        xs.remove(p1[0])
        xs.remove(p2[0])
        xs.remove(p3[0])
        ys.remove(p1[1])
        ys.remove(p2[1])
        ys.remove(p3[1])

        for i in range(len(xs)):
            xv = xs[i]
            yv1 = ys[i]
            xs.remove(xv)
            ys.remove(yv1)
            xj = 0
            while xs[xj] != xs[i]:
                xj += 1
            ys.remove(ys[xj])

            yv2 = ys[xj]
            ymin, ymax = min(yv1, yv2), max(yv1, yv2)
            for y in range(ymin, ymax + 1):
                screen.set_at((xv, y), color)

    l1 = line_eq(p1[0], p1[1], p2[0], p2[1])
    l2 = line_eq(p1[0], p1[1], p3[0], p3[1])
    l3 = line_eq(p2[0], p2[1], p3[0], p3[1])

    graph_line(l1, p1[0], p1[1], p2[0], p2[1])
    graph_line(l2, p1[0], p1[1], p3[0], p3[1])
    graph_line(l3, p2[0], p2[1], p3[0], p3[1])

    if fill:
        fill_triangle()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    p1, p2, p3 = (100, 100), (300, 250), (200, 400)
    triRender(p1, p2, p3, (255, 0, 0), True) 

    pygame.display.flip()
