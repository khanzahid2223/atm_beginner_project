# Python ATM Management System (Beginner Project)

A console-based ATM simulation built using core Python concepts. It uses no external libraries or database.

## Features
- Login with sample account number and PIN
- Check balance, deposit, and withdraw money
- Transfer money between sample accounts
- Mini statement stored in a list during the current program run
- View account details and change PIN
- Input validation and exception handling
- Three PIN attempts per login session

## Python concepts demonstrated
- Variables, strings, numbers, input/output
- `if` / `elif` / `else`, `for` and `while` loops
- Functions and methods
- Lists, dictionaries, and `enumerate`
- Classes, objects, constructors, and `self`
- Encapsulation with a private PIN attribute
- Inheritance with `StudentAccount`
- Polymorphism by overriding `show_details`
- Exception handling with `try` / `except`

## Run in VS Code
1. Install Python 3 if it is not already installed.
2. Open this folder in VS Code.
3. Open Terminal → New Terminal.
4. Run `python main.py` (or `py main.py` on Windows if needed).

## Demo accounts
| Account number | PIN | Starting balance |
|---|---|---:|
| 1001 | 1234 | Rs. 5,000 |
| 1002 | 5678 | Rs. 2,500 |
| 1003 | 4321 | Rs. 7,500 |

## Important limitations
This is a learning simulation, not real banking software. Accounts and transaction history reset when the program restarts. Do not use real PINs or financial information.
