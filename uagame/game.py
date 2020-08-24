#n This game was made by Ayaan Merchant, using the uagame script #
# Full tutorial on YouTube Channel Mr.Merchant on how to make this game and use uagame #

from uagame import Window
from time import sleep
from random import randint

def main():
    window = create_window()
    height = window.get_height()
    width = window.get_width()
    enter = entry(window, height, width)
    if enter == True:
        load(window, width, height)
        play(window, width, height)
        window.draw_string('GAME OVER', height/2, width/2)
        window.update()

def create_window():
    window = Window('Game', 600, 500)
    window.set_font_name('couriernew')
    window.set_font_size(20)
    window.set_font_color('yellow')
    window.set_bg_color('black')
    return window

def entry(window, height, width):
    password = 'sub'
    attempts = 2
    guess = window.input_string('ENTER PASSWORD > ', width/3, height/3)
    while guess != password and attempts > 0:
        window.clear()
        window.draw_string('attempts left: ' + str(attempts), 10, window.get_font_height())
        window.draw_string('Entry Unsuccessful', width/2.5, height/2.5)
        guess = window.input_string('ENTER PASSWORD > ', width/3, height/3)
        attempts -= 1
        window.clear()
    if guess == password:
        window.draw_string('Entry Successful', width/2.5, height/2.5)
        window.update()
        sleep(2)
        return True
    if attempts == 0:
        window.draw_string('You are out of attempts', width/3.5, height/3)
    window.update()

def load(window, height, width):
    new_font = window.get_bg_color()
    new_bg = window.get_font_color()
    window.set_bg_color(new_bg)
    window.set_font_color(new_font)
    window.clear()
    window.draw_string('LOADING......', width/2.5, height/2)
    window.update()
    sleep(2)

def play(window, width, height):
    choices = ['rock', 'paper', 'scissors']
    window.draw_string('Let"s play, rock, paper, scissors,', width/2, height/3)
    sleep(1)
    window.clear()
    # take comp choice #
    comp = choices[randint(0, 2)]
    # display options #
    window.draw_string('Your choices are: ', width/4, height/3)
    location = height/2.5
    numb = 1
    for choice in choices:
        window.draw_string(str(numb) + ') ' + choice, width/3, location)
        location += window.get_font_height()
        numb += 1
    # take player choice #
    player = window.input_string('enter your choice > ', width/4, height/1.8)
    window.clear()
    # JUDGE #
    # JUDGE #
    if comp == player:
        window.draw_string("IT'S A TIE", width/4, height/1.8)
    elif player == 'rock':
        # comp beats player #
        if comp == 'paper':
            window.draw_string('YOU LOSE, ' + comp + ' covers ' + player, width/4, height/1.8)
            # player beats comp #
        else:
            window.draw_string('YOU WIN, ' + player + ' smashes ' + comp, width/4, height/1.8)
    elif player == 'paper':
        # comp beats player #
        if comp == 'scissors':
            window.draw_string('YOU LOSE, ' + comp + ' cuts ' + player, width/4, height/1.8)
        # player beats comp #
        else:
            window.draw_string('YOU WIN, ' + player + ' covers ' + comp, width/4, height/1.8)
    elif player == 'scissors':
        # comp beats player #
        if comp == 'rock':
            window.draw_string('YOU LOSE, ' + comp + ' smashes ' + player, width/4, height/1.8)
        # player beats comp #
        else:
            window.draw_string('YOU WIN, ' + player + ' cuts ' + comp, width/4, height/1.8)
    window.update()
    sleep(1.5)
    window.clear()
    
                           

main()

#n This game was made by Ayaan Merchant, using the uagame script #
# Full tutorial on YouTube Channel Mr.Merchant on how to make this game and use uagame #
