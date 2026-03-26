# calculator.py
def add(a, b):
    return a + b


def subtract(a, b):
    pass

def multiply(a, b):
    return a * b

def divide(a, b):
    pass

def main():
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
    elif op == "-":
        result = subtract(a, b)
    elif op == "*":
        result = multiply(a, b)
    elif op == "/":
        result = divide(a, b)
    else:
        print("Invalid operator.")
        return

    print(f"Result: {result}")


if __name__ == "__main__":
    main()