"""Beginner-friendly ATM Management System
Concepts: variables, conditions, loops, functions, lists, dictionaries,
classes, objects, constructors, encapsulation, inheritance, polymorphism,
and exception handling.
"""


class Account:
    """Stores account details and performs basic banking operations."""

    def __init__(self, name, account_number, pin, balance=0):
        self.name = name
        self.account_number = account_number
        self.__pin = str(pin)  # Encapsulation: PIN is a private attribute
        self.balance = balance
        self.transactions = [f"Account opened with balance Rs. {balance:.2f}"]

    def check_pin(self, entered_pin):
        return self.__pin == entered_pin

    def check_balance(self):
        print(f"\nAvailable balance: Rs. {self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        self.balance += amount
        self.transactions.append(f"Deposited Rs. {amount:.2f}")
        print(f"Rs. {amount:.2f} deposited successfully.")
        self.check_balance()

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawn Rs. {amount:.2f}")
            print(f"Please collect Rs. {amount:.2f}.")
            self.check_balance()

    def show_details(self):
        print(f"\nAccount holder: {self.name}")
        print(f"Account number: {self.account_number}")
        self.check_balance()

    def show_statement(self):
        print("\n========== MINI STATEMENT ==========")
        for number, transaction in enumerate(self.transactions, start=1):
            print(f"{number}. {transaction}")
        print("====================================")

    def change_pin(self, old_pin, new_pin):
        if not self.check_pin(old_pin):
            print("Incorrect current PIN.")
        elif len(new_pin) != 4 or not new_pin.isdigit():
            print("New PIN must contain exactly 4 digits.")
        else:
            self.__pin = new_pin
            self.transactions.append("PIN changed")
            print("PIN changed successfully.")

    def receive_transfer(self, amount, sender_name):
        self.balance += amount
        self.transactions.append(f"Received Rs. {amount:.2f} from {sender_name}")


class StudentAccount(Account):
    """Example inheritance: a student account customizes account details."""

    def show_details(self):
        print("\n========== STUDENT ACCOUNT ==========")
        super().show_details()
        print("Account type: Student")


class ATM:
    def __init__(self):
        # Dictionary stores accounts using account number as the key.
        self.accounts = {
            "1001": StudentAccount("Zahid", "1001", "1234", 5000),
            "1002": Account("Rahul", "1002", "5678", 2500),
            "1003": Account("Ayesha", "1003", "4321", 7500),
        }

    @staticmethod
    def read_amount(message):
        try:
            amount = float(input(message))
            return amount
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

    def login(self):
        print("\n========== WELCOME TO PYTHON ATM ==========")
        account_number = input("Enter account number: ").strip()
        account = self.accounts.get(account_number)

        if account is None:
            print("Account not found.")
            return None

        for attempt in range(3):
            pin = input("Enter 4-digit PIN: ").strip()
            if account.check_pin(pin):
                print(f"\nWelcome, {account.name}!")
                return account
            remaining = 2 - attempt
            if remaining > 0:
                print(f"Incorrect PIN. Attempts remaining: {remaining}")

        print("Too many incorrect attempts. Returning to main menu.")
        return None

    def transfer(self, sender):
        receiver_number = input("Enter receiver account number: ").strip()
        receiver = self.accounts.get(receiver_number)

        if receiver is None:
            print("Receiver account not found.")
            return
        if receiver.account_number == sender.account_number:
            print("You cannot transfer money to your own account.")
            return

        amount = self.read_amount("Enter amount to transfer: Rs. ")
        if amount is None:
            return
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > sender.balance:
            print("Insufficient balance.")
        else:
            sender.balance -= amount
            receiver.receive_transfer(amount, sender.name)
            sender.transactions.append(
                f"Transferred Rs. {amount:.2f} to {receiver.name} ({receiver.account_number})"
            )
            print(f"Rs. {amount:.2f} transferred successfully to {receiver.name}.")
            sender.check_balance()

    def account_menu(self, account):
        while True:
            print("\n------------ ATM MENU ------------")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transfer Money")
            print("5. Mini Statement")
            print("6. Account Details")
            print("7. Change PIN")
            print("8. Logout")
            print("----------------------------------")

            choice = input("Choose an option (1-8): ").strip()

            if choice == "1":
                account.check_balance()
            elif choice == "2":
                amount = self.read_amount("Enter deposit amount: Rs. ")
                if amount is not None:
                    account.deposit(amount)
            elif choice == "3":
                amount = self.read_amount("Enter withdrawal amount: Rs. ")
                if amount is not None:
                    account.withdraw(amount)
            elif choice == "4":
                self.transfer(account)
            elif choice == "5":
                account.show_statement()
            elif choice == "6":
                account.show_details()
            elif choice == "7":
                old_pin = input("Enter current PIN: ").strip()
                new_pin = input("Enter new 4-digit PIN: ").strip()
                account.change_pin(old_pin, new_pin)
            elif choice == "8":
                print(f"Goodbye, {account.name}! You have logged out.")
                break
            else:
                print("Invalid choice. Please select 1 to 8.")

    def run(self):
        while True:
            print("\n1. Login")
            print("2. Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                account = self.login()
                if account is not None:
                    self.account_menu(account)
            elif choice == "2":
                print("Thank you for using Python ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    atm = ATM()
    atm.run()
