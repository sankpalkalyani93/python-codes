#1. Write a program using functions to Compute the monthly payment, given the loan amount, 
#   number of years and the annual interest rate.
#ans. 
def calculateMonthlyPayment(loan_amount, num_of_years, annual_interest_rate):
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    num_of_monthly_payment = num_of_years * 12

    monthly_payment = (
        loan_amount
        * monthly_interest_rate
        * (1 + monthly_interest_rate) ** num_of_monthly_payment
    ) / ((1 + monthly_interest_rate) ** num_of_monthly_payment - 1)

    return monthly_payment

loan_amount = float(input("Enter the loan amount : "))
num_of_years = float(input("Enter the number of years : "))
annual_interest_rate = float(input("Enter the annual interest rate : "))

monthly_payment = calculateMonthlyPayment(loan_amount, num_of_years, annual_interest_rate)

print("Monthly payment for loan : ", monthly_payment)


#2. write a program using function definition to print multiplication of all the numbers in a list.

def multiplicationOfListNumbers(list):
    result = 1
    for i in list:
        result *= i

    return result

list = [2, 3, 4, 5, 6, 8]
result = multiplicationOfListNumbers(list)

print("Result of multiplication of numbers in list : ", result)