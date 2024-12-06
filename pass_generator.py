import string as str
import secrets
import random  # this is the module used to generate random numbers on your given range


class PasswordGenerator:
    @staticmethod
    def gen_sequence(
        conditions,
    ):  # must have  conditions (in a list format), for each member of the list possible_characters
        possible_characters = [
            str.ascii_lowercase,  # Lowercase letters
            str.ascii_uppercase,  # Uppercase letters
            str.digits,           # Digits
            str.punctuation,      # Punctuation characters
        ]
        sequence = ""
        for x in range(len(conditions)):
            if conditions[x]:  # Check if the condition for the character type is True
                sequence += possible_characters[x]  # Add the corresponding characters to the sequence
            else:
                pass  # If condition is False, do nothing
        return sequence  # Return the generated sequence of characters

    @staticmethod
    def gen_password(sequence, passlength=8):
        password = "".join((secrets.choice(sequence) for i in range(passlength)))  # Generate a random password
        return password  # Return the generated password


class Interface:
    has_characters = {
        "lowercase": True,  # Flag for including lowercase letters
        "uppercase": True,  # Flag for including uppercase letters
        "digits": True,     # Flag for including digits
        "punctuation": True, # Flag for including punctuation
    }

    @classmethod
    def change_has_characters(cls, change):
        try:
            cls.has_characters[change]  # Check if the specified key exists in the dictionary
        except Exception as err:
            print(f"Invalid \nan Exception: {err}")  # Print error if key does not exist
        else:
            cls.has_characters[change] = not cls.has_characters[change]  # Toggle the value of the specified key
            print(f"{change} is now set to {cls.has_characters[change]}")  # Print the new value

    @classmethod
    def show_has_characters(cls):
        print(cls.has_characters)  # Print the current character flags

    def generate_password(self, lenght):
        sequence = PasswordGenerator.gen_sequence(list(self.has_characters.values()))  # Generate character sequence based on flags
        print(f"Generated Passwaord: {PasswordGenerator.gen_password(sequence, lenght)}")  # Generate and print the password


def list_to_vertical_string(list):
    to_return = ""
    for member in list:
        to_return += f"{member}\n"  # Convert list items to a vertical string format
    return to_return  # Return the formatted string


class Run:
    def decide_operation(self):
        user_input = input(": ")  # Get user input
        try:
            int(user_input)  # Try to convert input to an integer
        except:
            Interface.change_has_characters(user_input)  # Change character flags if input is not an integer
        else:
            Interface().generate_password(int(user_input))  # Generate password if input is valid
        finally:
            print("\n\n")  # Print new lines for better readability

    def run(self):
        menu = f"""Welcome to the PassGen App!
Commands:
    generate password ->
    <lenght of the password>

commands to change the characters to be used to generate passwords:
{list_to_vertical_string(Interface.has_characters.keys())}  # Display available character options
            """
        print(menu)  # Print the menu
        while True:
            self.decide_operation()  # Continuously decide operation based on user input


Run().run()  # Start the application
