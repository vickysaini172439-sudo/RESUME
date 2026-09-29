"""
STUDENT MANAGEMENT SYSTEM
Stores student records in a binary file (student.dat) using pickle.
Operations: Add, Search, Update, Remove, Display.

Author: Vicky
"""
import pickle
import os

FILE = "student.dat"

print("WELCOME TO OUR STUDENT MANAGEMENT SYSTEM")
print("YOU CAN PERFORM:\n1. ADD(): TO ADD NEW RECORDS\n2. Search(): TO INFER DETAILS OF ANY STUDENT"
      "\n3. Update(): TO CHANGE ANY DETAIL OF STUDENTS\n4. Remove(): TO DELETE THE RECORD OF ANY STUDENT"
      "\n5. Display(): TO DISPLAY ALL THE RECORDS SAVED")


# ---------- helper functions ----------
def read_all():
    """Read every record from the file and return them as a list."""
    records = []
    if not os.path.exists(FILE):
        return records
    with open(FILE, "rb") as f:
        try:
            while True:
                records.append(pickle.load(f))
        except EOFError:
            pass
    return records


def write_all(records):
    """Overwrite the file with the given list of records."""
    with open(FILE, "wb") as f:
        for d in records:
            pickle.dump(d, f)


def get_int(msg):
    """Keep asking until the user types a whole number."""
    while True:
        value = input(msg)
        if value.strip().isdigit():
            return int(value)
        print("PLEASE ENTER NUMBERS ONLY")


def get_mobile(msg):
    """Keep asking until the mobile number has exactly 10 digits."""
    while True:
        m = input(msg).strip()
        if m.isdigit() and len(m) == 10:
            return int(m)
        print("INVALID NUMBER (must be 10 digits)")


def get_gender(msg):
    G = input(msg).strip()
    if G == "1":
        return "Male"
    elif G == "2":
        return "Female"
    else:
        return "Other"


def show(d):
    for i in d:
        print("   ", i, "  :  ", d[i])
    print("   " + "-" * 30)


# ---------- main operations ----------
def ADD():
    A = get_int("Enter Admission Number: ")
    for d in read_all():
        if d["Adm"] == A:
            print("THIS ADMISSION NUMBER ALREADY EXISTS")
            return
    D = input("      Enter D.O.B of student (Format: dd/mm/yyyy): ")
    G = get_gender("      Gender of student:\n1.       Male\n2.       Female\n3.       Other\n")
    N = input("Enter Name of student: ")
    C = input("Enter Class of student: ")
    M = get_mobile("Enter Mobile Number: ")
    P = input("Enter Address of Residence: ")
    d = {"Adm": A, "D.O.B": D, "Gender": G, "Name": N, "Class": C, "Mobile no.": M, "Address": P}
    with open(FILE, "ab") as f:
        pickle.dump(d, f)
    print("RECORD ADDED SUCCESSFULLY")


def Search():
    adm = get_int("Enter Admission Number to get details: ")
    found = False
    for d in read_all():
        if d["Adm"] == adm:
            show(d)
            found = True
    if not found:
        print("NO RECORD FOUND")


def Update():
    adm = get_int("Enter Admission Number whose details to be changed: ")
    records = read_all()
    for d in records:
        if d["Adm"] == adm:
            u = get_int("Enter particular detail that you need to update:\n1. D.O.B\n2. Gender\n3. Name"
                        "\n4. Class\n5. Mobile no.\n6. Address\n")
            if u == 1:
                d["D.O.B"] = input("Enter updated details (Format: dd/mm/yyyy): ")
            elif u == 2:
                d["Gender"] = get_gender("Enter updated details:\n1. Male\n2. Female\n3. Other\n")
            elif u == 3:
                d["Name"] = input("Enter updated details: NAME: ")
            elif u == 4:
                d["Class"] = input("Enter updated details: CLASS: ")
            elif u == 5:
                d["Mobile no."] = get_mobile("Enter updated details: MOBILE NUMBER: ")
            elif u == 6:
                d["Address"] = input("Enter updated details: ADDRESS: ")
            else:
                print("INVALID CHOICE")
                return
            write_all(records)
            print("RECORD UPDATED SUCCESSFULLY")
            return
    print("NO RECORD FOUND")


def Remove():
    adm = get_int("Enter Admission Number whose details are to be removed: ")
    records = read_all()
    remaining = [d for d in records if d["Adm"] != adm]
    if len(remaining) == len(records):
        print("NO RECORD FOUND")
    else:
        write_all(remaining)
        print("TASK SUCCESSFULLY COMPLETED")


def Display():
    records = read_all()
    if not records:
        print("NO RECORDS SAVED YET")
    for z in records:
        show(z)


def Call():
    q = get_int("ENTER THE FUNCTION THAT YOU WANT TO PERFORM :\n      Format:\n      Enter 1 to call Add()"
                "\n      Enter 2 to call Search()\n      Enter 3 to call Update()\n      Enter 4 to call Remove()"
                "\n      Enter 5 to call Display()\n")
    if q == 1:
        ADD()
    elif q == 2:
        Search()
    elif q == 3:
        Update()
    elif q == 4:
        Remove()
    elif q == 5:
        Display()
    else:
        print("INVALID CHOICE")


while True:
    k = input("DO YOU WANT TO CONTINUE? enter y: ")
    if k.lower() == "y":
        Call()
    else:
        break
print("THANKS FOR COMING TO OUR PLATFORM")
