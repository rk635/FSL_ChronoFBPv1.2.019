import pygame
import time as t 
from playsound import playsound
import random
from pygame.locals import *

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0 ,0)
lightRed = (200, 0, 0)
green = (0, 255, 0)
lightGreen = (0, 200, 0)
blue = (0, 0, 255)

counter = 5
gameExit = False
gameStarted = False
countDown = True

titleFont = pygame.font.Font('freesansbold.ttf', 32) 
normalFont = pygame.font.Font('freesansbold.ttf', 18)
timerFont = pygame.font.SysFont('Consolas', 70)

titleText = titleFont.render('Field Blood Pressure Simulator', True, black) 
titleTextRect = titleText.get_rect()  
titleTextRect.center = (800 // 2, 400 // 2) 

directionText = normalFont.render('Field Blood Pressure Simulator and this is how the game goes', True, black)
directionTextRect = directionText.get_rect()  
directionTextRect.center = (800 // 2, 600 // 2) 

startButtonText = normalFont.render('Start', True, black) 
startButtonTextRect = startButtonText.get_rect()  
startButtonTextRect.center = (200, 475) 

stopButtonText = normalFont.render('Stop', True, black)
stopButtonTextRect = stopButtonText.get_rect()  
stopButtonTextRect.center = (600, 475) 

timerText = timerFont.render(str(counter), True, black)
timerTextRect = directionText.get_rect()  
timerTextRect.center = (650, 300) 

mainMenu = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

pygame.display.set_caption('Field Blood Pressure Simulator')

while not gameExit:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameExit = True

    mouseMovement = pygame.mouse.get_pos()
    mousePress = pygame.mouse.get_pressed()

    mainMenu.fill(white)
    mainMenu.blit(titleText, titleTextRect)
    mainMenu.blit(directionText, directionTextRect)

    if 150+100 > mouseMovement[0] > 150 and 450+50 > mouseMovement[1] > 450:
        pygame.draw.rect(mainMenu, lightGreen, (150, 450, 100, 50))
        if mousePress[0] == 1:
            print('Start Button Pressed')
            gameStarted = True
            while gameStarted:
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        
                        gameStarted = False
                        gameExit = True
                
                mainMenu.fill(white)
                pygame.display.update()
                
                while countDown:
                
                    for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            
                            countDown = False
                            gameStarted = False
                            gameExit = True
                    
                    if counter == 0:
                        countDown = False
                    
                    else:
                        timerText = timerFont.render(str(counter), True, black)
                        mainMenu.blit(timerText, timerTextRect)
                        print(str(counter))
                        pygame.display.update()
                        
                        counter -= 1
                        mainMenu.fill(white)
                    pygame.time.wait(1000)
                
                timerText = timerFont.render('Begin!', True, black)
                mainMenu.blit(timerText, timerTextRect)
                pygame.display.update()
                
                pygame.time.wait(3000)
                song_number = random.randint(1,5)
                start_time = t.time()
                playsound('audio_files/' + str(song_number) + '.mp3', False)

    else:
        pygame.draw.rect(mainMenu, green, (150, 450, 100, 50))
            
    mainMenu.blit(startButtonText, startButtonTextRect)

    if 550+100 > mouseMovement[0] > 550 and 450+50 > mouseMovement[1] > 450:
        pygame.draw.rect(mainMenu, lightRed, (550, 450, 100, 50))
        if mousePress[0] == 1:
            gameExit = True
    else:
        pygame.draw.rect(mainMenu, red, (550, 450, 100, 50))
            
    mainMenu.blit(stopButtonText, stopButtonTextRect)
        
    pygame.display.update()

pygame.quit()
    
    


