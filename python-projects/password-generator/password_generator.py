"""
RANDOM PASSWORD GENERATOR
Makes an 8-character password with 2 uppercase letters, 2 lowercase
letters, 2 digits and 2 special characters, in a random order.

Uses Python's `secrets` module, which is designed for passwords,
instead of `random`, whose output can be predicted.

Author: Vicky
"""
import secrets

print("RANDOM PASSWORD GENERATOR PROGRAM")


def pas():
    L1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    L2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
          "T", "U", "V", "W", "X", "Y", "Z"]
    L3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
          't', 'u', 'v', 'w', 'x', 'y', 'z']
    L4 = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"]
    rng = secrets.SystemRandom()
    L5 = [rng.choice(L2), rng.choice(L2),     # 2 uppercase
          rng.choice(L3), rng.choice(L3),     # 2 lowercase
          rng.choice(L1), rng.choice(L1),     # 2 digits
          rng.choice(L4), rng.choice(L4)]     # 2 special characters
    rng.shuffle(L5)                           # random order, so the pattern can't be guessed
    s = ""
    for i in L5:
        s = s + str(i)
    return s


while True:
    print("Generated Password :", pas())
    D = input("DO YOU WANT MORE PASSWORDS: y/n ")
    if D.lower() != "y":
        break
print("STAY SAFE ONLINE!")
