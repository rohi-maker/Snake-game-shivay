import pygame
import random
snk_length=1
snk_list=[]
pygame.mixer.init()
def display_score(gameWindow,font,text,colour):
    t = font.render(text, True, colour)
    gameWindow.blit(t,(10,10))
def drawsnake(gameWindow,red,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,red,[x,y,snake_size,snake_size])

        
def gameloop():
    

    global snk_length
    global snk_list
    pygame.init()
    screen_width=900
    screen_height=600
    snake_x=40
    snake_y=40
    snake_size=15
    x_velocity=0
    y_velocity=0
    fps=35
    white=(255,255,255)
    red=(255,0,0)
    green=(0,255,0)
    fruiet_x=random.randint(1,850)
    fruiet_y=random.randint(1,570)
    fruiet_size=12
    gameWindow=pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("SNAKE GAME BY CODE-WITH-SHIVAY")
    pygame.display.set_icon(gameWindow)
    
    pygame.display.update()
    game_exit=False
    game_over=False
    value=1
    score=0
    font = pygame.font.Font(None,30)
    clock=pygame.time.Clock()
    while not game_exit:
        if game_over:
            gimg=pygame.image.load("gameover.png").convert_alpha()
            gameWindow.blit(gimg,(0,0))
            pygame.display.update()
            for event in pygame.event.get():
                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        return 
                        
    
        else:
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        y_velocity=-10    
                        x_velocity=0    
                    if event.key == pygame.K_RIGHT:
                        x_velocity=10 
                        y_velocity=0
                    if event.key == pygame.K_LEFT:
                        x_velocity=-10     
                        y_velocity=0            
                    if event.key == pygame.K_DOWN:
                        y_velocity=10
                        x_velocity=0
                    if event.key == pygame.K_SPACE:
                        value=value+1
                        pygame.mixer.music.load("naagsong.mp3")
                        pygame.mixer.music.play()

            if value==1:
                wimg=pygame.image.load("welcome.png").convert_alpha()
                gameWindow.blit(wimg,(0,0))
                pygame.display.update()
            else:
                
                snake_x=snake_x+x_velocity
                snake_y=snake_y+y_velocity
                gameWindow.fill(white)
                rimg=pygame.image.load("snake-1940343_640.png")
                rimg=pygame.transform.scale(rimg, (screen_width,screen_height)).convert_alpha()
                gameWindow.blit(rimg,(1,1))
                
                
                if abs(snake_x-fruiet_x)<10 and abs(snake_y-fruiet_y)<10: # if food is eaten
                    fruiet_x=random.randint(1,850)
                    fruiet_y=random.randint(1,570)
                    score=score+10
                    snk_length=snk_length+3
                    
                head=[]
                head.append(snake_x)
                head.append(snake_y)
                snk_list.append(head)
                if len(snk_list)>snk_length:
                    del snk_list[0]
                drawsnake(gameWindow,red,snake_size) 
                pygame.draw.rect(gameWindow,green,[fruiet_x,fruiet_y,fruiet_size,fruiet_size])
                display_score(gameWindow,font,"Score="+str(score),red)
                if snake_x>=screen_width or snake_x<=0 or snake_y>=screen_height or snake_y<=0:
                    game_over=True
                    
                if head in snk_list[:-1]:
                    game_over=True
                    
                pygame.display.update()
                
                    
                


                clock.tick(fps)

    pygame.quit()
    quit()
if __name__ == '__main__':
    
    gameloop()
    