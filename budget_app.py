import math

class Category:

    # Constructor method for name of object and creating object ledger
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def __str__(self):
        rows = []
        # Design the category name row with the stars
        star_amount = round((30 - len(self.name))/2)
        self.title_row = '*'*star_amount + self.name + '*'*star_amount
        if len(self.title_row) == 29:
            self.title_row += '*'
        rows.append(self.title_row)
        # Parse and format each ledger row
        for i in self.ledger:
            # Display first 23 characters of the description
            row_desc = i['description'][:23]
            # Display the amount, right aligned and with 2 decimal places
            "%0.2f" % 10
            row_amt = str("%0.2f" % i['amount']).rjust(30-len(row_desc))
            each_row = row_desc + row_amt
            rows.append(each_row)
        # Use get_balance method to get the total
        total = "Total: " + str(self.get_balance())
        rows.append(total)
        # Join the rows list to make a returnable string
        display = '\n'.join(rows)
        return display

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



 # Testers    
test1 = Category('test1')
test2 = Category('test2')
test1.deposit(1.10, 'food')
test1.deposit(93.54, 'anything else this string needs to be really long')
test2.deposit(200, 'initial')
test1.withdraw(4.00, 'minus')
test2.withdraw(15.34, 'withdrawal')
test2.withdraw(39, 'look')
test1.transfer(4.25, test2)
print(test1.ledger)
print(test2.ledger)
cat_list = [test1, test2]

def create_spend_chart(cat_list):
    # Get the totals of each category's withdrawals only
    cat_totals_dict = {}
    for i in cat_list:
        cat_totals_dict.update({i.name : 0})
        for j in i.ledger:
            if j['amount'] < 0:
                cat_totals_dict[i.name] += j['amount']
                # print(i.name, j['amount'])
    print(cat_totals_dict)
    # Calculate their percentage of total spend rounded down to nearest 10%
    total = 0
    cat_total = 0
    for i in cat_totals_dict:
        total += cat_totals_dict[i]
        cat_total += 1
    print(total)
    for i in cat_totals_dict:
        cat_totals_dict[i] = math.floor(cat_totals_dict[i]/total*10)*10
    print(cat_totals_dict)
    # Design the print layout string
    width = 3*(cat_total) + 1
    


print(create_spend_chart(cat_list))
