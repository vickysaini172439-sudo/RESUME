# Python Projects

Console programs I wrote while teaching myself Python: menu-driven record systems, billing tools, a password generator, small games and file-handling practice.

**Portfolio:** https://vicky-cse.vercel.app

| Project | What it does | Concepts |
|---|---|---|
| [Student Management System](student-management/student_management.py) | Add, search, update, remove and display student records | Binary files (`pickle`), functions, input validation |
| [Food Ordering System](food-ordering-system/food_ordering_system.py) | Choose a restaurant, order from 6 menu categories, get a bill; each order is saved | Dictionaries, loops, `pickle` |
| [GST Bill Calculator](gst-bill-calculator/gst_bill_calculator.py) | Applies the GST rate for each item category and prints a formatted bill | `pickle`, string formatting |
| [GST Billing & Inventory System](gst-billing-inventory/gst_billing_inventory.py) | Products, stock purchases, sales with GST, price details and profit report | Dictionaries, functions, error handling |
| [Password Generator](password-generator/password_generator.py) | Makes strong 8-character passwords with upper/lowercase letters, digits and symbols | `secrets` module (secure randomness) |
| [Stone Paper Scissor](rock-paper-scissors/rock_paper_scissors.py) | Play against the computer with a running score | `random`, conditionals |
| [Daily Activity Tracker](activity-tracker/activity_tracker.py) | Logs what you did in each 30-min / 1-hr / 2-hr slot and saves the day's log | Loops, f-strings, text files, `datetime` |
| [Periodic Table Explorer](periodic-table/periodic_table.py) | Enter an atomic number to see the name, symbol, atomic mass, electronegativity, block and period of any of the 118 elements | Lists, functions, input validation |

## How to run

Each program runs on plain Python 3, with nothing to install:

```
cd student-management
python student_management.py
```

## Fixes made while cleaning up the code

- **Student Management:** gender choice always saved "Other" (number compared with text); "not found" never printed; Update and Remove could not rewrite records in the file. Now reads all records, changes them and writes the file back.
- **GST Bill Calculator:** the total used the price of one unit instead of price × quantity; typo `/n` in the menu; invalid category crashed the program.
- **Food Ordering System:** the "Cake and Biscuits" category never matched; an unknown item crashed the program; the contact number was never saved (`CONTACT:` instead of `CONTACT =`); the order file was created but never used.
- **Password Generator:** switched from `random` to `secrets`, which is meant for passwords, and shuffled the characters so the pattern can't be guessed.
- **Stone Paper Scissor:** "play again?" compared the answer with a variable instead of the text `"n"`, so the game never stopped.
- **Periodic Table Explorer:** block checks like `v==49 or 50` were always true, so blocks came out wrong; several periods were wrong; Kr/Rb masses were swapped; numbers outside 1–118 crashed; the loop never ended. The 12 repeated code blocks are now one, using the same data lists.
- **Activity Tracker:** `input()` was given several arguments, which crashes Python; time slots are now shown correctly (12:00 AM to 11:59 PM).
