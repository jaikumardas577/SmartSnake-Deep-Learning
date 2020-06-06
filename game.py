from Interface.models import *
import csv
import os
from pyfiglet import Figlet
from time import sleep
from utils.utils import *
import msvcrt
import sys 
from colorama import Fore, Back, Style 
f = Figlet(font='slant')
print(f.renderText('Hello World'))


board = Board()
print("Press any key to Play and Q to quit")
input_char = msvcrt.getch()
print(input_char)
board = Board()
food = Food(board)
snake = Snake(board)
GameOver = False
data_file = open('data.csv', mode='w')
data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

while(True):
    # print(snake)
    # print(food)
    print(board.getLength,board.getbreath)
    print(food)
    print(snake, "L1 : " + str(snake.getL1(board))," L2 : ",str(snake.getL2(board))," L3 : ",snake.getL3(board)," L4 : ",snake.getL4(board))
    print("Distance From Food : ", str(snake.getDistance(food,board)), "  Gradient1 : ",str(snake.getGradient1(food))," Gradient 2 : ",str(snake.oreintation(food)))
    showBoard(board,snake,food)
    GameOver = check_game_over(board,snake)
    if GameOver:
        clear()
        print(Fore.RED,f.renderText('Game Over'))
        break
    input_char = msvcrt.getch()
    if input_char.decode("utf-8")  == 'w':
        movement = 0
        snake.moveUp
    elif input_char.decode("utf-8")  == 's':
        movement = 1
        snake.moveDown
    elif input_char.decode("utf-8")  == 'a':
        movement = 2
        snake.moveLeft
    elif input_char.decode("utf-8")  == 'd':
        movement = 3
        snake.moveRight
    if snake.getPosx == food.getPosx and snake.getPosY == food.getPosY:
        food = Food(board)

    data_writer.writerow([snake.getL1(board),snake.getL2(board), snake.getL3(board),snake.getL4(board),snake.getGradient1(food),snake.oreintation(food),movement])

    # sleep(1)
    # if input_char:
    clear()
        




