print("Government of tamilnadu")
print("Electricity board")
print("----------------")
str1=input("enter the EB no:")
str2=input("enter the customer name:")
no1=int(input("Reading for previous month:"))
no2=int(input("reading for current month:"))
total=no2-no1
print("total unit consumed:",total)
paid=total*5
print("Amount to be paid :",paid)
