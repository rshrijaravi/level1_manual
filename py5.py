print("shrija international[p] ltd")
print("NO.15 nagapura dist,bangulore")
print("------------------------")
print("Employee payroll system")
print("------------------")
Id=int(input("Enter the employee Id:"))
ename=input("Enter the employee name:")
salary=int(input("enter the salary:"))
print("Income")
bonas=salary*20/100
print("overtime(20 percentage):")
ot=salary*10/100
print("overtime(10 percentage):")
ta=salary*5/100
print("travel allovance(5 percentage):",ta)
grosspay=salary+bonas+ot+ta
print("grosspay in rupees:",grosspay)
             
