def execute_display(menu_dict):
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
        '1':'decimal_to_binary',
        '2':'binary_to_decimal',
        'x':'exit_program',

    }
    return menu_dict

def bin_to_dec(binary):
    return int(binary, 2)


def dec_to_bin(decimal):
    return bin(decimal)[2:]

def convert_number(number, from_base, to_base):
    if from_base == 1:
        decimal = bin_to_dec(number)
    elif from_base == 2:
        decimal = oct_to_dec(number)
    else:
        decimal = int(number)

    if to_base == 1:
        result = dec_to_bin(decimal)
    elif to_base == 2:
        result = dec_to_oct(decimal)

    else:
        result = str(decimal)

    return result

print("Enter number system:")
print("1. binary")
print("2. decimal")

from_base = int(input(": "))

number = input(": ")

print("Enter Number:")
print("1. binary")
print("2. decimal")


to_base = int(input("Enter Number: "))

result = convert_number(number, from_base, to_base)

print(f"result: {result}")


def decimal_to_binary(number):
    result = ""
    number = int(number)
    while number > 0:
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

def binary():
    num = input("Enter Binary Number:")
    print("Binary to Decimal: {}".format(binary_to_decimal(num)))


def main():
    sel, choice = execute_display(menu_display())
    print("You selected {} and want to convert {}".format(sel,choice))
    if choice == 1:
     decimal_to_binary(number)
    elif choice == 2:
     binary_to_decimal(number)
    else:
        print("Done converting!")


if __name__ == "__main__":
        main()
