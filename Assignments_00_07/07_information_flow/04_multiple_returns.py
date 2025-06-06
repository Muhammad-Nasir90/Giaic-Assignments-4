def get_user_data():
    """
    Collects user registration data and returns it as a tuple.
    Returns:
        tuple: (first_name, last_name, email_address)
    """
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email_address = input("What is your email address?: ")
    return first_name, last_name, email_address

def main():
    print("User Registration System")
    user_data = get_user_data()
    print("\nReceived the following user data:", user_data)

if __name__ == "__main__":
    main()