def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name please."
        except KeyError:
            return "Contact with this name does not exist!"
    return inner

@input_error
def add_contact(contacts, args):
    name, phone = args
    if name in contacts:
        return "Contact with this name already exists!"
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(contacts, args):
    name = args[0]
    return contacts[name]

@input_error
def change_contact(contacts, args):
    name, phone = args
    contacts[name] = phone
    return "Contact changed."

def all(contacts):
    return "\n".join([f"Name: {name}, phone: {phone}" for name, phone in contacts.items()])

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(contacts, args))
        elif command == "change":
            print(change_contact(contacts, args))
        elif command == "phone":
            print(get_phone(contacts, args))
        elif command == "all":
            print(all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()