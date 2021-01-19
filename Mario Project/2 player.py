# Asad Bhatti, Vamsi Gajella, Taha Khimani
# June 18th 2018
# ICS3UR
# This file initiates the 2 layer game mode. Two sets of controls are used and players are trying to both avoid enemies while gathering points.
# This game mode includes the same rules as single player.

import pygame,random,sys,time,os
from os import path

pygame.init()

APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))


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

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Mario Kart Remastered")
clock = pygame.time.Clock()

car_width = 73
car_width2 = 73

graphics = 0
graphics2=0
score = -10
score2 = -10

carimg = pygame.image.load(os.path.join(APP_FOLDER, 'Mario\mario_straight.png'))
carrightimg = pygame.image.load(os.path.join(APP_FOLDER,'Mario\mario_right_turn.png'))
carleftimg = pygame.image.load(os.path.join(APP_FOLDER, 'Mario\mario_left_turn.png'))
trackimg = pygame.image.load(os.path.join(APP_FOLDER, 'Pictures\Track_2.png')).convert()
goombaimg= pygame.image.load(os.path.join(APP_FOLDER,'Goomba\Vector-goomba.png'))
koopaimg = pygame.image.load(os.path.join(APP_FOLDER, 'Koopa\Vector-koopa.png'))
bombimg = pygame.image.load(os.path.join(APP_FOLDER, 'Bomb\Vector-bomb.png'))

koopasound = pygame.mixer.Sound(os.path.join(APP_FOLDER, 'Koopa\Koopa_crash.wav'))
bombsound = pygame.mixer.Sound(os.path.join(APP_FOLDER,'Bomb\Bomb_crash.wav'))
goombasound = pygame.mixer.Sound(os.path.join(APP_FOLDER, 'Goomba\Goomba_crash.wav'))
gameoversound = pygame.mixer.Sound(os.path.join(APP_FOLDER,'Music\Gameover_sound.wav'))

carimg2 = pygame.image.load(os.path.join(APP_FOLDER,'Luigi\luigi_straight.png'))
carrightimg2 = pygame.image.load(os.path.join(APP_FOLDER,'Luigi\luigi_right_turn.png'))
carleftimg2 = pygame.image.load(os.path.join(APP_FOLDER,'Luigi\luigi_left_turn.png'))

goombaspeed = 4
goombax=(random.randint(50, 677))
goombay=(600)
goombawidth=65
goombaheight=65

koopaspeed = 5
koopax = (random.randint(50, 677))
koopay = (600)
koopawidth = 65
koopaheight = 65

bombspeed = 6
bombx=(random.randint(50, 677))
bomby=(600)
bombwidth=65
bombheight=65

road_y = 0

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

def playagain():
    os.startfile('Play Again Screen.py')
    
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

def text_display(msg, x, y):
    Smalltext = pygame.font.SysFont("comicsansms", 25)
    textSurf, textRect = text_objects(msg, Smalltext)
    textRect.center = ((x), (y))
    gameDisplay.blit(textSurf, textRect)

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
                game(goombay,goombax,score,goombaspeed,koopay,koopax,koopaspeed,bomby,bombx,bombspeed,graphics,road_y)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    Smalltext = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, Smalltext)
    textRect.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(textSurf, textRect)

def crash(sound):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(sound)
    pygame.mixer.Sound.play(gameoversound)
    font = pygame.font.SysFont("comicsansms", 25)
    text=font.render('You died '+str(score - 5),True,white)
    gameDisplay.blit(text,(350,600))
    
def scorekeeper(score):
    font = pygame.font.SysFont("comicsansms", 25)
    text=font.render('P1 Score '+str(score - 5),True,white)
    gameDisplay.blit(text,(100,500))

def scorekeeper2(score2):
    font = pygame.font.SysFont("comicsansms", 25)
    text=font.render('P2 Score '+str(score2 - 5),True,white)
    gameDisplay.blit(text,(550,500))

def goomba(x,y):
    gameDisplay.blit(goombaimg,(x,y))

def koopa(x,y):
    gameDisplay.blit(koopaimg,(x,y))

def bomb(x,y):
    gameDisplay.blit(bombimg, (x,y))

def right_turn_display(x,y):
    gameDisplay.blit(carrightimg, (x,y))

def left_turn_display(x,y):
    gameDisplay.blit(carleftimg, (x,y))

def car_display(x,y):
    gameDisplay.blit(carimg, (x,y))

def right_turn_display2(x,y):
    gameDisplay.blit(carrightimg2, (x,y))

def left_turn_display2(x,y):
    gameDisplay.blit(carleftimg2, (x,y))

def car_display2(x,y):
    gameDisplay.blit(carimg2, (x,y))


def game(goombay,goombax,score,goombaspeed,koopay,koopax,koopaspeed,bomby,bombx,bombspeed,graphics,road_y,graphics2,score2):
    gameDisplay.fill(black)
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(APP_FOLDER, 'Music\Track_music.wav'))
    pygame.mixer.music.play()

    display_message("Ready?",400,50)
    time.sleep(1)
    display_message("Set",400,300)
    time.sleep(1)
    display_message("Go!",400,550)
    time.sleep(0.5)
    
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x2 = (display_width * 0.45)
    y2 = (display_height * 0.8)

    x_change = 0
    x2_change = 0
    exit_game = False
    while not exit_game:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                exit_game = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                    graphics = 1
                    
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
                    graphics = 2

                if event.key == ord('a'):
                    x2_change = -10
                    graphics2 = 1
                    
                elif event.key == ord('d'):
                    x2_change = 10
                    graphics2 = 2
    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    graphics = 0
                if event.key == ord('a') or event.key == ord('d'):
                    graphics2 = 0
                    x2_change= 0

        x += x_change
        x2 += x2_change
        
        if x < 50:
            x = 50
        elif x > display_width - car_width - 50:
            x = display_width - car_width - 50
        

        if x2<50:
            x2=50
        elif x2>display_width-car_width-50:
            x2=display_width-car_width-50

        rel_y = road_y % trackimg.get_rect().height
        gameDisplay.blit(trackimg, (0,rel_y - trackimg.get_rect().height))
        if rel_y < display_height:
            gameDisplay.blit(trackimg,(0,rel_y))
        road_y += 3

        if graphics == 0:
            car_display(x,y)
        elif graphics == 1:
            left_turn_display(x,y)
        else:
            right_turn_display(x,y)

        if graphics2==0:
            car_display2(x2,y2)

        elif graphics2==1:
            left_turn_display2(x2,y2)

        else:
            right_turn_display2(x2,y2)
            

        goomba(goombax,goombay)
        goombay += goombaspeed

        koopa(koopax,koopay)
        koopay += koopaspeed

        bomb(bombx, bomby)
        bomby += bombspeed

        if koopax == goombax or koopax == bombx or goombax == bombx:
            goomba(goombax,goombay)
            goombay += goombaspeed

            koopa(koopax,koopay)
            koopay += koopaspeed
            
            bomb(bombx, bomby)
            bomby += bombspeed

        if goombay > 600:
            goombay=0
            goombax=(random.randint(50, 677))
            if y<1000:
                score=score+5
                if (score)%100 == 0:
                    goombaspeed = goombaspeed + 2
                    koopaspeed = koopaspeed + 2
                    bombspeed = bombspeed + 2
            else:
                score=score
                
            if y2<1000:
                score2=score2+5
                if (score)%100 == 0:
                    goombaspeed = goombaspeed + 2
                    koopaspeed = koopaspeed + 2
                    bombspeed = bombspeed + 2
            else:
                score2=score2

        if y<goombay+goombaheight:
            if x>goombax and x<goombax+goombawidth or x+car_width>goombax and x+car_width<goombax+goombawidth:
                y=1000
                crash(goombasound)
                
        if y2<goombay+goombaheight:
            if x2>goombax and x2<goombax+goombawidth or x2+car_width2>goombax and x2+car_width2<goombax+goombawidth:
                y2=1000
                crash(goombasound)
        
        if koopay > 600:
            koopay=0
            koopax=(random.randint(50, 677))
            if y<1000:
                score=score+5
                if (score)%100 == 0:
                    goombaspeed = goombaspeed + 2
                    koopaspeed = koopaspeed + 2
                    bombspeed = bombspeed + 2
            else:
                score=score

            if y2<1000:
                score2=score2+5
                if (score)%100 == 0:
                    goombaspeed = goombaspeed + 2
                    koopaspeed = koopaspeed + 2
                    bombspeed = bombspeed + 2
            else:
                score2=score2

        if y<koopay+koopaheight:
            if x>koopax and x<koopax+koopawidth or x+car_width>koopax and x+car_width<koopax+koopawidth:
                y=1000
                crash(koopasound)
        if y2<koopay+koopaheight:
            if x2>koopax and x2<koopax+koopawidth or x2+car_width2>koopax and x2+car_width2<koopax+koopawidth:
                y2=1000
                crash(koopasound)

        if bomby > 600:
            bomby=0
            bombx=(random.randint(50, 677))
            if y<1000:
                score=score+5
                if (score)%100 == 0:
                    goombaspeed = goombaspeed + 2
                    koopaspeed = koopaspeed + 2
                    bombspeed = bombspeed + 2
            else:
                score=score
            if y2<1000:
                score2=score2+5

                if (score)%100 == 0:
                    goombaspeed = goombaspeed + 2
                    koopaspeed = koopaspeed + 2
                    bombspeed = bombspeed + 2
            else:
                score2=score2
           
        if y<bomby+bombheight:
            if x>bombx and x<bombx+bombwidth or x+car_width>bombx and x+car_width<bombx+bombwidth:
                y=1000
                crash(bombsound)
        if y2<bomby+bombheight:
            if x2>bombx and x2<bombx+bombwidth or x2+car_width>bombx and x2+car_width<bombx+bombwidth:
                y2=1000
                crash(bombsound)

        if y2 == 1000 and y < 1000:
            pygame.mixer.music.play()
            y2 = 1001
            
        if y2 < 1000 and y == 1000:
            pygame.mixer.music.play()
            y = 1001

        if y2 == 1001 and y == 1000 or y2 == 1000 and y == 1001:
            font = pygame.font.SysFont("comicsansms", 25)
            if score>score2:
                text=font.render('Player 1 has won the game ',True,white)
                gameDisplay.blit(text,(250,200))
                pygame.display.update()
                time.sleep(3)
                playagain()
                quit()
            elif score2>score:
                text=font.render('Player 2 has won the game ',True,white)
                gameDisplay.blit(text,(250,200))
                pygame.display.update()
                time.sleep(3)
                playagain()
                quit()
            else:
                text=font.render('It was a tie! ',True,white)
                gameDisplay.blit(text,(350,300))
                pygame.display.update()
                time.sleep(3)
                playagain()
                quit()
                
                         
        scorekeeper(score)
        scorekeeper2(score2)
        pygame.display.update()
        clock.tick(60)

while True:
    game(goombay,goombax,score,goombaspeed,koopay,koopax,koopaspeed,bomby,bombx,bombspeed,graphics,road_y,graphics2,score2)
    pygame.quit()
    quit()

