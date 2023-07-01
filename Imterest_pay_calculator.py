# collect the neccessary input : principle ,interest rate, years
# calculate the monthly payment
# show to the user
def main():
    print("This is monthly payment loan calculator")
    print("")

    principle = float(input("enter the loan amount: "))
    apr = float(input("enter the annual interest rate: "))

    years = int(input("Enter the amount of years: "))

    monthly_interest_rate = apr/1200
    months = years *12
    monthly_payment = principle*monthly_interest_rate/(1-(1+monthly_interest_rate)**(-months))

    print("The monthly payment for this loan is: %.2f"%monthly_payment)
main()