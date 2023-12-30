# This is the python portfolio project

# THIS IS A MORTGAGE CALCULATOR

# We need to establish an engagement between the customer(borrower) & the lender(institution)
from datetime import datetime

# Income Tax
income_tax = 0.38

# Dictionary for interest rates in the month
rate_dict = {
    'January': 0.08, 'February': 0.09, 'March': 0.1, 'April': 0.05, 'May': 0.02, 'June': 0.065, 
    'July': 0.057, 'August': 0.03, 'September': 0.043, 'October': 0.072, 'November': 0.09, 'December': 0.028
    }

# Borrower class defines the person who is getting the loan
class Loan:
    def __init__(self):
        self.principal_amount = 0
        # Net income will be generated due to the relationship between Loan (Child) and Borrower Class (parent)
        self.rate = 0
        self.down_payment = 0
        self.loan_length = 0

    # Calculate the interest rate
    def generate_interest_rate(self):
        current_month = datetime.now().strftime('%B')
        for key in rate_dict.keys():
            if key == current_month:
                self.rate = rate_dict[key]

        print("{month}'s interest rate is set out to be {rate}".format(rate = self.rate, month = current_month))

    def set_loan_length(self):
        self.loan_length = int(input('How many years do you want to finance the loan for?'))

    

class Borrower(Loan):
    def __init__(self):
        self.name = str(input("Let's start off, Could you please provide me with your name?\n"))
        self.age = int(input("What's your age?\n"))
        self.income = int(input("Finally, What's your current income?\n"))
        self.net_income = 0
        self.house_cost = int(input('Please input the total cost of the house that you are looking to finance?\n'))
        self.monthly_payment = 0

        # Accessing attributes from the parent class
        Loan.__init__(self)

    def __repr__(self):
        return "Hi {name}! It's a pleasure to meet you. Let me be the first to congratulate you on the journey to becoming a homeowner!".format(name = self.name)    

    def generate_net_income(self):
        self.net_income = self.income - (self.income * income_tax)
        print("Your net income after tax, comes out to be {net_income}".format(net_income = self.net_income))
    
    def set_down_payment(self):
        payment = int(input('How much money are you putting in as down payment for the house?\n'))
        self.down_payment = 100 * (payment/self.house_cost)

    def set_principal_amount(self):
        self.principal_amount = self.house_cost - (self.down_payment * self.house_cost/100)
        print('These are the following details that we have identified: \n')
        print('Down Payment: {down_payment}%'.format(down_payment = self.down_payment))
        print('Principal Loan Amount: {principal}\n'.format(principal = self.principal_amount))
    
    def set_monthly_payment(self):
        if self.rate != 0:
            monthly_rate = self.rate / 12
            months_period = self.loan_length * 12
            monthly_payment = (monthly_rate * self.principal_amount * (1 + monthly_rate) ** months_period) / (((1 + monthly_rate) ** months_period) - 1)
    
        else:
            monthly_payment = self.principal_amount / months_period
        
        print("Hey {name}, based on the details provided above. Here's your overall calculated monthly repayment: \n".format(name = self.name))
        # Here we used the format function to convert the floating point number to 2 decimal places. {:.2f} commands the upto two decimal places float value
        print("Monthly mortgage payment: {:.2f}\n\n".format(monthly_payment))



print("Hi There, Welcome to your very own Mortgage Calculator")

borrower_1 = Borrower()
borrower_1.generate_interest_rate()
borrower_1.set_down_payment()
borrower_1.set_principal_amount()

print("Let's calculate your monthly repayments! \n")

borrower_1.set_loan_length()
borrower_1.set_monthly_payment()
