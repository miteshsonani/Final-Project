class Category:
    # Constructor to initialize a budget category and its ledger
    def __init__(self, category):
        self.category = category    # Name of the category (e.g., "Food", "Clothing")
        self.ledger = list()        # List to store all transactions (deposits and withdrawals)

    # Method to add deposits to the ledger
    def deposit(self, amount, description):
        amount = float(amount)
        self.ledger.append({"amount": amount, "description": description})  # Add deposit to ledger

    # Method to add withdrawals to the ledger
    def withdraw(self, amount, description):
        amount = float(amount)
        if self.check_funds(amount):    # Check if sufficient funds are available
            #amount = 0 - float(amount)
            self.ledger.append({"amount": -amount, "description": description}) # Add withdrawal as a negative amount
            print(self.category, "Ledger : ", self.ledger, '\n')
            return True # Withdrawal successful
        return False    # Insufficient funds

     # Method to calculate the current balance
    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)  # Sum of all amounts in the ledger

    # Method to transfer funds between categories
    def transfer(self, amount, budget_category):
    # amount = float(input("Enter transfer category amount:"))
    # description = input("Enter transfer category amount description:")
    # if "clothing" in description:
    #     budget_category = Category("Clothing")
    # if "food" in description:
    #     budget_category = Category("Food")
    # if "entertainment" in description:
    #     budget_category = Category("Entertainment")
    # else:
    #     return "Write proper category"
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True # Transfer successful
        return False    # Insufficient funds

    # Method to check if enough funds are available
    def check_funds(self, amount):
        return float(amount) <= self.get_balance()  # Return True if sufficient funds, False otherwise

    # Method to display the category in a formatted string
    def __str__(self):
        title = f"{self.category.center(30, '*')}\n"    
        items = ""
        for item in self.ledger:
            items += f"{item['description'].ljust(23, ' ')}{item['amount']:>7.2f}\n"    # Format description and amount
        total = f"Total: {self.get_balance():.2f}"  # Calculate total balance
        return title + items + total + '\n' # Combine title, ledger items, and total balance
  

# Function to create a spending bar chart for categories
def create_spend_chart(categories):
    s = "Percentage spent by Category\n"

    spendings = []  # List to store spending amounts for each category

    # Calculate spendings and total
    for category in categories:
        total = 0
        for item in category.ledger:
            if item['amount'] < 0:  # Only consider withdrawals
                total += item['amount']
        spendings.append(total * (-1))  # Convert to positive value

    print('\n', "Spendings", spendings, '\n')   

    total_spent = sum(spendings)    # Total spending across all categories
    print('\n', "Total Spent : ", total_spent, '\n')

    # Add the percentage lines
    for n in range(100, -1, -10):   # Iterate from 100% to 0% in steps of 10
        s += str(n).rjust(3) + '|'  # Add the percentage label
        i = 0
        for spending in spendings[:3]:
            percent = (spending / total_spent) * 100
            if percent >= n:
                s += ' o'   # Add 'o' for spending above or equal to the percentage
            else:
                s += '  '   # Add blank space for lower spending
        i += 1
        s += '\n'   # Newline after each percentage level
      
    # Add the separator line
    L = len(categories)
    s += '   -' + '---' * L + '\n'

    # Add category names vertically below the chart

    max_len = 0
    for category in categories: # Find the longest category name
        if len(category.category) > max_len:
            max_len = len(category.category)

    for i in range(max_len):
        s += '     '    # Initial spacing
        for category in categories:
            if i < len(category.category):
                s += category.category[i]   # Add character from the category name
            else:
                s += ' '    # Add blank space for shorter names
            s += '  '   # Spacing between characters
        s += '\n'   # Newline after each row

    return s.strip()    # Return the completed chart as a string


# Exampale
# Create categories
food_category = Category("Food")
clothing_category = Category("Clothing")
entertainment_category = Category("Entertainment")

# Add transactions to the categories
food_category.deposit(1000, "initial deposit")
food_category.withdraw(10.15, "groceries")
food_category.withdraw(15.89, "restaurant and more food")
food_category.transfer(50, clothing_category)

clothing_category.deposit(500, "initial deposit")
clothing_category.withdraw(20, "clothing")

entertainment_category.deposit(200, "initial deposit")
entertainment_category.withdraw(15, "movie")

# Print category details
print(food_category)
print(clothing_category)
print(entertainment_category)

# Print the spending bar chart
print(create_spend_chart([food_category, clothing_category, entertainment_category]))


# food_category.deposit(input("Enter deposit amount:"),
#                       input("Enter deposit amount description:"))
# food_category.withdraw(input("Enter withdrawal amount:"),
#                        input("Enter withdrawal amount description:"))
# food_category.withdraw(input("Enter withdrawal amount:"),
#                        input("Enter withdrawal amount description:"))
# food_category.transfer(50, clothing_category)

# print(food_category)
# print(clothing_category)
# print(entertainment_category)



        