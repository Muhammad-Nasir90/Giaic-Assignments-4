MAX_LENGTH = 3  # Removed the unnecessary colon (int annotation is optional)

def shorten(lst):
    """Shortens the list to MAX_LENGTH by removing elements from the end."""
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()  # Remove and get the last element
        print(f"Removed: {last_elem}")

def get_lst():
    """
    Prompts the user to enter list elements until an empty input is given.
    Returns the constructed list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()
    print(f"Original list: {lst}")
    shorten(lst)
    print(f"Shortened list: {lst}")

if __name__ == '__main__':
    main()