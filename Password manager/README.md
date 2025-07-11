# 🔐 Password Manager

A simple and secure console-based Password Manager built in Python.  
It lets you store login credentials for websites in a structured JSON file, along with timestamps.

---

## 📋 Features

- ✅ Add website credentials (username, password)
- ✅ Save everything in a structured `JSON` file
- ✅ View all saved credentials
- ✅ Timestamp added to each entry
- ✅ Error-handled: avoids crashing on missing files or invalid input

---

## 🧠 Technologies Used

- Python 3
- `json` module for data storage
- `datetime` for timestamps
- Loops, functions, and exception handling

---

## 📦 Example Data Structure (`passwords.json`)
```json
{
  "gmail.com": {
    "username": "teraphilo@gmail.com",
    "password": "mysecret123",
    "saved_at": "2025-07-07 14:00:00"
  },
  "facebook.com": {
    "username": "tera_fb",
    "password": "anotherpass",
    "saved_at": "2025-07-07 14:10:00"
  }
}
