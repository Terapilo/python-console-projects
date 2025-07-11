# 💰 Expense Tracker

A simple and effective Python console app to record and manage daily expenses. It saves your entries to a local text file along with a timestamp, and calculates your total spending.

This app was built as part of a hands-on journey to learn file handling, user input, and error-proof logic in Python.

---

## 🚀 Features

- 📝 Add a new expense with description and amount
- 📄 View all saved expenses
- 🧮 Automatically calculates total spent
- 🕒 Timestamp added to every entry
- ❌ Handles invalid inputs and missing file

---

## 💡 How It Works

1. User chooses an action: Add, View, or Exit.
2. On Add:
   - Inputs a short description and amount
   - App saves it with a date/time to `expenses.txt`
3. On View:
   - Reads and prints each line from file
   - Adds all amounts and displays the total

---

## 🔧 Tech Used

- Python 3
- File I/O: `open()`, `read()`, `write()`
- Exception handling: `try/except`
- `datetime` module

---

## 📸 Sample Output
=== EXPENSE TRACKER ===
1: Add Expense
2: View Expenses
3: Exit

Enter description: Snacks
Enter amount: 50
✅ Expense saved!

📄 Your Expenses:
2025-07-07 14:25:12 | Snacks - ₹50

💰 Total Spent: ₹50


---

## ▶️ How to Run

```bash
python expense_tracker.py

