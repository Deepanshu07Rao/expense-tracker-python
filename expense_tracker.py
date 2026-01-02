income = float(input("Enter your income ="))
               
n = int(input("how many expences you have?"))
expenses = []
for i in range(n):
    amount = float(input(f"Enter expense {i+1}: "))
    expenses.append(amount)
total_expense = sum(expenses)
balance = income - total_expense
print("\n----- Expense Summary -----")
print("Total Expense =", total_expense)
print("Remaining Balance =", balance)
if balance < 0:
    print("Warning: You are overspending!")


    
