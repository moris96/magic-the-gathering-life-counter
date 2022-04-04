import pygame as p
from pygame.locals import *

p.init()


HEIGHT = WIDTH = 600

screen = p.display.set_mode((HEIGHT, WIDTH))
p.display.set_caption("Magic The Gathering Life Counter")

font = p.font.SysFont('Arial', 30)

#colors
bg = (130, 131, 130) #background color (grey)
black = (0, 0, 0)
white = (255, 255, 255)
buttonColor = (110, 7, 0)
hoverColor = (63, 35, 186)
clickColor = (10, 0, 56)

#text
text = font.render('Magic The Gathering Life Counter', False, buttonColor)


#global variables
clicked = False
counter = 20
counter2 = 20


class button():

    #colors for button & text
    button_color = buttonColor
    hover_color = hoverColor
    click_color = clickColor
    text_color = black
    width = 180
    height = 70

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):
        global clicked
        action = False

        pos = p.mouse.get_pos() #mouse position

        button_rect = Rect(self.x, self.y, self.width, self.height)

        #clicked conditions
        if button_rect.collidepoint(pos):
            if p.mouse.get_pressed()[0] == 1:
                clicked = True
                p.draw.rect(screen, self.click_color, button_rect)
            elif p.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                p.draw.rect(screen, self.hover_color, button_rect)
        else:
            p.draw.rect(screen, self.button_color, button_rect)

        #add text to button
        text_img = font.render(self.text, True, self.text_color)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action


#buttons
reset = button(100, 100, 'Reset')
player1 = button(75, 200, 'Player 1')
player2 = button(325, 200, 'Player 2')
plus = button(30, 300, '+')
minus = button(175, 300, '-')
plus2 = button(325, 350, '+')
minus2 = button(425, 350, '-')
startWith40 = button(50, 50, 'Start With 40 HP')


run = True
while run:
    screen.fill(bg)

    if reset.draw_button():
        print('Resetting Game')
        counter = 20
        counter2 = 20
    if player1.draw_button():
        print('Player 1')
    if player2.draw_button():
        print('Player 2')
    if plus.draw_button():
        print('Player 1 + 1HP')
        counter += 1
    if minus.draw_button():
        print('Player 1 - 1HP')
        counter -= 1
    if plus2.draw_button():
        print('Player 2 + 1HP')
        counter2 += 1
    if minus2.draw_button():
        print('Player 2 - 1HP')
        counter2 -= 1
    if startWith40.draw_button():
        print('Starting game with 40 HP')
        counter = counter2 = 40

    #life counter for player 1
    counter_img = font.render(str(counter), True, buttonColor)
    screen.blit(counter_img, (130, 450))

    #life counter for player 2
    counter2_img = font.render(str(counter2), True, buttonColor)
    screen.blit(counter2_img, (430, 450))

    #stop game when a player wins 
    if counter <= 0:
        print('Player 2 Wins!')
        break
    elif counter2 <= 0:
        print('Player 1 Wins!')
        break

    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    p.display.update()

p.quit()