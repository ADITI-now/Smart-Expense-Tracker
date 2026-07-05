print("-----------Welcome, To the Smart Expense Tracker----------")

expenses = []


def save_expenses():

    with open("expenses.txt", "w") as f:

        for expense in expenses:

            f.write(
                expense["name"] + "," +
                str(expense["amount"]) + "," +
                expense["category"] + "," +
                expense["month"] + "\n"
            )


def add_expense():
   
        expense_name = input("Enter your expense name: ")
        expense_amount = float(input("Enter Amount: "))
        expense_category = input("Enter Category: ").strip().lower()
        expense_month = input("Enter Month: ").strip().lower()

        expense = {
            "name": expense_name,
            "amount": expense_amount,
            "category": expense_category,
            "month":expense_month
        }

        expenses.append(expense)

        save_expenses()
        

        print("Expense added successfully!")

def view_expenses():

      if len(expenses) == 0:
            print("No expenses found.")

      else:
            print("------ Your Expenses ------")

            for expense in expenses:
                print("Name     :", expense["name"])
                print("Amount   :", expense["amount"])
                print("Category :", expense["category"])
                print("Month    :", expense["month"])
                print("--------------------------")



def budget_summary():    
      total = 0

      for expense in expenses:
         total = total + expense["amount"]

      print("------ Budget Summary ------")
      print("Total Expenses:", total)


def spending_insights():    
       food_total = 0
       travel_total = 0
       entertainment_total = 0

       for expense in expenses:

            if expense["category"] == "food":
             food_total = food_total + expense["amount"]

            elif expense["category"] == "travel":
             travel_total = travel_total + expense["amount"]

            elif expense["category"] == "entertainment":
             entertainment_total = entertainment_total + expense["amount"]

       print("------ Spending Insights ------")
       print("Food :", food_total)
       print("Travel :", travel_total)
       print("Entertainment :", entertainment_total)     

def monthly_report():
    report_month = input("Enter Month: ").strip().lower()

    found = False

    for expense in expenses:

        if expense["month"] == report_month:

            found = True

            print("Name     :", expense["name"])
            print("Amount   :", expense["amount"])
            print("Category :", expense["category"])
            print("Month    :", expense["month"])
            print("--------------------------")

    if not found:
           print("No expenses found for this month.")


def delete_expense(): 
    if not expenses:
     print("No expenses to delete.")
     return
 

    print("-------------Expenses------------")

    for index, expense in enumerate(expenses, start=1):
     print(index, expense["name"],"-",expense["amount"])
    
    expense_number = int(input("Enter expense number to delete: "))

    expenses.pop(expense_number - 1)
    save_expenses()
    print("Expense deleted successfully!")


try:
    with open("expenses.txt", "r") as f:

     for line in f:
        line = line.strip()
        parts = line.split(",")


        expense = {
    "name": parts[0],
    "amount": float(parts[1]),
    "category": parts[2],
    "month": parts[3]
}

        expenses.append(expense)        

except FileNotFoundError:
    pass

while True:
    print("\nMenu")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Budget Summary")
    print("4. Spending Insights")
    print("5. Monthly Report")
    print("6. Delete Expense")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice here: "))

    except ValueError:
        print("❌ Please enter a valid number!")
        continue

    if choice == 1:
        add_expense()

    elif choice == 2:
        view_expenses()

    elif choice == 3:  
       budget_summary()


    elif choice == 4:
        spending_insights()

    elif choice == 5:
       monthly_report()


    elif choice==6:
        delete_expense()


    elif choice == 7:
        print("Thank you for using Smart Expense Tracker!")
        break
    else:
      print("❌ Invalid choice! Please try again.")