class BankBot:
    def __init__(self):
        self.balance = 1000  # Initial account balance

    def check_balance(self):
        return f"Your account balance is ${self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. Your new balance is ${self.balance}"
        else:
            return "Invalid amount for deposit."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. Your new balance is ${self.balance}"
        elif amount <= 0:
            return "Invalid amount for withdrawal."
        else:
            return "Insufficient funds for withdrawal."

# Create a BankBot object
bank_bot = BankBot()

print("BankBot: Welcome to the BankBot! How can I assist you today?")

while True:
    print("\nOptions:")
    print("1. Check Balance")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. Quit")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == "1":
        print("BankBot:", bank_bot.check_balance())
    elif choice == "2":
        try:
            amount = float(input("Enter the deposit amount: $"))
            print("BankBot:", bank_bot.deposit(amount))
        except ValueError:
            print("BankBot: Please specify a valid deposit amount.")
    elif choice == "3":
        try:
            amount = float(input("Enter the withdrawal amount: $"))
            print("BankBot:", bank_bot.withdraw(amount))
        except ValueError:
            print("BankBot: Please specify a valid withdrawal amount.")
    elif choice == "4":
        print("BankBot: Thank you for using BankBot. Goodbye!")
        break
    else:
        print("BankBot: Invalid choice. Please select a valid option.")