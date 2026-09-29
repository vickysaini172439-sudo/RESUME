"""
GST BILL CALCULATOR
Takes items, applies the GST rate for their category, saves each line
to a binary file with pickle, then prints the bill.

Author: Vicky
"""
import pickle

f = open("GST_CALCULATOR_SYSTEM.dat", "wb")
f.close()
f = open("GST_CALCULATOR_SYSTEM.dat", "ab")
L1 = ["", "FOOD", "ELECTRONICS", "STATIONARY", "CLOTHES", "HOUSEHOLDS", "FURNITURE", "VEHICLES"]
d = {"FOOD": 5, "ELECTRONICS": 18, "STATIONARY": 1, "CLOTHES": 12, "HOUSEHOLDS": 6, "FURNITURE": 8, "VEHICLES": 23}


def get_number(msg, kind=int):
    """Ask again until a valid positive number is typed."""
    while True:
        try:
            v = kind(input(msg))
            if v > 0:
                return v
            print("VALUE MUST BE MORE THAN 0")
        except ValueError:
            print("PLEASE ENTER A VALID NUMBER")


grand_total = 0
while True:
    i_n = input("ENTER ITEM NAME: ")
    cp = get_number("ENTER PRICE OF ITEM: ", float)
    qty = get_number("ENTER QUANTITY: ")
    while True:
        category = get_number("Enter Category:\n Format:\n1 for Food\n2 for Electronics\n3 for Stationary"
                              "\n4 for Clothes\n5 for Households\n6 for Furniture\n7 for Vehicle\n")
        if 1 <= category <= 7:
            break
        print("CHOOSE A NUMBER FROM 1 TO 7")
    category = L1[category]
    tax = d[category]
    tcp = cp * qty                      # price of all units before tax
    GST = tcp * (tax / 100)
    Total_price = tcp + GST             # fixed: total must use tcp (price x quantity)
    grand_total += Total_price
    L = [i_n, cp, qty, category, round(tax, 2), round(GST, 2), round(Total_price, 2)]
    pickle.dump(L, f)
    z = input("Do You Want To Add More Items: Enter y for yes: ")
    if z.lower() != "y":
        break
f.close()

print("YOUR BILL IS GENERATING")
print("\n{:<12}{:<9}{:<6}{:<13}{:<7}{:<10}{:<11}".format("|ITEM|", "|PRICE|", "|QTY|", "|CATEGORY|", "|TAX%|", "|GST|", "|TOTAL|"))
print("-" * 68)
f = open("GST_CALCULATOR_SYSTEM.dat", "rb")
try:
    while True:
        l = pickle.load(f)
        print("{:<12}{:<9}{:<6}{:<13}{:<7}{:<10}{:<11}".format(l[0], l[1], l[2], l[3], l[4], l[5], l[6]))
except EOFError:
    f.close()
print("-" * 68)
print("GRAND TOTAL (incl. GST): Rs.", round(grand_total, 2))
