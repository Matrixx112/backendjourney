# Dictionary to store user data
user_data = {}

# Function to register a user
def register():
    username = input("Enter a username: ")
    if username in user_data:
        print("Username already exists. Try a different one.")
        return
    password = input("Enter a password: ")
    user_data[username] = password
    print(f"User '{username}' registered successfully!")

# Function to log in
def login():
    if not user_data:
        print("No users registered. Please register first.")
        return
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if user_data.get(username) == password:
        print(f"Welcome, {username}! You are now logged in.")
        return username
    else:
        print("Invalid username or password. Please try again.")
        return None

# Function to log out
def logout(username):
    if username:
        print(f"Goodbye, {username}! You have successfully logged out.")
        return None
    else:
        print("No user is currently logged in.")

# Main program loop
def main():
    current_user = None
    while True:
        print("\nOptions: register, login, logout, quit")
        choice = input("Choose an option: ").lower()

        if choice == "register":
            register()
        elif choice == "login":
            if current_user:
                print(f"User '{current_user}' is already logged in.")
            else:
                current_user = login()
        elif choice == "logout":
            current_user = logout(current_user)
        elif choice == "quit":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

# Run the main program
main()
