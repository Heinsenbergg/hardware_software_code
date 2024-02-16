#Eric Lopez
def execute_display(menu_dict, title):
    print(title)
    for items, values in menu_dict.items():
        print("{}. {}".format(items, values.capitalize()))
    menu_selection = list(menu_dict.keys())
    selection = "none"

    while selection not in menu_selection:
        selection = input("Enter: ")
        if selection not in menu_selection:
            print("Invalid entry!")

    return selection, menu_dict[selection]

def menu_display():
    menu_dict = {
        '1': 'decimal to binary',
        '2': 'binary to decimal',
        'x': 'exit program'
    }
    return menu_dict

def decimal_to_binary(number):
    result = ""
    number = int(number)
    while number > 0:
        remainder = number % 2
        number = number // 2
        result = str(remainder) + result
    return result

def decimal():
    num = input("Enter Decimal Number:")
    print("Decimal {} to Binary: {}".format(num, decimal_to_binary(num)))

def binary_to_decimal(number):
    result = 0
    if len(number) > 0:
        power = len(str(number)) - 1
        for num in str(number):
            result += int(num) * 2 ** power
            power -= 1
        return result

def bin():
    num = input("Enter Binary Number:")
    print("Binary to Decimal: {}".format(binary_to_decimal(num)))

def check_selection():
    # Function placeholder for future implementation
    pass

def main():
    title = "Conversion Calculator"

    while True:
        sel, choice = execute_display(menu_display(), title)
        if sel == '1':
            decimal()
        elif sel == '2':
            bin()
        elif sel == 'x':
            print("Exiting the program.")
            break
        else:
            print("Invalid selection.")
        input("Press Enter to continue")

if __name__ == "__main__":
    main()
