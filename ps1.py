# Problem Set 1
# Name: Michael Smith
# Time Spent: 5:00

## Problem 1 -- Paying the minimum

# print('Problem 1 - input')
# balance = float(input('Enter the outstanding balance on your credit card: '))
# annual_interest = float(input('Enter the annual credit card interest rate as a decimal: '))
# min_month_rate = float(input('Enter the minimum monthly payment as a decimal: '))

# min_monthly_pay = min_month_rate * balance
# interest_paid = (annual_interest/12) * balance
# principle_paid = min_monthly_pay - interest_paid
# remaining_balance = balance - principle_paid

# def min_monthly_payment_for_a_year(balance, annual_interest, min_month_rate):
#     print(f'Starting balance: ${balance:.2f}')
#     for i in range(1,13):
#         print('Month:', i)
#         min_monthly_pay = float(min_month_rate) * balance
#         print(f'Minimum monthly payment: ${min_monthly_pay:.2f}')
#         interest_paid = (float(annual_interest)/12.0) * balance
#         principle_paid = min_monthly_pay - interest_paid
#         print(f'Principle paid: ${principle_paid:.2f}')
#         balance = balance - principle_paid
#         print(f'Remaining balance: ${balance:.2f}')

def twelve_months_paid(balance, annual_interest, payment):
    '''
    Calculates twelve months of credit cards paid. 
    '''
    monthly_interest_rate = annual_interest/12.0
    previous_balance = balance
    minimum_monthly_payment = payment
    pay_list = []
    for i in range(1,13):
        updated_balance = previous_balance * (1 + monthly_interest_rate) - minimum_monthly_payment
        previous_balance = updated_balance
        pay_list.append((minimum_monthly_payment,i,previous_balance))
    return pay_list

def calculate_pay_debt_in_a_year(balance):
    '''
    Calculates paying off debt in a year.
    '''
    end_balance = balance
    payment = 10
    while end_balance > 0: 
        payment = payment + 10
        pay_list = twelve_months_paid(balance, annual_interest, payment)
        payment, month, end_balance = pay_list[-1]

    less_than_zero = [i for i in pay_list if i[2] < 0]
    paid_off = [[(i) for i, j, k in less_than_zero], 
               [ j for i, j, k in less_than_zero ],
               [ k for i, j, k in less_than_zero]]
    payment2, month2, balance2 = paid_off[0][0], min(paid_off[1]), max(paid_off[2])
    return payment2, month2, balance2

    
if __name__ == "__main__":
#     print("Program output - Problem 1 -- Paying the minimum:\n") 
#     min_monthly_payment_for_a_year(balance, annual_interest, min_month_rate)
#     print("\nProblem 1 - Output end.")

    print('Problem 2 input')
    balance =  float(input('Enter the outstanding balance on your credit card: '))
    annual_interest = float(input('Enter the annual credit card interest rate as a decimal: '))
    
    print("\nProgram output - Problem 2 -- Paying Debt off in a Year")
    payment2, month2, balance2 = calculate_pay_debt_in_a_year(balance)

    print('\nRESULT')
    print(f'\nMonthly payment to pay off debt in a year: ${payment2:.2f}')
    print(f'\nNumber of months needed: {month2}')
    print(f'\nBalance: ${balance2:.2f}')
    print("\nProblem 2 - Output end.")
