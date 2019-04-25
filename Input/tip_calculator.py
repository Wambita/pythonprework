print ("Enter your bill")
bill = int(input())

print ("Enter your level of satisfaction. Either Great(80-100), Good(60-80), Terrible(less than 60)")
level = int(input())

if level > 80:
    tip = 0.2 * bill

elif level > 60:
    tip = 0.15 * bill


else:
     tip = 0 * bill

total = bill + tip 

print("Your bill for your meal is:Kshs. " + str(bill) )

print(" Based on your level of satisfaction of: " + str(level) + "% , Your tip is: Kshs. " +str(tip) + " and Your total bill is:Kshs. " + str(total) )
