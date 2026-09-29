"""
STONE PAPER SCISSOR GAME
Play against the computer and keep a running score.

Author: Vicky
"""
import random

L = ["Stone", "Paper", "Scissor"]
s = 0
print("STONE PAPER SCISSOR GAME")
while True:
    n = input("Choose :\n1 for Stone\n2 for Paper\n3 for Scissor\n").strip()
    if n not in ("1", "2", "3"):
        print("PLEASE CHOOSE 1, 2 OR 3")
        continue
    n = int(n)
    you = L[n - 1]
    g = random.choice(L)
    print("BOT choose", g)
    print("YOU choose", you)
    if you == g:
        print("Draw")
    elif (you == "Stone" and g == "Scissor") or (you == "Paper" and g == "Stone") or (you == "Scissor" and g == "Paper"):
        s = s + 1
        print("You WON")
    else:
        s = s - 1
        print("You LOSE")
    print("YOUR SCORE", s)
    d = input("DO YOU WANT TO PLAY MORE: y/n ")
    if d.lower() == "n":          # fixed: compare with the text "n", not the variable n
        break
print("FINAL SCORE", s)
