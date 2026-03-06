# Company sales Calculator
import numpy as np
Months=["januray","february","march","april","may","june","july","august","september","october","november","december"]
Sales=[]  #stores the sales for each month
Investment=[] #stores the investment for each month
for month in Months:
    sale=float(input(f"Enter the sales for {month}:"))
    investment=float(input(f"Enter the investment for {month}:"))
    Sales.append(sale)
    Investment.append(investment)
Sales=np.array(Sales)
Investment=np.array(Investment)
print("Total sales for the year:",np.sum(Sales)) #sum of all sales for the year
print("Average sales per month:",np.mean(Sales)) #average sales per month for the year
print("Total investment for the year:",np.sum(Investment)) #sum of all investment for the year
print("Average investment per month:",np.mean(Investment)) #average investment per month for the year
if(np.sum(Sales)>np.sum(Investment)):
    print("The company is profitable for the year with a profit of",np.sum(Sales)-np.sum(Investment)) # total profit or loss for the year
else:
    print("The company is not profitable for the year with a loss of",np.sum(Investment)-np.sum(Sales)) #total loss for the year
Sales_max_month=np.argmax(Sales) #stores the index of the month with the highest sales
print(f"The highest sales is in {Months[Sales_max_month]} with sales of {Sales[Sales_max_month]}")
Sales_min_month=np.argmin(Sales) #stores the index of the month with the lowest sales
print(f"The lowest sales is in {Months[Sales_min_month]} with sales of {Sales[Sales_min_month]}")
avg_sales=np.mean(Sales) #stores the average sales for the year
for i in range(len(Sales)):
    if Sales[i]>avg_sales:
        print(f"{Months[i]} has above average sales with sales of {Sales[i]}") #month  above average sales
    else:
        print(f"{Months[i]} has below average sales with sales of {Sales[i]}") #month below average sales