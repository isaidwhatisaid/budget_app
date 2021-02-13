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
food = Category('Food')
business = Category('Business')
entertainment = Category("Entertainment")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
categories = [business, food, entertainment]



def create_spend_chart(categories):

    # Get the totals of each category's withdrawals only
    cat_totals_dict = {}
    for i in categories:
        cat_totals_dict.update({i.name : 0})
        for j in i.ledger:
            if j['amount'] < 0:
                cat_totals_dict[i.name] += j['amount']
                
    # Calculate their percentage of total spend for each category
    total = 0
    cat_total = 0
    for i in cat_totals_dict:
        total += cat_totals_dict[i]
        cat_total += 1
    
    # Design the print layout string
    width = 3*(cat_total) + 1
    spaces = ' '*width
    rows = []
    for i in range(100,-1,-10):
        rows.append((str(i) + '|').rjust(4) + spaces)
    rows.append(' '*4 + '-'*(width))

    # Add the length of the longest category name to the bottom of the chart
    cat_lengths = []
    for i in categories:
        cat_lengths.append(len(i.name))
    cat_length = max(cat_lengths)
    for i in range(0,cat_length):
        rows.append(' '*(width+4))
        
    # Round down to 10% and design the bars for each category
    cat_bars = []
    height = 11
    for i in cat_totals_dict:
        cat_totals_dict[i] = math.floor(cat_totals_dict[i]/total*10)*10
        top = int(cat_totals_dict[i]/10) + 1
        cat_bars.append(' '*(height-top) + top*'o' + '-' + i + ' '*(cat_length-len(i)))
    
    # Make all the rows into lists of individual characters so they're mutable
    row_lists = []
    for row in rows:
        row_lists.append(list(row))

    # Loop through all the rows and add the content from the categories
    total_height = len(rows)
    spacing = list(range(5,25,3))
    for i in range(total_height):
        for j in range(len(categories)):
            row_lists[i][spacing[j]] = cat_bars[j][i]

    # Format the result to a single string
    new_rows = []
    for i in row_lists:
        new_rows.append(''.join(i))
    formatted = 'Percentage spent by category\n' + '\n'.join(new_rows)
    return formatted
