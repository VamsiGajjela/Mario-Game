import pygame,random,sys,time,os
from os import path

pygame.init()

display_width = 800
display_height = 600

HW, HH = display_width/2, display_height/2
area = display_width*display_height

os.environ["SDL_VIDEO_WINDOW_POS"] = "50,50"

black = (0,0,0)
white = (255,255,255)
green = (0,200,0)
bright_green = (0,255,0)
red = (200,0,0)
bright_red = (255,0,0)
grey = (207,207,207)
highscore_file = "highscore.txt"

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Mario Kart Remastered")
clock = pygame.time.Clock()

car_width = 73
graphics = 0
score = -10

trackimg = pygame.image.load('Pictures\Track_2.png').convert()


gameoversound = pygame.mixer.Sound('Music\Gameover_sound.wav')

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
    
def display_message(message,x,y):
    Largetext = pygame.font.SysFont("comicsansbold", 60)
    TextSurf, TextRect = text_objects(message, Largetext)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(0.1)

def main_menu():
    os.startfile('Mario Kart Remastered Intro Screen.py')

def game():
    os.startfile('Mario Kart Character Menu.py')
    
def small_text_display(msg, x, y):
    Smalltext = pygame.font.Font("freesansbold.ttf",10)
    textSurf, textRect = text_objects(msg, Smalltext)
    textRect.center = ((x), (y))
    gameDisplay.blit(textSurf, textRect)

def message(message):
    Largetext = pygame.font.SysFont("comicsansms", 30)
    TextSurf, TextRect = text_objects(message, Largetext)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(0.1)

def text_display(message,x,y):
    Largetext = pygame.font.SysFont("comicsansbold", 60)
    TextSurf, TextRect = text_objects(message, Largetext)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(0.1)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "main_menu":
                main_menu()
                quit()
            elif action == 'play':
                game()
                quit()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    Smalltext = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, Smalltext)
    textRect.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(textSurf, textRect) 

def scorekeeper(score):
    font = pygame.font.SysFont("comicsansms", 25)
    text=font.render('Score '+str(score),True,white)
    gameDisplay.blit(text,(100,500))

def game_end():
    pygame.mixer.music.load('Music\Gameover_music.wav')
    pygame.mixer.music.play()    
    start = True
    while start == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(trackimg,(0,0))
        small_text_display("This game is not affiliated with Nintendo", 400, 570)
        small_text_display("Copyright © ATV.Inc 2018", 400, 580)
        button("<-- Back",50, 20, 100, 50, grey, black,"main_menu")
        button("Play Again",360, 500, 100, 50, green, bright_green,"play")
        display_message('High Score',400,20)
        dir = path.dirname(__file__)
        with open(path.join(dir, highscore_file), 'r') as f :              
            try:
                highscore = f.read()
            except:
                highscore = f.read()
        text_display(str(highscore),400,250)
        
        pygame.display.update()
        clock.tick(60)

while True:
    game_end()
    pygame.quit()
    quit()
