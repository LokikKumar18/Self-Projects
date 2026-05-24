# Jackpot Machine Simulator

#importing necessary libraries
import random
import time

# Process to Test Your Luck
print("Welcome to the Jackpot Machine Simulator!")
time.sleep(2)
print()
print("                                                 Rules are Simple Insert Coin and Try Your Luck!                     ")
time.sleep(2)
print()
print("You can win a jackpot of 1000 coins if you hit the lucky combination!")
time.sleep(2)
Coin=input("Insert Your Coin =")
print("Yeah You Inserted the Coin of =", Coin)
time.sleep(2)

#Some time to think
Press=input("Enter P to Spin the Reels")
print("Spinning the reels...")
time.sleep(2)


# Wait For Your Luck
r=random.choice(['🍒', '🍋', '🍊'])
u=random.choice(['🍒', '🍋', '🍊'])
n=random.choice(['🍒', '🍋', '🍊'])
print("Wait For Results...")
time.sleep(3)
if r==u==n:
    print("                                               Congratulations! You hit the jackpot with", r, u, n)
    print("You win 1000 coins!")
   
else:
    print("                                                 Sorry, you didn't hit the jackpot. You got", r, u, n)
    print("Better luck next time!")
    exit()