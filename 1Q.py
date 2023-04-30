print("Please enter the quantity of each book")
book1 = int(input("Introduction To Python : "))
book2 = int(input("Python Libraries Cookbook : "))
book3 = int(input("Datascience In Python : "))
book1_amt = 499.00*book1
book2_amt = 855.00*book2
book3_amt = 645.00*book3
t_price = book1_amt+book2_amt+book3_amt
final_amt = t_price+(t_price*0.12)+ 250
print("Invoice---")
print("GST = 12%",end = " ")
print("Delivery Charges = 250")
print("Total amount for all the books is",end = " ")
print(final_amt)