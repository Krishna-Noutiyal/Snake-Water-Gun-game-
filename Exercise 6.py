"""
Making the Game:
Snake, Water, Gun
"""
import random as rand

import time 


def Welcome_Lines():
    welcome = [
    "\n\n\tHello and Welcome to\n\tSnake, Water, Gun ",
    "\n\tSo first of all, before starting the game let's talk about rules",
    "\n\tThere are no rule 🤣",
    "\n\tKidding !!! HaHa",
    "\n\tYou will get 10 chances ",
    "\n\tPlayer with most victory will win at last",
    "\n\tYou just have to choose from Snake, Water, Gun",
    "\n\tbut i will choose first always",
    "\n\tYou wondering why, because kid!! I am the boss",
    "\n\n\nSo let's begin"
    ]

    #Adding a delay
    for i in welcome:
        print(i)
        # time.sleep(3)

Welcome_Lines()
#Delay
def Delay():
    time.sleep(1)
    # print()

#Delay in printing of long statments
def Line_Delay(a):
    """Addes delay to a list and prints it, takes a list as a """
    #Adding delay in printin lines
    for i in a:
        print(i)
        Delay()



#Asking user to start
q = input("Press Enter to Start: ")

#Adding a delay
Delay()

Swg = ["Snake", "Water", "Gun"]

#Shortform of Snake Water Gun
s = "Snake"
w = "Water"
g = "Gun"


#Lines to tell player to choose
Player_Choose= [
    "it's your turn",
    "It's your turn to choose",
    "Now choose"
    ]

i = 1

def turns():
    
    #Turns left
    print(f"\n\nTurns left {10-i}")


# No. of draws
draw = 0
# Pc winning
Pc_win = 0
# Player winning
Player_win = 0


while True:

    while (i < 11):

        Pc_Choose = rand.choice(Swg)

        #Adding a delay
        Delay()

        print("\n\t\tI have choosen!!")
            
        #Adding a delay
        Delay()
        
        #Random statments for user
        Ask_line = rand.choice(Player_Choose)

        print(f"\n\t\t {Ask_line}")

        #Adding a delay
        Delay()

        User_Choose = str(input("\n\n\t\t\tChoose from Snake, Water, Gun: "))
        User_Choose = User_Choose.capitalize()
        
        #Adding a delay
        Delay()
        
        
        # if player and pc choose the same option
        
        if User_Choose == Pc_Choose:
            print(f"\n\n\t\t\tOh Lol it was a draw we both took {User_Choose}")
            
            #Adding a delay
            Delay()
        
            print("\n\t\t\t\tLet's go again")
            
            #Adding a delay
            Delay()
        
            # Adding the number of draws to draw
            draw +=1
            # Increasing the value of i to stop the loop
            i = i+1

            # Function that prints turns left
            turns()
            c = input("\n\tPress Enter for next turn: ")
            continue

    # Conditions where pc will loose

        # if player = snake and pc = water
        elif User_Choose == s and Pc_Choose == w:
            print(f"\n\n\t\t\tAhugh!! Man you win I took {Pc_Choose} and you took {User_Choose}")
            
            #Adding a delay
            Delay()
        
            print("\n\t\t\t\tYou are so pro but not better then me 🤔🤔")
            
            #Adding a delay
            Delay()
        
            # Adding no of victories to Player_win
            Player_win += 1
            # Increaing the value of i to stop the loop
            i = i+1

            # Function that prints turns left
            turns()
            c = input("\n\tPress Enter for next turn: ")
            continue

        
        # if player = water and pc = gun
        elif User_Choose == w and Pc_Choose == g:
            
            print(f"\n\n\t\t\tAhugh!! Man you win I took {Pc_Choose} and you took {User_Choose}")
            
            #Adding a delay
            Delay()
        
            print("\n\t\t\t\tYou are so pro but not better then me 🤔🤔")
            
            #Adding a delay
            Delay()
        
            # Adding no of victories to Player_win
            Player_win += 1
            # Increaing the value of i to stop the loop
            i = i+1

            # Function that prints turns left
            turns()
            c = input("\n\tPress Enter for next turn: ")
            continue
        
        # if player = gun and pc = snake
        elif User_Choose == g and Pc_Choose == s:
            
            print(f"\n\n\t\t\tAhugh!! Man you win I took {Pc_Choose} and you took {User_Choose}")
            
            #Adding a delay
            Delay()
        
            print("\n\t\t\t\tYou are so pro but not better then me 🤔🤔")
            
            #Adding a delay
            Delay()
        
            # Adding no of victories to Player_win
            Player_win += 1
            # Increaing the value of i to stop the loop
            i = i+1

            # Function that prints turns left
            turns()
            c = input("\n\tPress Enter for next turn: ")
            continue


    # Conditions where player will loose

        # if player = water and pc = snake
        elif User_Choose == w and Pc_Choose == s:

            #Statement if player loose
            print(f"\n\n\t\t\tHaehaa!! lol I win I took {Pc_Choose} and you took {User_Choose}")
            
            #Adding a delay
            Delay()
        
            print("\n\t\t\t\tTry again you might win")
            
            #Adding a delay
            Delay()
        
            # Adding the victory to Pc_win 
            Pc_win += 1
            # Increasing the value of i to stop the loop
            i = i+1

            # Function that prints turns left
            turns()
            c = input("\n\tPress Enter for next turn: ")
            continue

        
        # if player = gun and pc = water
        elif User_Choose == g and Pc_Choose == w:

            #Statement if player loose
            print(f"\n\n\t\t\tHaehaa!! lol I win I took {Pc_Choose} and you took {User_Choose}")
            
            #Adding a delay
            Delay()
        
            print("\n\t\t\t\tTry again you might win")
            
            #Adding a delay
            Delay()
        
            # Adding the victory to Pc_win 
            Pc_win += 1
            # Increasing the value of i to stop the loop
            i = i+1

            # Function that prints turns left
            turns()
            c = input("\n\tPress Enter for next turn: ")
            continue
        
        # if player = snake and pc = gun
        elif User_Choose == s and Pc_Choose == g:
            
            #Statement if player loose
            print(f"\n\n\t\t\tHaehaa!! lol I win I took {Pc_Choose} and you took {User_Choose}")
            
            #Adding a delay
            Delay()
        
            print("\n\t\t\t\tTry again you might win")
            
            #Adding a delay
            Delay()
        
            # Adding the victory to Pc_win 
            Pc_win += 1
            # Increasing the value of i to stop the loop
            i = i+1

            # Function that prints turns left
            turns()
            c = input("\n\tPress Enter for next turn: ")
            continue
        
    # Don't know what will go wrong

        else:
            # Statement if player did someting wrong
            def l():
                lines = [

                    f"\n\n\t\t\tYou did someting illegal heahe 🤣🤣",
                    f"\n\t\t\tI try to be funny but you know that wasn't funny at all",
                    "\n\n\t\t\t\tTry again"
                    ]
                
                # Delay 
                Line_Delay(lines)
            
            l()
            
            # Function that prints turns left
            turns()
            i = i+1
            continue
        

    # Finishing lines when game is finished
    def finish():
        lines = [
            "\n\n\n\n\tSo our game is finished 🎉🎉👏",
            "\n\tNow it's time to reveal the result",
            "\n\tAre you ready🐱‍🏍🐱‍🏍",
            "\n\tPress Enter to reveal the result hheeh 👏🐱‍🏍👏"]

        #Adding delay
        Line_Delay(lines)

    finish()

    r = input("\n\n")


    # if both draw
    if Pc_win == Player_win:
        def l():
            lines = [
                "\n\n\t\tWe both faught hard but in the end it was a tie",
                f"\n\tYou won {Player_win} times",
                f"\n\tI won {Pc_win} times",
                f"\n\tWe draw {draw} rounds"
                ]
            #Adding delay to the lines
            Line_Delay(lines)
        
        l()

    # if Pc wins
    elif Pc_win > Player_win:
        def l():
            lines = [

                "\n\n\t\tWe both faught hard ",
                "\t\tBut boss will always boss my friend i won ",
                f"\n\tYou won {Player_win} times",
                f"\n\tI won {Pc_win} times",
                f"\n\tWe draw {draw} rounds"
            ]
            #Adding delay to the lines
            Line_Delay(lines)
        
        l()

    # if Player wins
    elif Pc_win < Player_win:
        def l():
            lines = [
                "\n\n\t\tWe both faught hard ",
                "\t\tBut how the hell a dumb like you can defeat me 😒😒😒",
                "\t\tAnyways, well played",
                f"\n\tYou won {Player_win} times",
                f"\n\tI won {Pc_win} times",
                f"\n\tWe draw {draw} rounds"
            ]
            #Adding delay to the lines
            Line_Delay(lines)
        
        l()


    close = str(input("\n\nPress Enter to exit or y to continue: "))

    if close == "y":
        i = 1
        continue
    else:
        break

    