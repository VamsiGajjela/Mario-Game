import pygame,random,sys,time,os

pygame.init()

display_width = 800
display_height = 600

gold = (244, 212, 66)
yellow = (247, 243, 0)
white = (255,255,255)
red = (200,0,0)
bright_red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Mario Kart Remastered")
clock = pygame.time.Clock()

APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))

pygame.mixer.music.load(os.path.join(APP_FOLDER, 'Music\Instructions_music.wav'))

instructionimg = pygame.image.load(os.path.join(APP_FOLDER, 'Pictures\instruction_background_base.png')).convert()


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
    
def display_message(message):
    Largetext = pygame.font.SysFont("comicsansbold", 60)
    TextSurf, TextRect = text_objects(message, Largetext)
    TextRect.center = (400), (50)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(0.1)
    
def instruction_background_display(x,y):
    gameDisplay.blit(instructionimg, (x,y))

def singleplayer():
    os.startfile('Single Player Instructions.py')

def multiplayer():
    os.startfile('MultiPlayer Instructions.py')

def menu():
    os.startfile('Mario Kart Remastered Intro Screen.py')

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "singleplayer":
                singleplayer()
                action='none'
            if action == "multiplayer":
                multiplayer()
                action='none'
            if action == "quit":
                menu()
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

def instructions():
    pygame.mixer.music.play()
    start = True
    while start == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        instruction_background_display(0,0)
        small_text_display("This game is not affiliated with Nintendo", 400, 570)
        small_text_display("Copyright © ATV.Inc 2018", 400, 580)
        button("Single Player",200, 150, 150, 50, gold, yellow,"singleplayer")
        button("Multiplayer",500, 150, 150, 50, gold, yellow,"multiplayer")
        button("Back", 350, 250, 150, 50, red, bright_red,"quit")
        display_message('How to Play')

        pygame.display.update()
        clock.tick(60)

while True:
    instructions()
    pygame.quit()
    quit()
