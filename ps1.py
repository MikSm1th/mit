# paying off credit card debt

# define variables

balance = 5000
annual_interest = 0.18
min_month_rate = 0.02

min_monthly_pay = min_month_rate * balance
interest_paid = (annual_interest/12) * balance
principle_paid = min_monthly_pay - interest_paid
remaining_balance = balance - principle_paid




if __name__ == "__main__":
    print("Program output:\n") 
    print("minimun_monthly_payment = ",  min_monthly_pay)        
    print("\nOutput end.")
