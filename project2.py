def execute_display(menu_dict):
    for items, values in menu_dict.items():
        print("{}. {}".format(items, values.capitalize()))
    menu_selection = list(menu_dict.keys())
    selection = "#"

    while selection not in menu_selection:
        selection = input("Enter: ")
        if selection not in menu_selection:
            print("Invalid entry!")

    return selection, menu_dict[selection]

def menu_display():
    menu_dict = {
        '1':'decimal_to_binary',
        '2':'binary_to_decimal',
        'x':'exit_program'
    }
    return menu_dict

    if answer == "1":
        choice = decimal_to_binary
    elif answer == "2":
        choice = binary_to_decimal

def main():
    sel, choice = execute_display(menu_display())
    print("You selected {} and want to convert {}".format(sel,choice))

if __name__ == "__main__":
    main()


def decimal_to_binary(number):
    result = ""
    number = int(number)
    while number > 0:
        remainder = number % 2
        number = number // 2
        result = str(remainder) + result
    return result

def deci():
    num = input("Enter Decimal Number:")
    print("Decimal {} to Binary: {}".format(num, decimal_to_binary(num)))

if __name__ == "__main__":
    deci()

def binary_to_decimal(number):
    result = 0
    if len(number) > 0:
        power = len(str(number)) - 1
        for num in str(number):
            result += int(num) * 2 ** power
            power -= 1
        return result

def bina():
    num = input("Enter Binary Number:")
    print("Binary to Decimal: {}".format(binary_to_decimal(num)))

if __name__ == "__main__":
    bina()
