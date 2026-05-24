#Importing Required Modules
import random
import time
import playsound

print("Welcome To Squid Game OXΔ")

time.sleep(2)

print("This is a Ddakaji Game Between Player and Salesman")


#Firstly Both Player and Salesman Choose One Card From Red And Sky Blue
Player=input("Choose One Ddakaji From Red And Sky Blue:")
if Player=="Sky Blue":
    print("         Player Choose the Ddakaji: Sky Blue")
else:
    print("         Player Choose the Ddakaji: Red")

time.sleep(2)

Salesman=input("Choose One Dakaji From Red And Sky Blue:")
if Salesman==Player:
    print("      Ddakaji is Already Choosen By Player")
    exit()
elif Salesman==Salesman:
    print("      Salesman Choose the Ddakaji:",Salesman)  

time.sleep(2)

print("..........................................................................Game Start.......................................................")

time.sleep(2)


# Now Both Player and Salesman Flip Their Ddakajies
Player=random.choice(["Unfliped","Fliped"])
if Player=="Fliped":
    print("      Player Fliped The Ddakaji")
else:
    print("      Player Unfliped The Ddakaji")

time.sleep(2)

Salesman=random.choice(["Fliped","Unfliped"])
if Salesman=="Fliped":
    print("      Salesman Fliped The Ddakaji")
else:
    print("      Salesman Unfliped The Ddakaji")  

time.sleep(5)


# Now We Check Who Win The Game
if Salesman=="Fliped" and Player=="Unfliped":
    print("      Player Lose The Game")
    playsound.playsound("C:\\Users\\DELL\\Downloads\\slap-in-the-face-101869.mp3")
    print("-------------------------------------------------------------------------Game Over---------------------------------------------------") 
    exit()
    
elif Salesman=="Unfliped" and Player=="Fliped":
    print("      Player Win The Game")
    print("      Player Get 1000$ Prize")
    
elif Salesman=="Fliped" and Player=="Fliped":
    print("      Player Lose The Game")
    playsound.playsound("C:\\Users\\DELL\\Downloads\\slap-in-the-face-101869.mp3")
    print("-------------------------------------------------------------------------Game Over---------------------------------------------------") 
    exit()

else: 
    print("        Player Win The Game")
    print("        Player Get 1000$ Prize")


# Selection for the Player and the Guard
Card=input("Enter the Ddakaji You Selected Before Game Starts:")
Number=random.randint(1,456)
if Card=="Red":
    print("You Are Selected as the Gaurd")
else:
    print("You Are Selected as the Player:",Number)
