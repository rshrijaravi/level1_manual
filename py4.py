print("Bharathi supermark")
print("no 44,nehru street,puducherry")
print("------------------")
print("bill Recipt")
print("------------------")
sl=input("Enter the serial no:")
pr=input("Enter the particular:")
rate=int(input("Enter the rate:"))
Qty=int(input("Enter the Quaulity:"))
total=rate*Qty
print("total amount rs:",total)
gst=total*10/100
print("gst(10 per):",gst)
paid=total+gst
print("Amount to be paid rs:",paid)

