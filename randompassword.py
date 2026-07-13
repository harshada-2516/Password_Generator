import random
import string

# Ask the user for the password length
while True:
    try:
        pass_len = int(input("Enter the password length: "))
        
        if pass_len <= 0:
            print("Password length must be greater than 0. Please try again.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

# Characters to use in the password
charvalue = string.ascii_letters + string.digits + string.punctuation

# Generate the password
password = ""

for i in range(pass_len):
    password += random.choice(charvalue)

# Display the password
print("\nYour random password is:", password)
