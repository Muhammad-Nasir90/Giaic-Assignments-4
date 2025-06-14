def print_multiple(message: str, repeats: int):
    for i in range(repeats):
        print(message, end=' ')  # Print with space instead of newline
    print()  # Add a newline at the end

def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()