import sys
sys.path.append("D:\TensorFlowEnv\SmartSnake-Deep-Learning")
from interface.models import *
import csv
import os
from pyfiglet import Figlet
from time import sleep
from utils.utils import *
import msvcrt
import sys 
from colorama import Fore, Back, Style 
import pandas as pd
import numpy as np
from tensorflow import keras
import warnings
warnings.filterwarnings("ignore")

#loading The Model

model = keras.models.load_model('D:/TensorFlowEnv/SmartSnake-Deep-Learning/training/models/my_model-version1.1')


def predict(L1,L2,L3,L4,Gradient1,oreintation):

    outcome_dict = { "0":"MoveUp" , "1":"MoveDown" , "3":"MoveLeft" , "2":"MoveRight"}

    d = {
        "L1": [L1],   "L2":[L2],
        "L3":[L3],"L4":[L4],
        "Gradient":[Gradient1],"Orientation": [oreintation]
        }

    d_ =  pd.DataFrame(data = d)
    predicted_move = np.argmax(model.predict(d_))
    return outcome_dict[str(predicted_move)]



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
    print(snake, "L1 : " + str(snake.getL1(board))," L2 : ",str(snake.getL2(board))," L3 : ",snake.getL3(board)," L4 : ",snake.getL4(board))
    print("Distance From Food : ", str(snake.getDistance(food,board)), "  Gradient1 : ",str(snake.getGradient1(food))," Gradient 2 : ",str(snake.oreintation(food)))
    showBoard(board,snake,food)
    sleep(1)
    GameOver = check_game_over(board,snake)


    if GameOver:
        clear()
        print(Fore.RED,f.renderText('Game Over'))
        break

    ml_predicted_move = predict(snake.getL1(board),snake.getL2(board), snake.getL3(board),snake.getL4(board),snake.getGradient1(food),snake.oreintation(food))
    if ml_predicted_move  == 'MoveUp':
        print("run1")
        snake.moveUp
    elif ml_predicted_move == 'MoveDown':
        print("run2")
        snake.moveDown
    elif ml_predicted_move  == 'MoveLeft':
        print("run3")
        snake.moveLeft
    elif ml_predicted_move  == 'MoveRight':
        print("run4")
        snake.moveRight

    if snake.getPosx == food.getPosx and snake.getPosY == food.getPosY:
        food = Food(board)

    # Function for writting data into Csv File for Training.

    # data_writer.writerow([snake.getL1(board),snake.getL2(board), snake.getL3(board),snake.getL4(board),snake.getGradient1(food),snake.oreintation(food),movement])

    clear()
    
        




