def get_smallest(smallest, value):
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    return smallest

def main():
    smallest = None
    while True:
        num = input("Enter a number: ").lower()
        if num == "done":
            break
        smallest = get_smallest(smallest, int(num))
        print("Smallest number is:", smallest)
        print(smallest , "is smaller than" , num)

if __name__ == "__main__":
    main()
