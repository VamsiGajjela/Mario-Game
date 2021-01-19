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
bright_red = (255, 72, 0)
gold = (244, 212, 66)
yellow = (247, 243, 0)
blue = (66, 134, 244)
pink = (255, 61, 183)

highscore_file = "highscore.txt"

pygame.mixer.music.load('Music\Characterselect_music.wav')
mariosound = pygame.mixer.Sound('Mario\Mario_music.wav')
luigisound = pygame.mixer.Sound('Luigi\Luigi_music.wav')
toadsound = pygame.mixer.Sound('Toad\Toad_music.wav')
peachsound = pygame.mixer.Sound('Peach\Peach_music.wav')

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Mario Kart Remastered")
clock = pygame.time.Clock()

mariocarimg = pygame.image.load('Mario\mario_selection.png')
luigicarimg = pygame.image.load('Luigi\luigi_selection.png')
toadcarimg = pygame.image.load('Toad\Toad_selection.png')
peachcarimg = pygame.image.load('Peach\peach_selection.png')
backgroundimg = pygame.image.load('Pictures\instruction_background_base.png').convert()

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
    
def display_message(message):
    Largetext = pygame.font.SysFont("comicsansbold", 60)
    TextSurf, TextRect = text_objects(message, Largetext)
    TextRect.center = ((display_width/2), (display_height*0.2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(0.1)

def background_display(x,y):
    gameDisplay.blit(backgroundimg, (x,y))

def instruc_file():
    os.startfile('Mario Kart Remastered Instructions.py')

def game_file_mario():
    os.startfile('Version 2.1 (Mario).py')

def car_display_mario(x,y):
    gameDisplay.blit(mariocarimg, (x,y))

def game_file_luigi():
    os.startfile('Version 2.1 (Luigi).py')

def car_display_luigi(x,y):
    gameDisplay.blit(luigicarimg, (x,y))

def game_file_toad():
    os.startfile('Version 2.1 (Toad).py')

def car_display_toad(x,y):
    gameDisplay.blit(toadcarimg, (x,y))

def game_file_peach():
    os.startfile('Version 2.1 (Peach).py')

def car_display_peach(x,y):
    gameDisplay.blit(peachcarimg, (x,y))

def button(msg,x,y,w,h,ic,ac,sound,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            pygame.mixer.Sound.play(sound)
            time.sleep(1)
            if action == "mario":
                game_file_mario()
                quit()
            if action == 'luigi':
                game_file_luigi()
                quit()
            if action == 'toad':
                game_file_toad()
                quit()
            if action == 'peach':
                game_file_peach()
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
        button(' ',150, 225, 80, 85, bright_red, white,mariosound,"mario")
        car_display_mario(150,225)
        button(" ",300, 225, 80, 85, bright_green, white,luigisound,"luigi")
        car_display_luigi(300,225)
        button(" ",450, 225, 80, 85, blue, white, toadsound,"toad")
        car_display_toad(450,225)
        button(" ",600, 225, 80, 85, pink, white, peachsound,"peach")
        car_display_peach(600,225)
        display_message('Choose Your Character')
        
        pygame.display.update()
        clock.tick(60)

while True:
    game_intro()
    pygame.quit()
    quit()
