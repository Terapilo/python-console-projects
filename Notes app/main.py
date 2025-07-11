from datetime import datetime

FILENAME = "notes.txt"

def add_note():
    note = input("Enter your note: ").strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILENAME, "a") as f:
        f.write(f"[{timestamp}] {note}\n")
    print("Note saved!")

def view_notes():
    try:
        with open(FILENAME, "r") as f:
            content = f.read().strip()
            if not content:
                print("No notes yet")
            else:
                print("\nYour notes:")
                print(content)
    except FileNotFoundError:
        print("No notes file found.")

def clear_notes():
    confirm = input("Are you sure you want to delete all notes? (yes/no): ").strip().lower()
    if confirm == "yes":
        open(FILENAME, "w").close()  # Empty the file
        print("All notes deleted")
    else:
        print("Deletion cancelled")

# === Main loop ===
while True:
    print("\n=== Notes App ===")
    print("1: Add note")
    print("2: View notes")
    print("3: Delete notes")
    print("4: Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        clear_notes()
    elif choice == "4":
        print("Exiting notes app...")
        break
