#Eric Lopez
#This is a conversion calculator and it converts Decimal to Binary and Binary to Decimal
def execute_display(menu_dict, title):
    #shows title and options
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
    #menu options for user
    menu_dict = {
        '1': 'decimal to binary',
        '2': 'binary to decimal',
        'x': 'exit program'
    }
    return menu_dict
#converts decimal to binary
def decimal_to_binary(number):
    result = ""
    number = int(number)
    while number > 0:
        remainder = number % 2
        number = number // 2
        result = str(remainder) + result
    return result

def decimal():
    #takes decimal and tuns into binary
    num = input("Enter Decimal Number:")
    print("Decimal {} to Binary: {}".format(num, decimal_to_binary(num)))

def binary_to_decimal(number):
    #converts binary number to decimal
    result = 0
    if len(number) > 0:
        power = len(str(number)) - 1
        for num in str(number):
            result += int(num) * 2 ** power
            power -= 1
        return result

def bin():#takes binary input and turns into decimal
    num = input("Enter Binary Number:")
    print("Binary to Decimal: {}".format(binary_to_decimal(num)))

def check_selection():

    pass

def main():
    #start of code
    title = "Conversion Calculator"

    while True:#shows the menu and gets input
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
        input("Press Enter to continue")# allows person to redo code again 

if __name__ == "__main__":
    main()
