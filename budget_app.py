class Category:

    # Constructor method for name of object
    def __init__(self, name):
        self.name = name
        self.ledger = []

    # Deposit method that appends description and amount to the ledger
    def deposit(self, amount, description = ''):
        self.ledger.append({'amount' : amount, 'description' : description})
    
    # Mithdraw method that appends description and negative amount to the ledger, as long as the funds are available
    def withdraw(self, amount, description = ''):
        # Use the check_funds method to check if the amount can be withdrawn from the available balance
        if not self.check_funds(amount):
            return False
        # Return true if funds are available and append the withdrawal to the ledger
        else: 
            self.ledger.append({'amount' : -amount, 'description' : description})
            return True
    
    # Get balance method that returns the current balance of the budget category
    def get_balance(self):
        funds = 0
        for i in self.ledger:
            funds += i['amount']
            funds = round(funds,2)
        return funds
    
    # Check funds method that checks if a given amount is greater than the balance of the budget category
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else: return True

    # Transfer method that transfers a given amount to a new category so long as the funds are available
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        else: return False
