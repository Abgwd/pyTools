import random
import numpy as np

def tic_tac_toe_input():
    global hflag,mflag,ttt
    while 1:
        if hflag:
            print ("Please mark your square")
            print ("1 | 2 | 3")
            print ("_________")
            print ("4 | 5 | 6")
            print ("_________")
            print ("7 | 8 | 9")
            human = input("->")
            if int(human)<=3 and int(human)>0:
                ttt[0][int(human)-1]=1
                break
            elif int(human)<=6 and int(human)>3:
                ttt[0][int(human)-1]=1
                break
            elif int(human)<=9 and int(human)>6:
                ttt[0][int(human)-1]=1
                break
            else:
                print ("Try Again")

def tic_tac_toe_output():
    global ttt
    print 
    print (ttt)
    
def tic_tac_toe_game():
    for i in range(1,10):
        tic_tac_toe_input()
        tic_tac_toe_output()
#--Main 
try:
    print ("Welcome to pyTic-Tac-Toe")
    print ("------------------------")
    human = random.randint(0,1)
    hflag,mflag = True,True
    if human == 0:machine = 1
    else:machine = 0
    ttt = np.array([['','',''],['','',''],['','','']])
    tic_tac_toe_game()
except Exception as e:
    print(e)
finally:
    print ("Game Completed")
