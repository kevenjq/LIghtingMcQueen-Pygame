# programmer Keven Quevedo --- Date 24/Aug/2021
# THis is a practice game with pygame--- cars


import pygame

pygame.init()

display_width = 800
display_height = 777

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Side To Side")
icon = pygame.image.load('lighting mcqueen birds eye view copy.png')
pygame.display.set_icon(icon)

# start of game photo
start_photo_of_car = pygame.image.load('cars2.jpeg')
start_photo_of_carX = 270
start_photo_of_carY = 250

# star of game text
start_of_game_text = pygame.image.load('Side to side logo text.png')
start_of_game_textX = 180
start_of_game_textY = 500

# track
track = pygame.image.load('racetrack.jpeg')
trackX = 180
trackY = 500

start_button = pygame.image.load('start button.png')
start_buttonX = 389
start_buttonY = 449


def first_text(x, y):
    screen.blit(start_of_game_text, (x, y))


def first_photo_of_car(x, y):
    screen.blit(start_photo_of_car, (x, y))


def background(x, y):
    screen.blit(track, (x, y))


def button_to_start_game(x, y):
    screen.blit(start_button, (x, y))


def pos_of_button():
    pos = pygame.mouse.get_pos()
    print(pos)
    if pos == (393, 456):
        screen.fill("white")


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if start_button.get_rect().collidepoint(x, y):
                print('clicked on image')

    button_to_start_game(start_buttonX, start_buttonY)
    first_photo_of_car(start_photo_of_carX, start_photo_of_carY)
    first_text(start_of_game_textX, start_of_game_textY)
    pygame.display.update()
