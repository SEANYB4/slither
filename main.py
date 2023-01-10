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
block_size = 20
FPS = 30

direction = 'right'

# apple
apple_thickness = 30

# computer screens have a backlight, 

# surface, background or canvas

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')


icon = pygame.image.load('snakehead.png')

# best size for icons is 32 x 32 
pygame.display.set_icon(icon)

img = pygame.image.load('snakehead.png')

apple_img = pygame.image.load('apple.png')

#  pygame.display.flip() is interchangeable with display.update() when used with no parameters, updates the entire surface

smallfont = pygame.font.SysFont('comicsansms', 25)
mediumfont = pygame.font.SysFont('comicsansms', 50)
largefont = pygame.font.SysFont('comicsansms', 80)




# FUNCTIONS


def pause():

    paused = True

    while paused:
        for event in  


def score(score):

    text = smallfont.render("Score: " + str(score), True, white)
    gameDisplay.blit(text, [0, 0])


def game_intro():

    intro = True
    while intro:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()


        gameDisplay.fill(white)
        message_to_screen("Welcome to Slither",
                            green,
                            -100,
                            'large')
        message_to_screen('The objective of the game is to eat red apples',
                            black,
                            -30)

        message_to_screen('The more apples you eat, the longer your snake gets.',
                            black,
                            10)


        message_to_screen('If you run into yourself or the edges, then game over!',
                            black,
                            50)

        message_to_screen('Press C to play or Q to quit.',
        black,
        180)

        pygame.display.update()
        clock.tick(15)




def snake(block_size, snake_list):


    if direction == 'right':
        head = pygame.transform.rotate(img, 270)

    elif direction == 'left':
        head = pygame.transform.rotate(img, 90)

    elif direction == 'up':
        head = img

    elif direction == 'down':
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snake_list[-1][0], snake_list[-1][1]))
    for XnY in snake_list[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])



def rand_apple_gen():


    rand_apple_x = round(random.randrange(0, display_width-apple_thickness))
    rand_apple_y = round(random.randrange(0, display_height-apple_thickness))

    return rand_apple_x, rand_apple_y
    

def text_objects(text, color, size):
    if size == 'small':
        text_surface = smallfont.render(text, True, color)

    elif size == 'medium':
        text_surface = mediumfont.render(text, True, color)

    elif size == 'large':
        text_surface = largefont.render(text, True, color)


    return text_surface, text_surface.get_rect()



    

def message_to_screen(msg, color, y_displace=0, size = 'small'): 
    # screen_text = font.render(msg, True, color)
    # gameDisplay.blit(screen_text, [display_width/2, display_height/2])
    text_surface, text_rect = text_objects(msg, color, size)
    text_rect.center = (display_width/2), (display_height/2) + y_displace
    gameDisplay.blit(text_surface, text_rect)

def game_loop():
    # global keyword allows you to modify a variable within a function
    global direction 

    pygame.mixer.init()
    pygame.mixer.music.load('snake.mp3')
    # pygame.mixer.music.play(-1)

    snake_list = []
    snake_length = 1
    game_exit = False
    game_over = False
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0



    rand_apple_x, rand_apple_y = rand_apple_gen()
    

    #  GAME LOOP
    while not game_exit:

        while game_over == True:
            gameDisplay.fill(white)
            message_to_screen('Game Over', red, y_displace = -50, size='large')
            message_to_screen("Press C to play again or Q to quit.", black, 5, size='medium')
            pygame.display.update()

            # event loop

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False

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
                    direction = 'left'
                    lead_x_change = -block_size
                    lead_y_change = 0 
                elif event.key == pygame.K_RIGHT:
                    direction = 'right'
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = 'up'
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = 'down'
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
        gameDisplay.fill(black)

        
        
        gameDisplay.blit(apple_img, [rand_apple_x, rand_apple_y])
        # pygame.draw.rect(gameDisplay, red, [rand_apple_x, rand_apple_y, apple_thickness, apple_thickness])


        # snake


        
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]


        for point in snake_list[:-1]:
            
            if point == snake_head:
                game_over = True

        snake(block_size, snake_list)
        # alternative to using pygame.draw.rect. fill can be graphics accelerated.
        # gameDisplay.fill(black, rect=[200, 200, 50, 50])


        score((snake_length-1) * 10)

        # draw everything and then render to save resources
        pygame.display.update()


        # COLLISION DETECTION

        # if lead_x == rand_apple_x and lead_y == rand_apple_y:
        #     rand_apple_x = round(random.randrange(0, display_width-block_size)/10)*10
        #     rand_apple_y = round(random.randrange(0, display_height-block_size)/10)*10
        #     snake_length += 1

        
        # if (lead_x >= rand_apple_x and lead_x <= (rand_apple_x + apple_thickness)):
        #     if (lead_y >= rand_apple_y and lead_y <= (rand_apple_y + apple_thickness)):
        #         rand_apple_x = round(random.randrange(0, display_width-block_size))
        #         rand_apple_y = round(random.randrange(0, display_height-block_size))
        #         snake_length += 1


        if lead_x > rand_apple_x and lead_x < rand_apple_x + apple_thickness or (lead_x + block_size > rand_apple_x and lead_x + block_size < rand_apple_x + apple_thickness):
            if lead_y > rand_apple_y and lead_y < rand_apple_y + apple_thickness or (lead_y + block_size > rand_apple_y and lead_y + block_size < rand_apple_y + apple_thickness):
                rand_apple_x, rand_apple_y = rand_apple_gen()
                snake_length += 1
                
 

        # specify the frames per second that you want to have
        clock.tick(FPS)
    # use sprites or draw with pygame to put things on the screen (using coordinates)

    #  render font, blit the font, then update the sceen
    message_to_screen('GAME OVER', red)
    pygame.display.update()
    time.sleep(2)
    pygame.quit() # unintialises pygame
    quit() # exits out of python

game_intro()
game_loop()


# vid 18