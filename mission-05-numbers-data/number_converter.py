
# MISSION 5 - NUMBERS AND DATA
# Python Number Converter

print("================================")
print("       NUMBER CONVERTER")
print("================================")

while True:
    print("\nChoose an option:")
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    print("4. Binary to Decimal")
    print("5. Octal to Decimal")
    print("6. Hexadecimal to Decimal")
    print("7. Character to ASCII")
    print("8. ASCII to Character")
    print("9. Exit")

    choice = input("\nEnter your choice: ")

    try:
        if choice == "1":
            num = int(input("Enter decimal number: "))
            print("Binary:", bin(num)[2:])

        elif choice == "2":
            num = int(input("Enter decimal number: "))
            print("Octal:", oct(num)[2:])

        elif choice == "3":
            num = int(input("Enter decimal number: "))
            print("Hexadecimal:", hex(num)[2:].upper())

        elif choice == "4":
            num = input("Enter binary number: ")
            print("Decimal:", int(num, 2))

        elif choice == "5":
            num = input("Enter octal number: ")
            print("Decimal:", int(num, 8))

        elif choice == "6":
            num = input("Enter hexadecimal number: ")
            print("Decimal:", int(num, 16))

        elif choice == "7":
            char = input("Enter one character: ")
            if len(char) == 1 and ord(char) <= 127:
                print("ASCII value:", ord(char))
            else:
                print("Enter one ASCII character only.")

        elif choice == "8":
            num = int(input("Enter ASCII value (0-127): "))
            if 0 <= num <= 127:
                print("Character:", chr(num))
            else:
                print("Enter a value between 0 and 127.")

        elif choice == "9":
            print("Thank you for using Number Converter!")
            break

        else:
            print("Invalid choice. Try again.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

PY
