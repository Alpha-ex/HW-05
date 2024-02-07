class PhoneBookAssistant:
    def __init__(self):
        self.phone_book = {}

    def add_contact(self, name, phone):
        self.phone_book[name.lower()] = phone
        print("Contact added.")

    def change_contact(self, name, new_phone):
        if name.lower() in self.phone_book:
            self.phone_book[name.lower()] = new_phone
            print("Contact updated.")
        else:
            print("Contact not found.")

    def show_phone(self, name):
        if name.lower() in self.phone_book:
            print(f"Phone number for {name}: {self.phone_book[name.lower()]}")
        else:
            print("Contact not found.")

    def show_all(self):
        if self.phone_book:
            print("All contacts:")
            for name, phone in self.phone_book.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts available.")

    def parse_input(self, user_input):
        parts = user_input.split()
        command = parts[0].lower()

        if command == 'hello':
            print("How can I help you?")

        elif command == 'add':
            if len(parts) == 3:
                name, phone = parts[1], parts[2]
                self.add_contact(name, phone)
            else:
                print("Invalid command. Use: add <name> <phone number>")

        elif command == 'change':
            if len(parts) == 3:
                name, new_phone = parts[1], parts[2]
                self.change_contact(name, new_phone)
            else:
                print("Invalid command. Use: change <name> <new phone number>")

        elif command == 'phone':
            if len(parts) == 2:
                name = parts[1]
                self.show_phone(name)
            else:
                print("Invalid command. Use: phone <name>")

        elif command == 'all':
            self.show_all()

        elif command == 'exit' or command == 'close':
            print("Good bye!")
            exit()

        else:
            print("Invalid command.")

    def main(self):
        print("Welcome to the phone book!")

        while True:
            user_input = input("Enter command: ")
            self.parse_input(user_input)


if __name__ == "__main__":
    assistant = PhoneBookAssistant()
    assistant.main()