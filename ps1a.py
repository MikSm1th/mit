# Problem Set 1
# Name: Michael Smith
# Time Spent: 5:00

## Problem 1 -- Paying the minimum

print('Problem 1 - input')
balance = float(input('Enter the outstanding balance on your credit card: '))
annual_interest = float(input('Enter the annual credit card interest rate as a decimal: '))
min_month_rate = float(input('Enter the minimum monthly payment as a decimal: '))

min_monthly_pay = min_month_rate * balance
interest_paid = (annual_interest/12.0) * balance
principle_paid = min_monthly_pay - interest_paid
remaining_balance = balance - principle_paid

def min_monthly_payment_for_a_year(balance, annual_interest, min_month_rate):
    total_paid = []
    balance_list = []
    for i in range(1,13):
        print('Month:', i)
        min_monthly_pay = min_month_rate * balance
        print(f'Minimum monthly payment: ${min_monthly_pay:.2f}')
        interest_paid = (annual_interest/12.0) * balance
        principle_paid = min_monthly_pay - interest_paid
        print(f'Principle paid: ${principle_paid:.2f}')
        balance = balance - principle_paid
        print(f'Remaining balance: ${balance:.2f}')
        total_paid.append(min_monthly_pay)
        balance_list.append(balance)
    return sum(total_paid), balance_list[-1]
    
if __name__ == "__main__":
    total_paid, balance_list_last = min_monthly_payment_for_a_year(balance, annual_interest, min_month_rate)
    print('RESULT')
    print(f'Total amount paid: ${total_paid:.2f}')
    print(f'Remaing balance: ${balance_list_last:.2f}')
