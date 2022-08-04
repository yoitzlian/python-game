import pygame 
from pygame import mixer
from paddle import Paddle
from ball import Ball

pygame.init()

#colors
pygame.display.set_caption("Main Menu")

background = pygame.image.load('background.png') 
BLACK = (0,0,0)
WHITE = (255,255,255)

#background soundw
mixer.music.load('background.wav')
mixer.music.play(-1)

#Open Window
size = (700, 500)
screen = pygame.display.set_mode(size )
pygame.display.set_caption("Lian's Pong Game")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE,10,10)
ball.rect.x = 400
ball.rect.y = 400 

#Sprites
all_sprites_list = pygame.sprite.Group()

#adding paddles
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

#The loop will carry the user exit the game
carryOn = True

#The clock will be used to control how fast screen updates
clock = pygame.time.Clock()

#Initialise player scores
scoreA = 0
scoreB = 0

#Main program loop

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #If user click close
            carryOn = False #Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x: #Pressing X will quit the game
                carryOn=False

                    
#Moving Paddles

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)
    #if keys[pygame.K_SPACE]
    #set certain value to true/freeze the screen

            #Game Logic
    all_sprites_list.update() 

#Cheking the bounce of the ball
    if ball.rect.x>=690:
        SoundS = mixer.Sound("POINT.wav")
        scoreA+=1
        SoundS.play()
        if scoreA == 5:
            image = pygame.image.load("youwin.png")
            image = pygame.transform.scale(image, (700,500))
            screen.blit(image, (0,0))
            pygame.display.flip()
            pygame.time.wait(3000)
            carryOn = False
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        scoreB+=1
        SoundS = mixer.Sound("POINT.wav")
        SoundS.play()
        if scoreB == 5:
            image = pygame.image.load("youwin.png")
            image = pygame.transform.scale(image, (700,500))
            screen.blit(image, (0,0))
            pygame.display.flip()
            pygame.time.wait(3000)
            carryOn = False
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]   
    
        #detecting collision
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()
        ball_Sound = mixer.Sound('laser.wav')
        ball_Sound.play()

        #   #drawning colors
            #SCreen Black
    screen.fill(BLACK)
            #Drawing the net 
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    #drawing sprites
    all_sprites_list.draw(screen)

#Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420,10))
 
    #Updating the screen
    pygame.display.flip()

    #FPS
    clock.tick(60)

    #Once we exited the main program loop we can stop engine:
pygame.quit()