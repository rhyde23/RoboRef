import pygame, random

pygame.init()

red = (255, 0, 0)
green = (0, 255, 0)
dark_green = (0, 175, 0)
black = (0, 0, 0)
white = (255, 255, 255)

window_size = 700
screen = pygame.display.set_mode((window_size, window_size))

pygame.display.set_caption("Rain")

rains = []
rain_amt = 8000

def randomizeRain() :
    length = random.randint(2, 4)
    height = random.randint(2, 10)
    x = random.randint(1, 700-length)
    color = (0, 0, random.randint(50, 205))
    speed = random.randint(50, 500)
    return [x, -height, length, height, color, speed/100]

def populateRains() :
    for r in range(rain_amt) :
        rains.append(randomizeRain())


populateRains()


while True :
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN :
            pass
    for index in range(len(rains)) :
        rain = rains[index]
        pygame.draw.rect(screen, rain[4], [rain[0], rain[1], rain[2], rain[3]])
        rain[1] += rain[5]
        if rain[1] > window_size :
            rains[index] = randomizeRain()
    pygame.display.update()

