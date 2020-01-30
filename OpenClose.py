# Program: The Open-Closed Game
# Name: Wanatbodee Buriwong
# Mahidol University International College
# a 4th year computer engineering student 


import random
import time
import numpy as np
import os

class Bot:
    #predict openhand
    def b_predict():
        option = ['O','C']
        result = []
        for i in range(2):
            #randomly select choices from option
            result.append(random.choice(option))
        #guess open hands
        num = random.randint(0,4)
        result = ''.join(result)+''.join(str(num))
        return result
    
    def b_manifest():
        option = ['O','C']
        result = []
        for i in range(2):
            result.append(random.choice(option))
        result = ''.join(result)
        return result
    
class Player:

    def p_predict():
        while(True):
            inputs = input("Your prediction is: ").upper()
            #looping until the input is valid
            if(len(inputs) == 3  and (inputs[0] == 'O' or inputs[0] == 'C') and (inputs[1] == 'O' or inputs[1] == 'C')):
                try: 
                    #make sure that the last character is an integers
                    inputs[2] == int(inputs[2])
                    if(int(inputs[2])>=0 and int(inputs[2])<5):
                        break
                    else:
                         print('The 3rd character must be a number between 0 to 4')
                except ValueError:
                        print('The 3rd character must be a number between 0 to 4')
            else:
                print("Invalid input: There must be exactly only 3 characters")
        return inputs

    def p_manifest():
        while(True):
            inputs = input("Show your hand!:").upper()
            if(len(inputs) == 2 and (inputs[0] == 'O' or inputs[0] == 'C') and (inputs[1] == 'O' or inputs[1] == 'C')):
                break
            else:
                print('The input must be only "O" or "C" !!!')
        return inputs

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

def compareResult(a,b):
    #remove the predicted number from string
    predicted_num = int(a[2])
    a_new = a[:2]
    print('Revealing hands in:')
    countdown(int(3))   
    o = ''.join(a_new)+''.join(b)
    count_O = o.count('O')
    print("Predictor's guess: %d"%(predicted_num))
    print('Result: %s '%o)
    
    if(count_O == predicted_num):
        print('Predictor wins !!!')
    else: 
        print('There is no winner..')

class Match:
    def start():
        bot = Bot
        player = Player
        round_num = 0
        print('======================HOW TO PLAY=============================')
        print('The first 2 characters must be either O or C')
        print('Predictor inputs: must be a total of 3 characters')
        print('\teg: OC1, OO2, CC3')
        print('Predictee inputs: must be 2 characters')
        print('\teg: OO, OC, CC, CO')
        print('==============================================================')
        while(True):
            #swapping turns
            if(round_num%2 == 0):
                print('Round:%d. \nPlayer predicts'%(round_num+1))
                print('===========================================================')
                a = player.p_predict()
                b = bot.b_manifest()
            else:
                print('Round:%d. \nBot predicts'%(round_num+1))
                print('===========================================================')
                a = bot.b_predict()
                b = player.p_manifest()
            
            compareResult(a,b)
            #decide whether user wants to continue or not
            while(True):
                continuum = input("Would you like to continue? (y/n):")
                continuum = continuum.upper()
                if(continuum == "Y" or continuum == "N"):
                    break
                else:
                    print('invalid')
            if(continuum == 'Y'):
                round_num += 1 
                print('===========================================================')
                #clear output screens
                os.system('clear')
                os.system('cls')
            elif(continuum == 'N'):
                print("\nThank you for playing.\nHave a great day!")
                break


def main():
    match = Match
    match.start()
if __name__ == '__main__':
    main()



