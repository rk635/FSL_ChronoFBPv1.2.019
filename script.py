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
listNumber = 1

start_user = []
stop_user = []
start_track1 = [10.416, 62.754, 100.821, 163.337, 282.550]
stop_track1 = [22.406, 77.271, 112.811, 177.860, 294.551]
start_track2 = [24.045, 51.677, 125.068, 241.606, 277.445]
stop_track2 = [38.562, 63.667, 137.057, 256.129, 289.446]
start_track3 = [47.764, 103.014, 126.931, 185.108, 233.982]
stop_track3 = [62.282, 115.003, 138.921, 197.108, 248.505]
start_track4 = [15.298, 80.803, 149.296, 215.345, 280.326]
stop_track4 = [27.918, 95.321, 161.285, 229.868, 292.327]
start_track5 = [80.803, 109.749, 208.659, 240.591, 280.326]
stop_track5 = [95.321, 121.738, 220.648, 255.114, 292.327]

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
                
                #TODO Polish up Countdown
                while countDown:
                
                    for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            
                            countDown = False
                            gameStarted = False
                            gameExit = True
                    
                    if counter == 0:
                        #TODO trying moving all this code into the if statement
                        timerText = timerFont.render('Begin!', True, black)
                        mainMenu.blit(timerText, timerTextRect)
                        pygame.display.update()
                        pygame.time.wait(2000)
                        
                        pygame.display.update
                        print('screen black')
                        song_number = random.randint(1,5)
                        start_time = t.time()
                        pygame.mixer.init()
                        pygame.mixer.music.load('audio_files/' + str(song_number) + '.mp3')
                        pygame.mixer.music.play()
                        print('song playing')
                        countDown = False
                    
                    else:
                        timerText = timerFont.render(str(counter), True, black)
                        mainMenu.blit(timerText, timerTextRect)
                        print(str(counter))
                        pygame.display.update()
                        counter -= 1
                        mainMenu.fill(white)
                        pygame.time.wait(1000)
                
                print('audio is continuing to play')
                while True:
                    
                    #TODO code for when it is pressed alternate between lists
                    for event in pygame.event.get():

                        if event.type == pygame.KEYDOWN:

                            if event.key == pygame.K_SPACE:
                                
                                
                                end_time = t.time()

                                time_stamp = end_time - start_time

                                print('spacebar pressed' + str(time_stamp))

                                
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