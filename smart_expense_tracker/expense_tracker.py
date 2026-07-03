print("-----------Welcome, To the Smart Expense Tracker----------")

expenses = []

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
    print("6. Exit")

    try:
        choice = int(input("Enter your choice here: "))

    except ValueError:
        print("❌ Please enter a valid number!")
        continue

    if choice == 1:
        expense_name = input("Enter your expense name: ")
        expense_amount = float(input("Enter Amount: "))
        expense_category = input("Enter Category: ")
        expense_month = input("Enter Month: ")

        expense = {
            "name": expense_name,
            "amount": expense_amount,
            "category": expense_category,
            "month":expense_month
        }

        expenses.append(expense)

        with open("expenses.txt", "a") as f:
          f.write(expense_name + "," + str(expense_amount) + "," + expense_category + "," + expense_month + "\n")
       
        

        print("Expense added successfully!")

    elif choice == 2:
        
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
    elif choice == 3:  
       total = 0

       for expense in expenses:
        total = total + expense["amount"]

       print("------ Budget Summary ------")
       print("Total Expenses:", total)

    elif choice == 4:

       food_total = 0
       travel_total = 0
       entertainment_total = 0

       for expense in expenses:

            if expense["category"] == "Food":
             food_total = food_total + expense["amount"]

            elif expense["category"] == "Travel":
             travel_total = travel_total + expense["amount"]

            elif expense["category"] == "Entertainment":
             entertainment_total = entertainment_total + expense["amount"]

       print("------ Spending Insights ------")
       print("Food :", food_total)
       print("Travel :", travel_total)
       print("Entertainment :", entertainment_total)


    elif choice == 5:

     report_month = input("Enter Month: ")

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

    elif choice == 6:
        print("Thank you for using Smart Expense Tracker!")
        break
    else:
      print("❌ Invalid choice! Please try again.")