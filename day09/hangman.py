import sys
import random
import os
import datetime
import pygame
def open_read_file(file):
    if os.path.isfile(file):
        f = open(file)
        return f.read()
    print("incorrect file!")
    exit

def str_to_tab(string, delim):
    return string.split(delim)

def random_word(tab):
    return tab[random.randint(0, len(tab) - 1)]

def make_underscore(string):
    new_string =""
    for i in range(len(string)):
        new_string += "_ "
    return new_string

def find_letter(string, letter):
    if letter in string:
        if len(letter) == 1:
            print ("Found '"+letter +"'")
        else:
            print(letter + ": correct guess")
        return 0
    if len(letter) == 1:
        print ("Not found '"+letter +"'")
        return 1
    else:
        print(letter + ": incorrect guess")
        return len(letter)

def update_string(string, letter, current_string):
    new_current_string = ""
    print(current_string)
    for i in range(len(string)):
        for j in range (len(letter)):
            if string[i] == letter[j]:
                new_current_string += string[i] + " "
        if len(new_current_string) / 2 <= i:
            new_current_string += current_string[i * 2] + " "
    print("Current word: " + new_current_string)
    return new_current_string

def find_underscore(string):
    for i in range(len(string)):
        if string[i] == "_":
            return True
    return False

def write_in_file(file, string):
    if os.path.isfile(file):
        f = open(file, "a")
        return f.write(string)
    print("incorrect file!")
    exit

def draw_stickman(window, penalty):
    if penalty == 0:
        return
    if penalty >= 1:
        pygame.draw.line(window, (255, 0, 0), [100, 900], [500, 900], 3)
    if penalty >= 2:
        pygame.draw.line(window, (255, 0, 0), [200, 900], [200, 500], 3)
    if penalty >= 3:
        pygame.draw.line(window, (255, 0, 0), [200, 500], [300, 500], 3)
    if penalty >= 4:
        pygame.draw.line(window, (255, 0, 0), [200, 600], [300, 500], 3)
    if penalty >= 5:
        pygame.draw.line(window, (255, 0, 0), [300, 500], [400, 500], 3)
    if penalty >= 6:
        pygame.draw.line(window, (255, 0, 0), [400, 500], [400, 540], 3)
    if penalty >= 7:
        pygame.draw.circle(window, (255, 0, 0), [400, 570], 30, 3)
    if penalty >= 8:
        pygame.draw.line(window,  (255, 0, 0), [400, 600],  [400, 700], 3)
    if penalty >= 9:
        pygame.draw.line(window,  (255, 0, 0), [400, 700],  [350, 750], 3)
    if penalty >= 10:
        pygame.draw.line(window,  (255, 0, 0), [400, 700],  [450, 750], 3)
    if penalty >= 11:
        pygame.draw.line(window,  (255, 0, 0), [350, 650],  [400, 650], 3)
    if penalty >= 12:
        pygame.draw.line(window,  (255, 0, 0), [400, 650],  [450, 650], 3)

def end_game(number_word):
    pygame.init()
    pygame.display.set_caption("End Game")
    background = pygame.image.load("./asset/Space-Background-Images.jpg")
    window = pygame.display.set_mode((1000, 1000))
    background = pygame.transform.scale(background, (1000, 1000))
    font = pygame.font.SysFont("Arial", 30)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return  
        best_score = str_to_tab(open_read_file("best_scores"), "|")
        if len(best_score) == 1:
            write_in_file("best_scores", str(number_word) + "-" + str(datetime.date.today()) + "|")
            text = font.render("Best ever!!! You've guessed "+ str(number_word) + " word", True, (255, 255, 255))
            window.blit(background, (0, 0))
            window.blit(text, (150, 250))
            pygame.display.update()
        else:
            if int(str_to_tab(best_score[len(best_score) - 2], "-")[0]) < number_word:
                write_in_file("best_scores", str(number_word) + "-" + str(datetime.date.today()) + "|")
                text = font.render("Best ever!!! You've guessed "+ str(number_word) + " word", True, (255, 255, 255))
                window.blit(background, (0, 0))
                window.blit(text, (150, 250))
                pygame.display.update()
            else :
                text = font.render("You've guessed "+ str(number_word) +" words. The record is " + str(str_to_tab(best_score[len(best_score) - 2], "-")[0]) + " words", True, (255, 255, 255))
                window.blit(background, (0, 0))
                window.blit(text, (150, 250))
                pygame.display.update()

def game_loop(penalty, number_word, string, word, current_string, clock, start_time, level ):
    pygame.init()
    pygame.display.set_caption("Hangman")
    background = pygame.image.load("./asset/Space-Background-Images.jpg")
    window = pygame.display.set_mode((1000, 1000))
    background = pygame.transform.scale(background, (1000, 1000))
    font = pygame.font.SysFont("Arial", 30)
    button_menu = pygame.Rect(0, 0, 200, 50)
    while penalty <= 12:
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        letter = ""
        status = 0
        while status != 1:
            elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        status = 1
                    elif event.key == pygame.K_BACKSPACE:
                        letter = letter[:-1]
                    else : 
                        letter += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if button_menu.collidepoint(event.pos):
                        if menu_pygame(penalty, number_word, string, word, current_string, clock, start_time, level) == 1:
                            return
            window.blit(background, (0, 0))
            text = font.render("Word: " + current_string, True, (255, 255, 255))
            window.blit(text, (50, 50))
            text = font.render("Penalty: " + str(penalty), True, (255, 255, 255))
            window.blit(text, (50, 100))
            text = font.render("Number of words: " + str(number_word), True, (255, 255, 255))
            window.blit(text, (50, 150))
            text = font.render("Level: " + str(level), True, (255, 255, 255))
            window.blit(text, (50, 200))
            draw_stickman(window, penalty)
            text = font.render("Time elapsed: " + str(elapsed_time) + "s / 60s", True, (255, 255, 255))
            if elapsed_time >= 60:
                penalty += 1
                start_time = pygame.time.get_ticks()
            window.blit(text, (50, 250))
            pygame.draw.rect(window, (0, 200, 0), button_menu)
            window.blit(font.render("menu", True, (255, 255, 255)), (button_menu.x+40, button_menu.y+10))
            pygame.display.update()
            clock.tick(60)
        penalty += find_letter(word, letter)
        current_string = update_string(word, letter, current_string)
        if find_underscore(current_string) == False:
            penalty -= 1
            string = open_read_file("Level"+str(level))
            word = random_word(str_to_tab(string, " "))
            current_string = make_underscore(word)
            number_word += 1
            if number_word % 5 == 0:
                level += 1
    end_game(number_word)

def start_game():
    penalty = 0
    number_word = 0
    level = 1
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    string = open_read_file("Level"+str(level))
    word = random_word(str_to_tab(string, " "))
    current_string = make_underscore(word)
    game_loop(penalty, number_word, string, word, current_string, clock, start_time, level)
    
def menu_pygame(penalty, number_word, string, word, current_string, clock, start_time, level):
    pygame.init()
    pygame.display.set_caption("Menu")
    background = pygame.image.load("./asset/Space-Background-Images.jpg")
    window = pygame.display.set_mode((1000, 1000))
    background = pygame.transform.scale(background, (1000, 1000))
    font = pygame.font.SysFont("Arial", 30)
    button_continue = pygame.Rect(200, 200, 200, 50)
    button_restart = pygame.Rect(200, 300, 200, 50)
    button_quit = pygame.Rect(200, 400, 200, 50)
    status = 0 
    while status == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = 1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_continue.collidepoint(event.pos):
                    game_loop(penalty, number_word, string, word, current_string, clock, start_time, level)
                elif button_restart.collidepoint(event.pos):
                    start_game()
                elif button_quit.collidepoint(event.pos):
                    pygame.quit()
                    return 1
        window.blit(background, (0, 0))
        pygame.draw.rect(window, (0, 200, 0), button_continue) 
        pygame.draw.rect(window, (200, 200, 0), button_restart)
        pygame.draw.rect(window, (200, 0, 0), button_quit)
        window.blit(font.render("Continue", True, (255, 255, 255)), (button_continue.x+40, button_continue.y+10))
        window.blit(font.render("Restart", True, (255, 255, 255)), (button_restart.x+55, button_restart.y+10))
        window.blit(font.render("Quit", True, (255, 255, 255)), (button_quit.x+75, button_quit.y+10))
        pygame.display.update()
    pygame.quit()
    return status

start_game()
