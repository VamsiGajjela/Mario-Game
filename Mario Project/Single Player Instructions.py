import pygame,random,sys,time,os

pygame.init()

display_width = 800
display_height = 600

white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Mario Kart Remastered")
clock = pygame.time.Clock()

pygame.mixer.music.load('Music\Instructions_music.wav')

instructionimg = pygame.image.load('Pictures\instruction_background_base.png').convert()

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
    
def display_message(message):
    Largetext = pygame.font.SysFont("comicsansbold", 60)
    TextSurf, TextRect = text_objects(message, Largetext)
    TextRect.center = ((display_width/2), (display_height/12))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(0.1)
    
def instruction_background_display(x,y):
    gameDisplay.blit(instructionimg, (x,y))

def text_display(msg, x, y, size):
    medium_text = pygame.font.SysFont("comicsansms", size)
    textSurf, textRect = text_objects(msg, medium_text)
    textRect.center = ((x), (y))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()
    time.sleep(0.1)

def instructions():
    pygame.mixer.music.play()
    start = True
    while start == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        instruction_background_display(0,0)
        text_display("This game is not affiliated with Nintendo", 400, 570,10)
        text_display("Copyright © ATV.Inc 2018", 400, 580,10)
        display_message('How to Play')
        text_display("Single Player", 400, 75, 30)
        text_display("Movement:",400,125,30)
        text_display("Use the Left and Right arrow keys to move your character",400,145,25)
        text_display("around the screen",400,170,25)
        text_display("Objective:",400,215,30)
        text_display('Your goal is avoid the incoming enemies to score points',400,240,25)
        text_display('Every enemy avoided grants you 5 points',400,265,25)
        text_display('Every 100 points you score the enemies will speed up',400,290,25)
        text_display('If you hit an enemy you lose and the game ends',400,315,25)
        text_display(' so avoid them to score as much as you can',400,345,25)


        text_display('The instructions will automatically close within 30 seconds.', 400, 550,20)
        
        pygame.time.delay(30000)
        os.startfile('Mario Kart Remastered Instructions.py')
        start = False

while True:
    instructions()
    pygame.quit()
    quit()
