import pygame,random,sys,time,os

pygame.init()

display_width = 800
display_height = 600

white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Mario Kart Remastered")
clock = pygame.time.Clock()

APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))


pygame.mixer.music.load(os.path.join(APP_FOLDER, 'Music\Instructions_music.wav'))

instructionimg = pygame.image.load(os.path.join(APP_FOLDER, 'Pictures\instruction_background_base.png')).convert()
playeroneimg = pygame.image.load(os.path.join(APP_FOLDER, 'Pictures\mario controls.png'))
playertwoimg = pygame.image.load(os.path.join(APP_FOLDER, 'Pictures\luigi controls.png'))

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

def control_mario(x,y):
    gameDisplay.blit(playeroneimg, (x,y))

def control_luigi(x,y,):
    gameDisplay.blit(playertwoimg, (x,y))

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
        text_display("Multiplayer", 400, 75, 30)
        text_display("Objective:",400,125,30)
        text_display('Your goal is to achieve a higher score than the other player',400,155,25)
        text_display('You need to avoid the incoming enemies to score points',400,180,25)
        text_display('Every 100 points you score the enemies will speed up',400,215,25)
        text_display('If you hit an enemy you lose and the other player continues',400,240,25)
        text_display(' so avoid them to score as much as you can and beat the other person',400,265,25)
        text_display('Last player to survive wins',400,295,25)
        text_display("Player 1:",200,340,30)
        control_mario(100,360)
        text_display("Player 2:",600,340,30)
        control_luigi(500, 360)


        text_display('The instructions will automatically close within 30 seconds.', 400, 550,20)
        
        pygame.time.delay(30000)
        os.startfile('Mario Kart Remastered Instructions.py')
        start = False

while True:
    instructions()
    pygame.quit()
    quit()
