# 🧮 Error-Handled Calculator

A robust Python console calculator that performs basic arithmetic operations and gracefully handles invalid inputs. This project was built to practice input validation, error handling, and clean user interaction in a terminal environment.

---

## 🚀 Features

- ➕ Addition  
- ➖ Subtraction  
- ✖️ Multiplication  
- ➗ Division (with divide-by-zero protection)  
- ❌ Input validation using `try`/`except`  
- 🔄 Continuous usage with exit option

---

## 💻 How It Works

1. The user chooses an operation (1–4).
2. The user inputs two numbers.
3. The calculator performs the operation and prints the result.
4. If the input is invalid (e.g., text or 0 in division), it shows an error and restarts.

---

## 🔧 Technologies Used

- Python 3
- Control Flow (`if/elif/else`)
- Exception Handling (`try/except`)
- Loops

---

## 📸 Sample Output
=== CALCULATOR ===
1: Add
2: Subtract
3: Multiply
4: Divide
5: Exit
Choose an operation (1-5): 4
Enter first number: 10
Enter second number: 0
❌ Cannot divide by zero.


---

## ▶️ How to Run

```bash
python calculator.py

