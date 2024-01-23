def conversion_calc(numbers):
    list = ["1","2","3","4","5","6","7","8",]
    while numbers in numbers:
        if numbers.upper() in list:
            return(True)
def converting():
    bin()#dec to bin
    int()#binary to dec

def main():
        print("This Program converts numbers! ")
        print("Choose The Following Conversation")
        print("(1) Binary to Decimal")
        print("(2) Decimal To Binary")
        print("(3) Binary to Hexadecimal")
        print("(4) Decimal to Hexadecimal")
        print("(5) Hexadecimal to Decimal")
        print("(6) Hexadecimal to Binary")
        print("(7) Octal to Decimal")
        print("(8) Decimal to Octal")
        good_selection = True
        while good_selection:
            selection = input("Enter Valid Selection:")
            good_selection = conversion_calc(selection)
                    =converting()

        #return input("Convert from __ to __")
        return input("Type (q) to Quit or Enter to Continue:")
        answer = input() . lower()
        if answer == "q":
            print()
#elif answer == ("Enter"):



if __name__ == "__main__":
    main()
#Eric Lopez
#The purpose of the program is to
