import pygame
from pygame.locals import *
from config import *
pygame.init()


window = pygame.display.set_mode((width,height))
window.fill((255, 255, 255))
pygame.display.update()

pygame.display.set_caption('TicTacToe')

field = pygame.draw.rect
line = pygame.draw.line
circle = pygame.draw.circle


A1 = field(window, (255, 255, 255), (int(0+10), int(0+10), int(width/3-20), int(width/3-20)))
A2 = field(window, (255, 255, 255), (int(0+10), int(width/3+10), int(width/3-20), int(width/3-20)))
A3 = field(window, (255, 255, 255), (int(0+10), int(width/3*2+10), int(width/3-20), int(width/3-20)))
B1 = field(window, (255, 255, 255), (int(width/3+10), int(0+10), int(width/3-20), int(width/3-20)))
B2 = field(window, (255, 255, 255), (int(width/3+10), int(width/3+10), int(width/3-20), int(width/3-20)))
B3 = field(window, (255, 255, 255), (int(width/3+10), int(width/3*2+10), int(width/3-20), int(width/3-20)))
C1 = field(window, (255, 255, 255), (int(width/3*2+10), int(0+10), int(width/3-20), int(width/3-20)))
C2 = field(window, (255, 255, 255), (int(width/3*2+10), int(width/3+10), int(width/3-20), int(width/3-20)))
C3 = field(window, (255, 255, 255), (int(width/3*2+10), int(width/3*2+10), int(width/3-20), int(width/3-20)))

def grid():
    line(window, (45, 45, 45), (int(width/3), int(0)), (int(width/3), int(height)), lineth1)
    line(window, (45, 45, 45), (int(width/3*2), int(0)), (int(width/3*2), int(height)), lineth1)
    line(window, (45, 45, 45), (int(0), int(width/3)), (int(height), int(width/3)), lineth1)
    line(window, (45, 45, 45), (int(0), int(width/3*2)), (int(height), int(width/3*2)), lineth1)
grid()
pygame.display.update()

object = 'circle'

A1taken = 'a'
A2taken = 'a'
A3taken = 'a'
B1taken = 'a'
B2taken = 'a'
B3taken = 'a'
C1taken = 'a'
C2taken = 'a'
C3taken = 'a'

A1open = True
A2open = True
A3open = True
B1open = True
B2open = True
B3open = True
C1open = True
C2open = True
C3open = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                A1open = True
                A2open = True
                A3open = True
                B1open = True
                B2open = True
                B3open = True
                C1open = True
                C2open = True
                C3open = True
                A1taken = 'a'
                A2taken = 'a'
                A3taken = 'a'
                B1taken = 'a'
                B2taken = 'a'
                B3taken = 'a'
                C1taken = 'a'
                C2taken = 'a'
                C3taken = 'a'
                running = True
                field(window, (255, 255, 255), (0, 0, width, height))
                grid()
                pygame.display.update()

        if event.type == pygame.MOUSEBUTTONUP:
            position = pygame.mouse.get_pos()

            if A1.collidepoint(position) and A1open:
                if object == 'cross':
                    line(window, (45, 45, 45), (0+10, 0+10), (width/3-10, height/3-10), lineth2)
                    line(window, (45, 45, 45), (width/3-10, 0+10), (0+10, height/3-10), lineth2)
                    object = 'circle'
                    A1open = False
                    A1taken = 'cross'
                    pygame.display.update()
                else:
                    if object == 'circle':
                        circle(window, (45, 45, 45), (int(width/3/2), int(width/3/2)), rad, lineth2)
                        object = 'cross'
                        A1open = False
                        A1taken = 'circle'
                        pygame.display.update()

            if A2.collidepoint(position) and A2open:
                if object == 'cross':
                    line(window, (45, 45, 45), (0+10, width/3+10), (width/3-10, height/3*2-10), lineth2)
                    line(window, (45, 45, 45), (0+10, height/3*2-10), (width/3-10, height/3+10), lineth2)
                    object = 'circle'
                    A2open = False
                    A2taken = 'cross'
                    pygame.display.update()
                else:
                    if object == 'circle':
                        circle(window, (45, 45, 45), (int(width/3/2), int(width/3+width/3/2)), rad, lineth2)
                        object = 'cross'
                        A2open = False
                        A2taken = 'circle'
                        pygame.display.update()

            if A3.collidepoint(position) and A3open:
                if object == 'cross':
                    line(window, (45, 45, 45), (0+10, width/3*2+10), (width/3-10, height-10), lineth2)
                    line(window, (45, 45, 45), (0+10, height-10), (width/3-10, height/3*2+10), lineth2)
                    object = 'circle'
                    A3open = False
                    A3taken = 'cross'
                    pygame.display.update()
                else:
                    if object == 'circle':
                        circle(window, (45, 45, 45), (int(width/3/2), int(width-width/3/2)), rad, lineth2)
                        object = 'cross'
                        A3open = False
                        A3taken = 'circle'
                        pygame.display.update()

            if B1.collidepoint(position) and B1open:
                if object == 'cross':
                    line(window, (45, 45, 45), (width/3+10, 0+10), (width/3*2-10, height/3-10), lineth2)
                    line(window, (45, 45, 45), (width/3+10, height/3-10), (width/3*2-10, 0+10), lineth2)
                    object = 'circle'
                    B1open = False
                    B1taken = 'cross'
                    pygame.display.update()
                else:
                    if object == 'circle':
                        circle(window, (45, 45, 45), (int(width/2), int(width/3/2)), rad, lineth2)
                        object = 'cross'
                        B1open = False
                        B1taken = 'circle'
                        pygame.display.update()

            if B2.collidepoint(position) and B2open:
                if object == 'cross':
                    line(window, (45, 45, 45), (width/3+10, height/3+10), (width/3*2-10, height/3*2-10), lineth2)
                    line(window, (45, 45, 45), (width/3+10, height/3*2-10), (width/3*2-10, height/3+10), lineth2)
                    object = 'circle'
                    B2open = False
                    B2taken = 'cross'
                    pygame.display.update()
                else:
                    if object == 'circle':
                        circle(window, (45, 45, 45), (int(width/2), int(width/2)), rad, lineth2)
                        object = 'cross'
                        B2open = False
                        B2taken = 'circle'
                        pygame.display.update()

            if B3.collidepoint(position) and B3open:
                if object == 'cross':
                    line(window, (45, 45, 45), (width/3+10, height-10), (width/3*2-10, height/3*2+10), lineth2)
                    line(window, (45, 45, 45), (width/3+10, height/3*2+10), (width/3*2-10, height-10), lineth2)
                    object = 'circle'
                    B3open = False
                    B3taken = 'cross'
                    pygame.display.update()
                else:
                    if object == 'circle':
                        circle(window, (45, 45, 45), (int(width/2), int(width/3/2*2+width/2)), rad, lineth2)
                        object = 'cross'
                        B3open = False
                        B3taken = 'circle'
                        pygame.display.update()

            if C1.collidepoint(position) and C1open:
                if object == 'cross':
                    line(window, (45, 45, 45), (width/3*2+10, 0+10), (width-10, height/3-10), lineth2)
                    line(window, (45, 45, 45), (width/3*2+10, height/3-10), (height-10, 0+10), lineth2)
                    object = 'circle'
                    C1open = False
                    C1taken = 'cross'
                    pygame.display.update()
                else:
                    if object == 'circle':
                        circle(window, (45, 45, 45), (int(width/3*2+width/3/2), int(width/3/2)), rad, lineth2)
                        object = 'cross'
                        C1open = False
                        C1taken = 'circle'
                        pygame.display.update()

            if C2.collidepoint(position) and C2open:
                if object == 'cross':
                    line(window, (45, 45, 45), (width/3*2+10, height/3+10), (width-10, height/3*2-10), lineth2)
                    line(window, (45, 45, 45), (width/3*2+10, height/3*2-10), (width-10, height/3+10), lineth2)
                    object = 'circle'
                    C2open = False
                    C2taken = 'cross'
                    pygame.display.update()
                else:
                    if object == 'circle':
                        circle(window, (45, 45, 45), (int(width/3*2+width/3/2), int(width/2)), rad, lineth2)
                        object = 'cross'
                        C2open = False
                        C2taken = 'circle'
                        pygame.display.update()

            if C3.collidepoint(position) and C3open:
                if object == 'cross':
                    line(window, (45, 45, 45), (width/3*2+10, height/3*2+10), (width-10, height-10), lineth2)
                    line(window, (45, 45, 45), (width/3*2+10, height-10), (width-10, height/3*2+10), lineth2)
                    object = 'circle'
                    C3open = False
                    C3taken = 'cross'
                    pygame.display.update()
                else:
                    if object == 'circle':
                        circle(window, (45, 45, 45), (int(width-width/3/2), int(width-width/3/2)), rad, lineth2)
                        object = 'cross'
                        C3open = False
                        C3taken = 'circle'
                        pygame.display.update()

        if A1taken == 'circle':

            if B1taken == A1taken:
                if C1taken == A1taken:
                    line(window, (45, 45, 45), (width/3/2/2, height/3/2), (width-width/3/2/2, height/3/2), lineth3)
                    pygame.display.update()

            if A2taken == A1taken:
                if A3taken == A1taken:
                    line(window, (45, 45, 45), (width/3/2, height/3/2/2), (width/3/2, height-height/3/2/2), lineth3)
                    pygame.display.update()

        if C3taken == 'circle':

            if B3taken == C3taken:
                if A3taken == C3taken:
                    line(window, (45, 45, 45), (width-width/3/2/2, height-height/3/2), (width/3/2/2, height-height/3/2), lineth3)
                    pygame.display.update()
            if C2taken == C3taken:
                if C1taken == C3taken:
                    line(window, (45, 45, 45), (width-width/3/2, height/3/2/2), (width-width/3/2, height-height/3/2/2), lineth3)
                    pygame.display.update()

        if B2taken == 'circle':
            if A2taken == B2taken:
                if C2taken == B2taken:
                    line(window, (45, 45, 45), (width/3/2/2, height/2), (width-width/3/2/2, height/2), lineth3)
                    pygame.display.update()

            if B1taken == B2taken:
                if B3taken == B2taken:
                    line(window, (45, 45, 45), (width/2, height/3/2/2), (width/2, height-height/3/2/2), lineth3)
                    pygame.display.update()

            if A1taken == B2taken:
                if C3taken == B2taken:
                    line(window, (45, 45, 45), (width/3/2/2, height/3/2/2), (width-width/3/2/2, height-height/3/2/2), lineth3)
                    pygame.display.update()

            if A3taken == B2taken:
                if C1taken == B2taken:
                    line(window, (45, 45, 45), (width/3/2/2, height-height/3/2/2), (width-width/3/2/2, height/3/2/2), lineth3)
                    pygame.display.update()

        if A1taken == 'cross':

            if B1taken == A1taken:
                if C1taken == A1taken:
                    line(window, (45, 45, 45), (width/3/2/2, height/3/2), (width-width/3/2/2, height/3/2), lineth3)
                    pygame.display.update()

            if A2taken == A1taken:
                if A3taken == A1taken:
                    line(window, (45, 45, 45), (width/3/2, height/3/2/2), (width/3/2, height-height/3/2/2), lineth3)
                    pygame.display.update()

        if C3taken == 'cross':

            if B3taken == C3taken:
                if A3taken == C3taken:
                    line(window, (45, 45, 45), (width-width/3/2/2, height-height/3/2), (width/3/2/2, height-height/3/2), lineth3)
                    pygame.display.update()
            if C2taken == C3taken:
                if C1taken == C3taken:
                    line(window, (45, 45, 45), (width-width/3/2, height/3/2/2), (width-width/3/2, height-height/3/2/2), lineth3)
                    pygame.display.update()

        if B2taken == 'cross':
            if A2taken == B2taken:
                if C2taken == B2taken:
                    line(window, (45, 45, 45), (width/3/2/2, height/2), (width-width/3/2/2, height/2), lineth3)
                    pygame.display.update()

            if B1taken == B2taken:
                if B3taken == B2taken:
                    line(window, (45, 45, 45), (width/2, height/3/2/2), (width/2, height-height/3/2/2), lineth3)
                    pygame.display.update()

            if A1taken == B2taken:
                if C3taken == B2taken:
                    line(window, (45, 45, 45), (width/3/2/2, height/3/2/2), (width-width/3/2/2, height-height/3/2/2), lineth3)
                    pygame.display.update()

            if A3taken == B2taken:
                if C1taken == B2taken:
                    line(window, (45, 45, 45), (width/3/2/2, height-height/3/2/2), (width-width/3/2/2, height/3/2/2), lineth3)
                    pygame.display.update()
