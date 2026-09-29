"""
WORLD OF PERIODIC TABLE
Enter an atomic number (1-118) to see the element's name and symbol,
then ask for its atomic mass, electronegativity, block and period.

Author: Vicky
"""
print("::::::WELCOME TO WORLD OF PERIODIC TABLE:::::")
print("---HERE YOU CAN LEARN AND EXPAND YOUR KNOWLEDGE---")
print("USE : (A)YES , (B)NO")

n1 = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine"]
n2 = ["Neon", "Sodium", "Magnesium", "Aluminium", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium"]
n3 = ["Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper"]
n4 = ["Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium"]
n5 = ["Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium"]
n6 = ["Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Caesium", "Barium", "Lanthanum", "Cerium", "Praseodymium"]
n7 = ["Neodymium", "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium"]
n8 = ["Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold"]
n9 = ["Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium"]
n10 = ["Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium"]
n11 = ["Fermium", "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium"]
n12 = ["Darmstadtium", "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson"]
m1 = [1.008, 4.003, 6.941, 9.012, 10.811, 12.011, 14.007, 15.999, 18.998]
m2 = [20.180, 22.990, 24.305, 26.982, 28.086, 30.974, 32.066, 35.453, 39.948, 39.098]
m3 = [40.078, 44.956, 47.867, 50.942, 51.996, 54.938, 55.845, 58.933, 58.693, 63.546]
m4 = [65.38, 69.723, 72.631, 74.922, 78.971, 79.904, 83.798, 85.468, 87.62, 88.906]      # fixed Kr and Rb
m5 = [91.224, 92.906, 95.95, 98.907, 101.07, 102.906, 106.42, 107.868, 112.414, 114.818]
m6 = [118.711, 121.760, 127.60, 126.904, 131.294, 132.905, 137.328, 138.905, 140.116, 140.908]  # fixed Te
m7 = [144.243, 144.913, 150.36, 151.964, 157.25, 158.925, 162.500, 164.930, 167.259, 168.934]
m8 = [173.055, 174.967, 178.49, 180.948, 183.84, 186.207, 190.23, 192.217, 195.085, 196.967]
m9 = [200.592, 204.383, 207.2, 208.980, 208.982, 209.987, 222.018, 223.020, 226.025, 227.028]
m10 = [232.038, 231.036, 238.029, 237, 244, 243, 247, 247, 251, 252]
m11 = [257, 258, 259, 262, 261, 262, 266, 264, 269, 268]
m12 = [271, 272, 285, 284, 289, 288, 292, 294, 294]
sy1 = ['H', 'HE', 'LI', 'BE', 'B', 'C', 'N', 'O', 'F']
sy2 = ['NE', 'NA', 'MG', 'AL', 'SI', 'P', 'S', 'CL', 'AR', 'K']
sy3 = ['CA', 'SC', 'TI', 'V', 'CR', 'MN', 'FE', 'CO', 'NI', 'CU']
sy4 = ['ZN', 'GA', 'GE', 'AS', 'SE', 'BR', 'KR', 'RB', 'SR', 'Y']
sy5 = ['ZR', 'NB', 'MO', 'TC', 'RU', 'RH', 'PD', 'AG', 'CD', 'IN']
sy6 = ['SN', 'SB', 'TE', 'I', 'XE', 'CS', 'BA', 'LA', 'CE', 'PR']
sy7 = ['ND', 'PM', 'SM', 'EU', 'GD', 'TB', 'DY', 'HO', 'ER', 'TM']
sy8 = ['YB', 'LU', 'HF', 'TA', 'W', 'RE', 'OS', 'IR', 'PT', 'AU']
sy9 = ['HG', 'TL', 'PB', 'BI', 'PO', 'AT', 'RN', 'FR', 'RA', 'AC']
sy10 = ['TH', 'PA', 'U', 'NP', 'PU', 'AM', 'CM', 'BK', 'CF', 'ES']
sy11 = ['FM', 'MD', 'NO', 'LR', 'RF', 'DB', 'SG', 'BH', 'HS', 'MT']
sy12 = ['DS', 'RG', 'CN', 'NH', 'FL', 'MC', 'LV', 'TS', 'OG']
p1 = ["H", "HE"]
p2 = ['LI', 'BE', 'B', 'C', 'N', 'O', 'F', 'NE']
p3 = ['NA', 'MG', 'AL', 'SI', 'P', 'S', 'CL', 'AR']
p4 = ['K', 'CA', 'SC', 'TI', 'V', 'CR', 'MN', 'FE', 'CO', 'NI', 'CU', 'ZN', 'GA', 'GE', 'AS', 'SE', 'BR', 'KR']
p5 = ['RB', 'SR', 'Y', 'ZR', 'NB', 'MO', 'TC', 'RU', 'RH', 'PD', 'AG', 'CD', 'IN', 'SN', 'SB', 'TE', 'I', 'XE']
p6 = ['CS', 'BA', 'LA', 'CE', 'PR', 'ND', 'PM', 'SM', 'EU', 'GD', 'TB', 'DY', 'HO', 'ER', 'TM', 'YB', 'LU', 'HF', 'TA', 'W',
      'RE', 'OS', 'IR', 'PT', 'AU', 'HG', 'TL', 'PB', 'BI', 'PO', 'AT', 'RN']
p7 = ['FR', 'RA', 'AC', 'TH', 'PA', 'U', 'NP', 'PU', 'AM', 'CM', 'BK', 'CF', 'ES', 'FM', 'MD', 'NO', 'LR', 'RF', 'DB', 'SG',
      'BH', 'HS', 'MT', 'DS', 'RG', 'CN', 'NH', 'FL', 'MC', 'LV', 'TS', 'OG']
e1 = [2.2, "no data", 0.98, 1.57, 2.04, 2.55, 3.04, 3.44, 3.98]
e2 = ["no data", 0.93, 1.31, 1.61, 1.9, 2.19, 2.58, 3.16, "no data", 0.82]
e3 = [1, 1.36, 1.54, 1.63, 1.66, 1.55, 1.83, 1.88, 1.91, 1.9]
e4 = [1.65, 1.81, 2.01, 2.18, 2.55, 2.96, 3, 0.82, 0.95, 1.22]
e5 = [1.33, 1.6, 2.16, 1.9, 2.2, 2.28, 2.2, 1.93, 1.69, 1.78]
e6 = [1.96, 2.05, 2.1, 2.66, 2.6, 0.79, 0.89, 1.1, 1.12, 1.13]
e7 = [1.14, 1.13, 1.17, 1.2, 1.2, 1.22, 1.23, 1.24, 1.24, 1.25]
e8 = [1.1, 1.27, 1.3, 1.5, 2.36, 1.9, 2.2, 2.2, 2.28, 2.54]
e9 = [2, 1.62, 2.33, 2.02, 2, 2.2, "no data", 0.7, 0.89, 1.1]
e10 = [1.3, 1.5, 1.38, 1.36, 1.28, 1.3, 1.3, 1.3, 1.3, 1.3]
e11 = [1.3, 1.3, 1.3, "no data", "no data", "no data", "no data", "no data", "no data", "no data"]
e12 = ["no data", "no data", "no data", "no data", "no data", "no data", "no data", "no data", "no data"]

# Join the small lists into one list each, so element number v is at position v-1.
# (The old version had 12 copies of the same code, one per list, and each copy had different bugs.)
names = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + n11 + n12
masses = m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8 + m9 + m10 + m11 + m12
symbols = sy1 + sy2 + sy3 + sy4 + sy5 + sy6 + sy7 + sy8 + sy9 + sy10 + sy11 + sy12
electro = e1 + e2 + e3 + e4 + e5 + e6 + e7 + e8 + e9 + e10 + e11 + e12
periods = [p1, p2, p3, p4, p5, p6, p7]


def find_block(v):
    """Block from the atomic number (La-Yb and Ac-No are taken as the f-block)."""
    if v in (1, 2, 3, 4, 11, 12, 19, 20, 37, 38, 55, 56, 87, 88):
        return "S"
    if 57 <= v <= 70 or 89 <= v <= 102:
        return "F"
    if 21 <= v <= 30 or 39 <= v <= 48 or 71 <= v <= 80 or 103 <= v <= 112:
        return "D"
    return "P"


def find_period(symbol):
    for i in range(len(periods)):
        if symbol in periods[i]:
            return i + 1


D = input("DO YOU WANT TO CONTINUE THIS JOURNEY : ").strip().upper()
if D == "A":
    print("         CONGRATULATIONS!!! ")
    print("LETS KNOW BASICS ABOUT 118 ELEMENTS")
    while True:
        value = input("enter atomic number (1-118): ").strip()
        if not value.isdigit() or not 1 <= int(value) <= 118:        # fixed: bad input used to crash
            print("PLEASE ENTER A NUMBER FROM 1 TO 118")
            continue
        v = int(value)
        symbol = symbols[v - 1]
        print("Symbol: ", symbol.capitalize())
        print("ELEMENT NAME :", names[v - 1])
        q = input("YOU CAN ASK:(A)ATOMIC MASS,(B)ELECTRO NEGATIVITY,(C)BOTH : ").strip().upper()
        if q in ("A", "C"):
            print("ATOMIC MASS :", masses[v - 1])
        if q in ("B", "C"):
            print("ELECTRO NEGATIVITY :", electro[v - 1])
        b = input("DO YOU WANT TO KNOW BLOCK OF THIS ELEMENT:(A) YES , (B)NO : ").strip().upper()
        if b == "A":
            print(symbol.capitalize(), "Belongs to Block :", find_block(v))
        c = input("DO YOU WANT TO KNOW PERIOD OF THIS ELEMENT:(A) YES , (B)NO : ").strip().upper()
        if c == "A":
            print("Period of", symbol.capitalize(), ":", find_period(symbol))
        again = input("DO YOU WANT TO CHECK ANOTHER ELEMENT:(A) YES , (B)NO : ").strip().upper()
        if again != "A":                                              # fixed: the loop never ended before
            break
    print("--HAVE A NICE DAY--")
else:
    print("OPPS!!!")
    print("YOU HAVE QUIT OUR PLATFORM")
    print("--HAVE A NICE DAY--")
