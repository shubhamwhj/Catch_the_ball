import pygame, sys, random

#initialize pygame to  use it's functions
pygame.init()
clock=pygame.time.Clock()

#create a window where game will Run
screen = pygame.display.set_mode((400,400))
#title 
pygame.display.set_caption("Catch the Ball")

#load images
background_image = pygame.image.load("bg.png").convert()
plr_img = pygame.image.load("player.png").convert_alpha()
plr_img=pygame.transform.smoothscale(plr_img,(60,90))
ball_image = pygame.image.load("ball.png").convert_alpha()
ball_image=pygame.transform.smoothscale(ball_image,(40,40))
over_img=pygame.image.load("over.png").convert_alpha()
over_img=pygame.transform.smoothscale(over_img,(200,100))

#creating objects of game
ball=pygame.Rect(200,0,40,40)
player=pygame.Rect(100,310,60,90)

speed=0



while True:
  
  screen.blit(background_image,[0,0])
  #event loop to check which key is print
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    #use events to move the player   
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT:
            speed=5
        if event.key==pygame.K_LEFT:
            speed=-5
  
  player.x=player.x+speed  
    
  #code for ball falling
  ball.y=ball.y+5
  if(ball.colliderect(player)):
      ball.y=0
      ball.x=random.randint(0, 360)
  if(ball.y>400):
      screen.blit(over_img,[100,100])
      
      
  screen.blit(plr_img,player)
  screen.blit(ball_image,ball)
  
  pygame.display.flip()
  clock.tick(30)