import pygame
import time
import random

pygame.init() # returns a tuple of successful and unsuccessful initialisations

#  VARIABLES

# to define colors you give the RGB values, can be given in a list or a tuple

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

 
display_width = 800
display_height = 600
clock = pygame.time.Clock()
block_size = 10
FPS = 30


# computer screens have a backlight, 

# surface, background or canvas

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')

#  pygame.display.flip() is interchangeable with display.update() when used with no parameters, updates the entire surface

font = pygame.font.SysFont(None, 25)


# FUNCTIONS

def snake(block_size, snake_list):
    for XnY in snake_list:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

    

def message_to_screen(msg, color): 
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])


def game_loop():


    pygame.mixer.init()
    pygame.mixer.music.load('snake.mp3')
    pygame.mixer.music.play(-1)

    snake_list = []
    snake_length = 10
    game_exit = False
    game_over = False
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0

    rand_apple_x = round(random.randrange(0, display_width-block_size)/10)*10
    rand_apple_y = round(random.randrange(0, display_height-block_size)/10)*10


    

    #  GAME LOOP
    while not game_exit:

        while game_over == True:
            gameDisplay.fill(white)
            message_to_screen('Game Over. Press C to play again or Q to quit.', red)
            pygame.display.update()

            # event loop

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    elif event.key == pygame.K_c:
                        game_loop()


        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0 
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0


            # STOP MOVING WHEN KEYUP
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #         lead_x_change = 0
            


    # EVENT HANDLING AND THEN A GROUP OF LOGIC STATEMENTS, THEN GRAPHICS RENDERING AND THEN UPDATE THE DISPLAY
    #  THIS ALL HAPPENS EVERY FRAME PER SCOND, SO OPTIMISATION MAKES SENSE

    # LOGIC

        if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
            game_over = True
    
        
        lead_x += lead_x_change
        lead_y += lead_y_change



        # draw everything and then render to save resources
        gameDisplay.fill(white)

        # apple

        pygame.draw.rect(gameDisplay, red, [rand_apple_x, rand_apple_y, block_size, block_size])


        # snake


        
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        snake(block_size, snake_list)
        # alternative to using pygame.draw.rect. fill can be graphics accelerated.
        # gameDisplay.fill(black, rect=[200, 200, 50, 50])


        # draw everything and then render to save resources
        pygame.display.update()


        if lead_x == rand_apple_x and lead_y == rand_apple_y:
            rand_apple_x = round(random.randrange(0, display_width-block_size)/10)*10
            rand_apple_y = round(random.randrange(0, display_height-block_size)/10)*10

        # specify the frames per second that you want to have
        clock.tick(FPS)
    # use sprites or draw with pygame to put things on the screen (using coordinates)

    #  render font, blit the font, then update the sceen
    message_to_screen('GAME OVER', red)
    pygame.display.update()
    time.sleep(2)
    pygame.quit() # unintialises pygame
    quit() # exits out of python


game_loop()


# vid 18