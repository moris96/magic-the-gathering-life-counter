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
counter = 0
counter2 = 0



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
plus = button(75, 350, '+')
minus = button(325, 350, '-')
plus2 = button(175, 350, '+')
minus2 = button(425, 350, '-')

test = button(10, 10, '')


run = True
while run:
    screen.fill(bg)

    


    if reset.draw_button():
        print('Resetting Game')
        counter = 0
        counter2 = 0
    if player1.draw_button():
        print('Player 1')
    if player2.draw_button():
        print('Player 2')
    if plus.draw_button():
        print('Player 1 + 1')
        counter += 1
    if minus.draw_button():
        print('Player 1 - 1')
        counter -= 1
    if plus2.draw_button():
        print('Player 2 + 1')
        counter2 += 1
    if minus2.draw_button():
        print('Player 2 - 1')
        counter2 -= 1
    if test.draw_button():
        print('test')

    counter_img = font.render(str(counter), True, buttonColor)
    screen.blit(counter_img, (280, 450))

    counter2_img = font.render(str(counter2), True, buttonColor)
    screen.blit(counter2_img, (480, 450))

    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    p.display.update()

p.quit()