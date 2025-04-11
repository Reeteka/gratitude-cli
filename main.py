from journal import Journal
from utils import show_tip_of_the_day, splash_screen
import os

def main():
    splash_screen()
    show_tip_of_the_day()
    journal_obj = Journal()

    while True:
        print("\nMenu:")
        print("1. Add a new gratitude entry")
        print("2. View past entries")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            entry = input("What are you grateful for today? ")
            journal.add_entry(entry)
        elif choice == '2':
            journal.view_entries()
        elif choice == '3':
            print("Bye! Remember to be thankful 🌸")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
