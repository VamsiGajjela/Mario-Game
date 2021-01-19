import pygame,random,sys,time,os
from os import path

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
green = (0,200,0)
bright_green = (0,255,0)
red = (200,0,0)
bright_red = (255,0,0)
gold = (244, 212, 66)
yellow = (247, 243, 0)

highscore_file = "highscore.txt"

APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption(os.path.join(APP_FOLDER, "Mario Kart Remastered"))
clock = pygame.time.Clock()

pygame.mixer.music.load(os.path.join(APP_FOLDER, 'Music\Intro_music.wav'))

backgroundimg = pygame.image.load(os.path.join(APP_FOLDER, 'Pictures\intro_background_base.png')).convert()

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
    
def display_message(message):
    Largetext = pygame.font.SysFont("comicsansms", 25)
    TextSurf, TextRect = text_objects(message, Largetext)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(0.1)

def background_display(x,y):
    gameDisplay.blit(backgroundimg, (x,y))

def instruc_file():
    os.startfile('Mario Kart Remastered Instructions.py')

def game_file():
    os.startfile('Mario Kart Character Menu.py')

def game_file_2():
    os.startfile('2 player.py')

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "play":
                game_file()
                quit()
            if action == "play_2":
                game_file_2()
                quit()
            if action == 'instructions':
                instruc_file()
                quit()
            if action == "quit":
                pygame.quit()
                quit()
                
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    Smalltext = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, Smalltext)
    textRect.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(textSurf, textRect)

def small_text_display(msg, x, y):
    Smalltext = pygame.font.Font("freesansbold.ttf",10)
    textSurf, textRect = text_objects(msg, Smalltext)
    textRect.center = ((x), (y))
    gameDisplay.blit(textSurf, textRect)

def high_score_display(msg, highscore, x , y):
    scoretext = pygame.font.SysFont("comicsansms", 25)
    textSurf, textRect = text_objects(msg + highscore, scoretext)
    textRect.center = ((x), (y))
    gameDisplay.blit(textSurf, textRect)
    
def game_intro():
    pygame.mixer.music.play()
    start = True
    while start == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        dir = path.dirname(__file__)
        with open(path.join(dir, highscore_file), 'r') as f :              
            try:
                highscore = f.read()
            except:
                highscore = f.read()
        background_display(0,0)
        small_text_display("This game is not affiliated with Nintendo", 400, 570)
        small_text_display("Copyright © ATV.Inc 2018", 400, 580)
        button("Single Player",200, 150, 150, 50, green, bright_green,"play")
        button("Multiplayer",500, 150, 150, 50, green, bright_green,"play_2")
        button("How to Play",200, 230, 150, 50, gold, yellow, "instructions")
        button("Quit",500, 230, 150, 50, red, bright_red,"quit")
        high_score_display("The current high score is: ", highscore, 400, 100)
        
        pygame.display.update()
        clock.tick(60)

while True:
    game_intro()
    pygame.quit()
    quit()
