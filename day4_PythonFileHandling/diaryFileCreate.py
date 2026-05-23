from datetime import datetime

DIARY_FILE = "my_diary.txt"


def add_entry():
    entry = input("Write your diary entry: \n")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(DIARY_FILE, "a", encoding="utf-8") as file:
        file.write(f"\n[{timestamp}]\n")
        file.write(entry + "\n")
        file.write("-" * 50 + "\n")

    print("\nDiary entry saved successfully!\n")


def view_entries():
    try:
        with open(DIARY_FILE, "r", encoding="utf-8") as file:
            content = file.read()

            if content.strip() == "":
                print("\nNo diary entries found.\n")
            else:
                print("\n--- Your Diary Entries ---\n")
                print(content)

    except FileNotFoundError:
        print("\nDiary file does not exist yet.\n")


while True:
    print("=" * 40)
    print("Simple Python Diary")
    print("=" * 40)
    print("1. Add Diary Entry")
    print("2. View Diary Entries")
    print("3. Exit")

    choice = input("\nEnter your choice (1-3): ")

    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        print("\nGoodbye!\n")
        break
    else:
        print("\nInvalid choice. Please try again.\n")

