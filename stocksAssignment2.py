#CS501A
#Ezinne Ndumnwere
#Stocks Assignment
#User Input:
buying_comm_rate=float(input("Enter commission rate percentage on stock purchased: "))
selling_comm_rate=float(input("Enter commission rate percentage on stock sale: "))
stocks_bought=float(input("Enter the number of stocks purchased: "))
stocks_sold=float(input("Enter the number of stocks sold: "))
purchase_price=float(input("Enter the purchase price per stock: "))
selling_price=float(input("Enter the selling price per stock: "))

#Calculations:
amountPaidForStock=(stocks_bought*purchase_price)
purchaseCommission=(buying_comm_rate*amountPaidForStock)
totalPaid=(amountPaidForStock+purchaseCommission)
stockSoldFor=(stocks_sold*selling_price)
sellingCommission=(selling_comm_rate*stockSoldFor)
totalReceived=(stockSoldFor-sellingCommission)
profit=(totalReceived-totalPaid)

#Print Results:
print(f"Amount paid for the stock: ${amountPaidForStock:.2f}")
print(f"Comission paid on the purchase: ${purchaseCommission:.2f}")
print(f"Amount the stock sold for: ${stockSoldFor:.2f}")
print(f"commission paid on sale: ${sellingCommission:.2f}")
print(f"profit/loss: ${profit:.2f}")
  
