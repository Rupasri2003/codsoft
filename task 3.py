import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Password Generator")
    password_length = int(input("Enter the desired length of the password: "))
    
    if password_length <= 0:
        print("Invalid password length. Please enter a positive integer.")
    else:
        generated_password = generate_password(password_length)
        print("Generated Password:", generated_password)

if __name__== '__main__':
    main()
