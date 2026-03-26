def add(a, b):
    return a + b


def main():

    result = 0 
    print("=== Calculator ===")
    print("Operator: +, -, *, /")

    try:
        a = int(input("Enter first integer: "))
        b = int(input("Enter second integer: "))
        op = input("Enter operator (+, -, *, /): ").strip()
    except ValueError:
        print("Invalid input.")
        return
    

    if op == "+":
        result = add(a, b)


    print(f"Result: {result}")


if __name__ == "__main__":
    main()