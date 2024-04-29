import random
import string

def generate_password(length):
    # Define characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        # Prompt the user for the desired length of the password
        length = int(input("Enter the desired length of the password: "))
        
        if length <= 0:
            print("Length should be a positive integer.")
            return

        # Generate the password
        password = generate_password(length)

        # Display the generated password
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
