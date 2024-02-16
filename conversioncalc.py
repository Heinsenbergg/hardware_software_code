def bin_to_dec(binary):
    return int(binary, 2)

def dec_to_bin(decimal):
    return bin(decimal)[2:]

def convert_number(number, from_base, to_base):
    if from_base == 1:
        decimal = bin_to_dec(number)
    else:
        decimal = int(number)

    if to_base == 1:
        result = dec_to_bin(decimal)
    else:
        result = str(decimal)

    return result

def main():
    print("Number systems")
    print("1. binary")
    print("2. decimal")

    valid_choices = {1, 2}

    from_base = int(input("Enter number system of choice: "))
    if from_base not in valid_choices:
        print('Invalid number system choice')
        return

    number = input("Enter a Number: ")

    print("Select number system to convert to:")
    print("1. binary")
    print("2. decimal")

    to_base = int(input("Enter Number: "))
    if to_base not in valid_choices:
        print('Invalid number system choice')
        return

    result = convert_number(number, from_base, to_base)

    print(f"result: {result}")

    while True:
        choice = input("\nContinue with another number Y or N : ")
        if choice.lower() == "y":
            main()
        elif choice.lower() == "n":
            break
        else:
            print('Invalid choice. Please enter Y or N.')

if __name__ == "__main__":
    main()

def bin_to_dec(binary):
    return int(binary, 2)

def dec_to_bin(decimal):
    return bin(decimal)[2:]

def convert_number(number, from_base, to_base):
    if from_base == 1 and not all(bit in '01' for bit in number):
        print("Error: Invalid binary input.")
        return None
    elif not number.isdigit():
        print("Error: Invalid decimal input.")
        return None

    if from_base == 1:
        decimal = bin_to_dec(number)
    else:
        decimal = int(number)

    if to_base == 1:
        result = dec_to_bin(decimal)
    else:
        result = str(decimal)

    return result

def main():
    print("Number systems")
    print("1. binary")
    print("2. decimal")

    valid_choices = {1, 2}

    from_base_str = input("Enter number system of choice: ")
    if not from_base_str.isdigit():
        print('Invalid number system choice')
        return
    from_base = int(from_base_str)
    if from_base not in valid_choices:
        print('Invalid number system choice')
        return

    number = input("Enter a Number: ")
    if from_base == 1 and not all(bit in '01' for bit in number):
        print('Invalid binary input')
        return
    elif not number.isdigit():
        print('Invalid decimal input')
        return

    to_base_str = input("Enter Number: ")
    if not to_base_str.isdigit():
        print('Invalid number system choice')
        return
    to_base = int(to_base_str)
    if to_base not in valid_choices:
        print('Invalid number system choice')
        return

    result = convert_number(number, from_base, to_base)

    if result is not None:
        print(f"Result: {result}")

    while True:
        choice = input("\nContinue with another number Y or N : ")
        if choice.lower() == "y":
            main()
        elif choice.lower() == "n":
            break
        else:
            print('Invalid choice. Please enter Y or N.')

if __name__ == "__main__":
    main()
