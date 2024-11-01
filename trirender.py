import pygame, sys

pygame.init()
screen = pygame.display.set_mode((600, 400))


def triRender(p1, p2, p3):

    def lineEQ(x1, y1, x2, y2):
        m = (y2 - y1) / (x2 - x1)
        b = y2 - m * x2
        return (m, b)
        
    def graphLine(l, x1, y1, x2, y2):
        m, b = l
        xmin, xmax = min(x1, x2), max(x1, x2)
        for x in range(int(xmin), int(xmax) + 1):
            y = m * x + b
            screen.set_at((int(x), int(y)), (255, 255, 255))
        
    l1 = lineEQ(p1[0], p1[1], p2[0], p2[1])
    l2 = lineEQ(p1[0], p1[1], p3[0], p3[1])
    l3 = lineEQ(p2[0], p2[1], p3[0], p3[1])

    graphLine(l1, p1[0], p1[1], p2[0], p2[1])
    graphLine(l2, p1[0], p1[1], p3[0], p3[1])
    graphLine(l3, p2[0], p2[1], p3[0], p3[1])


p1 = (100, 150)
p2 = (300, 50)
p3 = (200, 300)

while True:
    screen.fill((0, 0, 0))
    triRender(p1, p2, p3)
    pygame.display.flip()
