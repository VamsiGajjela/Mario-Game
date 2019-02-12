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

carimg = pygame.image.load('Luigi\luigi_straight.png')
carrightimg = pygame.image.load('Luigi\luigi_right_turn.png')
carleftimg = pygame.image.load('Luigi\luigi_left_turn.png')
trackimg = pygame.image.load('Pictures\Track_2.png').convert()
goombaimg= pygame.image.load('Goomba\Vector-goomba.png')
koopaimg = pygame.image.load('Koopa\Vector-koopa.png')
bombimg = pygame.image.load('Bomb\Vector-bomb.png')

koopasound = pygame.mixer.Sound('Koopa\Koopa_crash.wav')
bombsound = pygame.mixer.Sound('Bomb\Bomb_crash.wav')
goombasound = pygame.mixer.Sound('Goomba\Goomba_crash.wav')
gameoversound = pygame.mixer.Sound('Music\Gameover_sound.wav')

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

def high_score():
    os.startfile('High Score Screen.py')
    
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

def crash(score, sound):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(sound)
    gameDisplay.blit(trackimg,(0,0))
    display_message('Game Over!',400,20)
    pygame.mixer.Sound.play(gameoversound)
    message('Your Score: ' + str(score))
    time.sleep(4)  

def scorekeeper(score):
    font = pygame.font.SysFont("comicsansms", 25)
    text=font.render('Score '+str(score),True,white)
    gameDisplay.blit(text,(100,500))

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


def game(goombay,goombax,score,goombaspeed,koopay,koopax,koopaspeed,bomby,bombx,bombspeed,graphics,road_y):
    gameDisplay.fill(black)
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Music\Track_music.wav')
    pygame.mixer.music.play()

    display_message("Ready?",400,50)
    time.sleep(1)
    display_message("Set",400,300)
    time.sleep(1)
    display_message("Go!",400,550)
    time.sleep(0.5)
    
    x = (display_width * 0.45)
    y = (display_height * 0.8)


    dir = path.dirname(__file__)
    with open(path.join(dir, highscore_file), 'r') as f:
        try:
            highscore = f.read()
        except:
            highscore = f.read()
    x_change = 0

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
    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    graphics = 0

        x += x_change
        
        if x < 50:
            x = 50
        elif x > display_width - car_width - 50:
            x = display_width - car_width - 50    
                
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
            score=score+5
            if (score)%100 == 0:
                goombaspeed = goombaspeed + 2
                koopaspeed = koopaspeed + 2
                bombspeed = bombspeed + 2
        if y<goombay+goombaheight:
            if x>goombax and x<goombax+goombawidth or x+car_width>goombax and x+car_width<goombax+goombawidth:
                if score > int(highscore):                          
                    highscore = score                               
                    with open(path.join(dir, highscore_file), 'w') as f:   
                        f.write(str(score))
                crash(score,goombasound)
                time.sleep(2)
                high_score()
                break
        
        if koopay > 600:
            koopay=0
            koopax=(random.randint(50, 677))
            score=score+5
            if (score)%100 == 0:
                koopaspeed = koopaspeed + 2
                goombaspeed = goombaspeed + 2
                bombspeed = bombspeed + 2
        if y<koopay+koopaheight:
            if x>koopax and x<koopax+koopawidth or x+car_width>koopax and x+car_width<koopax+koopawidth:
                if score > int(highscore):                          
                    highscore = score                               
                    with open(path.join(dir, highscore_file), 'w') as f:   
                        f.write(str(score))
                crash(score,koopasound)
                time.sleep(2)
                high_score()
                break
            
        if bomby > 600:
            bomby=0
            bombx=(random.randint(50, 677))
            score=score+5
            if (score)%100 == 0:
                koopaspeed = koopaspeed + 2
                goombaspeed = goombaspeed + 2
                bombspeed = bombspeed + 2
        if y<bomby+bombheight:
            if x>bombx and x<bombx+bombwidth or x+car_width>bombx and x+car_width<bombx+bombwidth:
                if score > int(highscore):                          
                    highscore = score                               
                    with open(path.join(dir, highscore_file), 'w') as f:   
                        f.write(str(score))
                crash(score,bombsound)
                time.sleep(2)
                high_score()
                break
            
        scorekeeper(score)
        pygame.display.update()
        clock.tick(60)

while True:
    game(goombay,goombax,score,goombaspeed,koopay,koopax,koopaspeed,bomby,bombx,bombspeed,graphics,road_y)
    pygame.quit()
    quit()
