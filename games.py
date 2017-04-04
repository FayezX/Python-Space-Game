import pygame
import time
import random

pygame.init()
rocket_sound = pygame.mixer.Sound('blast.wav')
laser_sound = pygame.mixer.Sound('Laser_Gun.wav')
crash_sound = pygame.mixer.Sound('crash.wav')
theme_sound = pygame.mixer.Sound('Bike_Rides.wav')

display_width = 800 #was 800
display_height = 600 #was 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('fast and furi0us')
clock = pygame.time.Clock()

car_img = pygame.image.load('plane.png')
bullet_img = pygame.image.load('bullet.png')
space_img = pygame.image.load('space.png').convert()

def score(number):
    font = pygame.font.Font(None,30)
    text = font.render("Score: " + str(number),True,red)
    gameDisplay.blit(text,(700,0))

def shoot(x,y):
    gameDisplay.blit(bullet_img,(x,y))
    pygame.mixer.Sound.play(laser_sound)
    pygame.display.update()

def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color, [thingx,thingy,thingw,thingh])

def rocket(x,y):
    gameDisplay.blit(car_img,(x,y))

def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()

def message_display(text):
    message = pygame.font.Font('freesansbold.ttf',90)
    textsurf, textrect = text_objects(text,message)
    textrect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(2)
    game_loop2()

def crash():
    pygame.mixer.Sound.stop(theme_sound)
    message_display("FtheLaw")


def game_loop():

    x = (display_width * 0.45)
    y = (display_height * .65)

    x_change = 0
    y_change = 0

    thing_startx = random.randrange(0,display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 10
    thing_height = 100

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            print(event)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                    pygame.mixer.Sound.play(rocket_sound)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP:
                    x_change = 0
                    y_change = 0
                        
    
        x += x_change
        y += y_change
        
        gameDisplay.fill(white)
        
        things(thing_startx,thing_starty,thing_width,thing_height,red)
        thing_starty += thing_speed
        
        car(x,y)
        
        if x > display_width-100 or x < 0-60:
            crash()
                
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
                
        
        pygame.display.update()
        clock.tick(60)


def game_loop2():
    
    x = (display_width * 0.45)
    y = (display_height * .65)
    gun_y = y - 100
    gun_x = 0
    
    x_change = 0
    y_change = 0
    gun_y_change = 0
    
    thing_startx = random.randrange(0,display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 50
    thing_height = 50
    
    dodged = 0
    
    game_exit = False
    
    pygame.mixer.Sound.play(theme_sound)
    
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #print(event)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -7
                elif event.key == pygame.K_RIGHT:
                    x_change = 7
                elif event.key == pygame.K_UP:
                    y_change = -7
                    pygame.mixer.Sound.play(rocket_sound)
                elif event.key == pygame.K_a:
                    gun_y_change = -25
                    gun_x = x - 8.5
                
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP:
                    x_change = 0
                    y_change = 0

        x += x_change
        y += y_change
        gun_y += gun_y_change
        
        ##gameDisplay.fill(white)
        gameDisplay.blit(space_img,[0,0])
        
        things(thing_startx,thing_starty,thing_width,thing_height,green)
        thing_starty += thing_speed
        rocket(x,y)
        score(dodged)
        
        if(gun_y_change is not 0):
            shoot(gun_x,gun_y)
            
        if(gun_y < -150):
            gun_y_change = 0
            gun_y = y - 100
            pygame.mixer.Sound.stop(laser_sound)
        
        if x > display_width-100 or x < 0-60:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width = random.randrange(10,100)
            thing_height = random.randrange(10,100)

        if y < thing_starty+thing_height-60:
            if x+100 > thing_startx and x+100 < thing_startx+thing_width:
                pygame.mixer.Sound.play(crash_sound)
                crash()

        pygame.display.update()
    clock.tick(60) #was 60

if __name__ == '__main__':
    game_loop2()
    pygame.quit()
    quit()

