import os

FILE_NAME = "expenses.txt"

sample_expenses = [
    ["Food", 120],
    ["Travel", 50],
    ["Stationery", 80]
]

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        for item in sample_expenses:
            f.write(item[0] + "," + str(item[1]) + "\n")
    print("Sample expenses added!\n")


expenses = []
with open(FILE_NAME, "r") as f:
    for line in f:
        category, amount = line.strip().split(",")
        expenses.append([category, float(amount)])


while True:
    print("\n--- Student Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))

        expenses.append([category, amount])

        # Save new expense
        with open(FILE_NAME, "a") as f:
            f.write(category + "," + str(amount) + "\n")

        print("Expense added!")

    elif choice == "2":
        print("\nYour Expenses:")
        for e in expenses:
            print(e[0], "-", e[1])

    elif choice == "3":
        total = sum(e[1] for e in expenses)
        print("Total spending:", total)

    elif choice == "4":
        print("Goodbye!")
        break

    else:

        print("Invalid choice. Try again.")
