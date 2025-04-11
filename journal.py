from storage import save_entry, load_entries

class Journal:
    def __init__(self):
        self.entries = load_entries()

    def add_entry(self, text):
        entry = {"text": text}
        self.entries.append(entry)
        save_entry(self.entries)
        print("✨ Entry saved!")

    def view_entries(self):
        if not self.entries:
            print("No entries yet. Start journaling today! 📓")
        for i, entry in enumerate(self.entries, start=1):
            print(f"{i}. {entry['text']}")
