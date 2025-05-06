class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            break
        elif action in ['deposit', 'withdraw']:
            while True:
                try:
                    amount = float(input(f" Enter the amount to {action}:$"))
                    if amount < 0:
                        print("Amouts must be positive. Please try again.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            if action == 'deposit':
                cb.deposit(amount)
            else:
                cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")
if __name__ == "__main__":
    main()
# The code is a simple checkbook program that allows users to deposit, withdraw, and check their balance.