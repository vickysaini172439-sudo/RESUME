"""
FOOD ORDERING SYSTEM
Pick a restaurant, choose items from six menu categories, enter your
delivery details and get a bill. Each confirmed order is saved to a
binary file (food delivery.dat) with pickle.

Author: Vicky
"""
import pickle

cake_and_biscuits = {"parle": 10, "bourbon": 10, "tiger": 10, "choco-lava": 150, "pastry": 45, "chocolate": 40}
snacks = {"kurkure": 20, "chips": 20, "cake bars": 35, "fries": 20}
chinese = {"noodles": 150, "momos": 80, "spring roll": 70, "manchurian": 120, "chilli potato": 150, "chilli paneer": 200}
drinks = {"mojito": 150, "coca-cola": 60, "red bull": 150, "chocolate shake": 150, "cold coffee": 100}
sweets = {"kaju katli": 1000, "custard": 200, "gulab jamun": 500, "jalebi": 200, "rasgulla": 500, "rabri": 250, "barfi": 200}
pizza = {"margherita": 400, "pepperoni": 550, "four cheese": 500, "onion": 250, "sicilian": 550}
restaurant = ["bhai restaurant", "milan", "bikaner", "haldiram", "dominos"]
address = ["sec-2", "sec-3", "tirkha colony", "sec-64", "arya nagar"]

# category name typed by the user -> its menu
menus = {
    "cake and biscuits": cake_and_biscuits,
    "snacks": snacks,
    "chinese": chinese,
    "drinks": drinks,
    "sweets": sweets,
    "pizza": pizza,
}

L = []
k = 0
print("WELCOME TO OUR FOOD ORDERING SYSTEM")

while True:
    r_name = input("      Select Your Restaurant Name:\n            BHAI RESTAURANT\n            MILAN\n            BIKANER"
                   "\n            HALDIRAM\n            DOMINOS\n").strip().lower()
    if r_name in restaurant:
        break
    print("RESTAURANT NOT AVAILABLE, PLEASE CHOOSE FROM THE LIST")

while True:
    order = input("      Select Your Item_Category:\n            Cake and Biscuits\n            Snacks\n            Chinese"
                  "\n            Drinks\n            Sweets\n            Pizza\n").strip().lower().replace("_", " ")
    if order not in menus:                              # fixed: unknown category no longer crashes
        print("CATEGORY NOT FOUND, TRY AGAIN")
        continue
    menu = menus[order]
    print("      Select Your Item:")
    for name, price in menu.items():
        print("            " + name.title() + "  - Rs.", price)
    item = input().strip().lower()
    if item not in menu:                                # fixed: unknown item no longer crashes
        print("ITEM NOT FOUND, TRY AGAIN")
        continue
    price = menu[item]
    try:
        quantity = int(input("enter your item quantity: "))
        if quantity <= 0:
            raise ValueError
    except ValueError:
        print("PLEASE ENTER A VALID QUANTITY")
        continue
    cost = price * quantity
    L1 = [item.title(), price, quantity, cost]
    L.append(L1)
    n = input("DO YOU WANT TO ADD MORE ITEMS: YES OR NO ")
    if n.upper() in ("NO", "N"):
        break

NAME = input("ENTER YOUR NAME: ")
ADDRESS = input("ENTER YOUR ADDRESS: ").strip().lower()
while ADDRESS not in address:                            # fixed: keeps asking until a delivery area is chosen
    print("LOCATION NOT AVAILABLE\nTRY NEW LOCATION")
    ADDRESS = input("ENTER YOUR ADDRESS:\n     Sec-2\n     Sec-3\n     Tirkha Colony\n     Sec-64\n     Arya Nagar\n").strip().lower()
print("ORDER CONFIRMED")

while True:
    CONTACT = input("ENTER YOUR CONTACT NUMBER: ").strip()  # fixed: was CONTACT:int(...) which never saved the value
    if CONTACT.isdigit() and len(CONTACT) == 10:
        break
    print("INVALID NUMBER (must be 10 digits)")

print("\nYOUR BILL IS GIVEN BELOW")
print("      Restaurant :", r_name.title())
for i in L:
    print("     ", i[0], "  :", i[1], "*", i[2], "=", i[3])
    k = i[3] + k
print("     Total Cost : Rs.", k)

with open("food delivery.dat", "ab") as f:              # the file is now actually used to store the order
    pickle.dump({"name": NAME, "restaurant": r_name, "address": ADDRESS, "contact": CONTACT, "items": L, "total": k}, f)

n = input("GIVE YOUR FEEDBACK HERE: ")
print("THANKS FOR COMING")
