def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def _get_number(prompt):
    while True:
        s = input(prompt).strip()
        if s.lower() in ("q", "quit"):
            raise SystemExit
        try:
            return float(s)
        except ValueError:
            print("Invalid number. Type a valid number or 'q' to quit.")


def main():
    print("Simple Calculator — enter 'q' at any prompt to quit")
    ops = {
        "1": ("Addition", add),
        "2": ("Subtraction", subtract),
        "3": ("Multiplication", multiply),
        "4": ("Division", divide),
    }

    while True:
        print("\nSelect operation:")
        for k, v in ops.items():
            print(f" {k}. {v[0]}")
        print(" q. Quit")

        choice = input("Choose 1/2/3/4 or q: ").strip().lower()
        if choice in ("q", "quit"):
            print("Goodbye.")
            break
        if choice not in ops:
            print("Invalid choice — please select 1,2,3,4 or q.")
            continue

        try:
            a = _get_number("Enter first number: ")
            b = _get_number("Enter second number: ")
            func = ops[choice][1]
            result = func(a, b)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            continue
        except SystemExit:
            print("Goodbye.")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            continue

        print(f"Result: {result}")


if __name__ == "__main__":
    main()
