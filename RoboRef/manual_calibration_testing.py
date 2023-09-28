
import sys
import argparse
import cv2

count = 0
vidcap = cv2.VideoCapture("test3.mov")
success, image = vidcap.read()
cv2.imwrite("FrameOne3.jpg", image)
quit()

#306:
#153:

#Manual Calibrating Playing Around

import pygame

pygame.init()

screen = pygame.display.set_mode((50, 50))
pygame.display.set_caption("Display")

red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

background = pygame.image.load("FrameOne.jpg")
width, height = background.get_rect().size
half_width = int(width/2)

screen = pygame.display.set_mode((width, height))
"""
far_sidline_y_value = 265
up_values = [(x, far_sidline_y_value) for x in range(width)]
down_values = [(0, y) for y in range(far_sidline_y_value, height, 1)]#+[(x, height) for x in range(0, width, 1)]+



screen.blit(background, (0, 0))
for i in range(len(down_values)) :
    pygame.draw.line(screen, blue, up_values[i], down_values[i])
    pygame.display.update()
#quit()
"""
#y=(-42.7873x+156947.0158)/(x+215.9736) Vertical
#y=(58.4672x+87757.0512)/(x+8.2499) Horizontal


def horizontal(y_hor) :
    return ((58.4672*y_hor)+87757.0512)/(y_hor+8.2499)

def vertical(y_value) :
    return (156947.0158-(215.9736*y_value))/(y_value+42.7873)

def get_inches_relating_to_close_side_halfway_line(pix_x, pix_y) :
    return ((pix_x-half_width)*((horizontal(pix_y))/width), vertical(pix_y))

def get_pixels_to_inches_dictionary() :
    pixels_to_inches = {}
    for x_pixel in range(width+1) :
        for y_pixel in range(height+1) :
            pixels_to_inches[(x_pixel, y_pixel)] = get_inches_relating_to_close_side_halfway_line(x_pixel, y_pixel)
    return pixels_to_inches

#print(get_pixels_to_inches_dictionary()[(200, 200)])

"""
#print(pixels_to_inches[(200, 200)])
#quit()
        

#Not currently making translations
y_horizontals = [horizontal(y_horizontal) for y_horizontal in range(42, height+1)]
for y_val in range(42, height+1) :
    pass
#print(width, height)

while True :
    screen.blit(background, (0, 0))
    x, y = pygame.mouse.get_pos()
    pygame.draw.line(screen, red, (0, 306), (width, 306))
    pygame.draw.line(screen, red, (0, 153), (width, 153))
    pygame.draw.line(screen, red, (0, 95), (width, 95))
    pygame.draw.line(screen, red, (0, 50), (width, 50))
    pygame.draw.line(screen, red, (0, 194), (width, 194))
    pygame.draw.line(screen, red, (0, 225), (width, 225))
    pygame.draw.line(screen, blue, (half_width, 0), (half_width, height))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN :
            print(x, y)
    pygame.display.update()
"""

"""
while True :
    screen.blit(background, (0, 0))
    x, y = pygame.mouse.get_pos()
    pygame.draw.line(screen, red, (0, 306), (width, 306))
    pygame.draw.line(screen, red, (0, 153), (width, 153))
    pygame.draw.line(screen, red, (0, 95), (width, 95))
    pygame.draw.line(screen, red, (0, 50), (width, 50))
    pygame.draw.line(screen, red, (0, 194), (width, 194))
    pygame.draw.line(screen, red, (0, 225), (width, 225))
    pygame.draw.line(screen, blue, (half_width, 0), (half_width, height))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN :
            print(x, y)
    pygame.display.update()
"""




