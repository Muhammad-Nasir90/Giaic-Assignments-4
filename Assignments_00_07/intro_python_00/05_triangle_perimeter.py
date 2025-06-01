def main():


    side1 = float(input("\033[1;3m Enter the length of the side 1:\033[0m"))
    side2 = float(input("\033[1;3mEnter the length of the side 2:\033[0m"))
    side3 = float(input("\033[1;3mEnter the length of the side 3:\033[0m"))

    permiter = side1 + side2 + side3


    print(f"The Perimeter of the triangle is : {permiter}")

if __name__== "__main__":
    main()