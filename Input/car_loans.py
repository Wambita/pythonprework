print("Enter the loan amount ")
loan = int(input())

print("Enter the amount of salary ")
salary = int(input())

print("Enter the interest rate(%) ")
rate = int(input())

rates = rate/100

installment =  rates * salary
print("Installment per month")
print(installment)

time = loan / installment
years = time /12

print("You have " + str(years) + "  years to repay your loan")

print("You have " + str(time) + " months to repay your loan")