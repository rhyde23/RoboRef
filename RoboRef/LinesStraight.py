#Check if lines are straigjt
import pygame

pygame.init()

screen = pygame.display.set_mode((50, 50))
pygame.display.set_caption("Display")

red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

hyc_interval = 25

def test() :
    fileName = input("File Name >> ")
    background = pygame.image.load(fileName)
    width, height = background.get_rect().size
    height_rounded_down = (height-(height%hyc_interval))
    horizontal_lines_y_coords = [i for i in range(hyc_interval, height, hyc_interval)]
    vertical_line_x_coord = int(width/2)
    print(horizontal_lines_y_coords)
    print(vertical_line_x_coord)
    screen = pygame.display.set_mode((width, height))
    while True :
        screen.blit(background, (0, 0))
        pygame.draw.line(screen, red, (vertical_line_x_coord, 0), (vertical_line_x_coord, height))
        for hyc in horizontal_lines_y_coords :
            pygame.draw.line(screen, red, (0, hyc), (width, hyc))
        pygame.display.update()


test()
