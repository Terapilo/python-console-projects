from datetime import datetime

while True:
    print("\n=== EXPENSE TRACKER ===")
    print("1: Add Expense")
    print("2: View Expenses")
    print("3: Exit")

    option = input("Enter the option you want: ").strip()

    if option == '1':
        task = input("Enter description: ").strip()
        
        try:
            amount = int(input("Enter the amount: ").strip())
        except ValueError:
            print("❌ Please enter a valid number for amount.")
            continue

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open("expenses.txt", "a", encoding="utf-8") as f:
                f.write(f"{timestamp} | {task} - ₹{amount}\n")  # <-- newline included
            print("✅ Expense saved!")
        except Exception as e:
            print(f"❌ Failed to save expense: {e}")

    elif option == '2':
        try:
            with open("expenses.txt", "r", encoding="utf-8") as f:
                print("\n📄 Your Expenses:")
                total = 0
                for line in f:
                    line = line.strip()
                    if not line:
                        continue  # skip blank lines
                    print(line)
                    try:
                        amt = int(line.split("₹")[1])
                        total += amt
                    except (IndexError, ValueError):
                        print(f"⚠️ Couldn't parse amount in: {line}")
                print(f"\n💰 Total Spent: ₹{total}")
        except FileNotFoundError:
            print("❌ No expenses found yet.")

    elif option == '3':
        print("👋 Exiting Expense Tracker...")
        break

    else:
        print("❌ Invalid option. Choose 1, 2, or 3.")
