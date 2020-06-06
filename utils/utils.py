import os
from time import sleep
from colorama import Fore, Back, Style 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def showBoard(board,snake,food):
    
    for x_ in range(board.getLength):
        for y_ in range(board.getbreath):
            if x_ == 0:
                if y_ == (board.getbreath -1):
                    print(" #m ")
                else:
                    print(" # ",end = "")
            elif x_ == (board.getLength - 1):
                if y_ == (board.getbreath -1):
                    print(" # ")
                else:
                    print(" # ",end = "")
            else:
                if y_ == 0:
                    print(" # ",end="")
                elif y_ == (board.getbreath -1):
                    print(" #m ")
                else:
                    if y_ == snake.getPosx and x_ == snake.getPosY:
                        print(" 0 ", end = "")
                    elif y_ == food.getPosx and x_ == food.getPosY:
                        print(Fore.RED + " F ",end = "")
                        print(Style.RESET_ALL,end = "") 
                    else:
                            print(" . ",end = "")

def check_game_over(board,snake):
    if snake.getPosx >= (board.getbreath -1 ) or snake.getPosx <= 0 or   snake.getPosY >= (board.getLength -1 ) or  snake.getPosY <= 0 :
        return True
    else:
        return False