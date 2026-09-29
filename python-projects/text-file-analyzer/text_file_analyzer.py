"""
TEXT FILE ANALYZER
Two text-file practice programs:
1. MTCOUNT()      - counts the letters M/m and T/t in Story.txt
2. VOWEL_LINES()  - prints the lines of Story.txt that start with a vowel

Author: Vicky
"""


def MTCOUNT():
    f = open("Story.txt", "r")
    r = f.read()
    f.close()
    m = 0
    t = 0
    for i in r:
        if i == "M" or i == "m":
            m = m + 1
        if i == "T" or i == "t":
            t = t + 1
    print("Number of M/m :", m)
    print("Number of T/t :", t)


def VOWEL_LINES():
    f = open("Story.txt", "r")
    r = f.readlines()
    f.close()
    for i in r:
        if i and i[0] in "AEIOUaeiou":
            print(i, end="")        # fixed: print the line (i), not the whole list (r)


try:
    MTCOUNT()
    print("\nLines starting with a vowel:")
    VOWEL_LINES()
except FileNotFoundError:
    print("Story.txt not found. Keep a Story.txt file in the same folder and run again.")
