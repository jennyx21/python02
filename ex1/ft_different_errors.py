def garden_operations():
    number = "abce"
    num = 42
    file = "file_not_exist.txt"
    keyplants = {"rose": "red"}

    try:
        print("Testing ValueError...")
        value = int(number)
        print(value)
    except ValueError:
        print("caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        num = num / 0
    except ZeroDivisionError:

        print("Caught ZeroDivitionError: division by zero\n")

    try:
        print("Testing FileNotFoundError...")
        f = open(file)
        print(f)
    except FileNotFoundError:
        print("caught FileNotFoundError: mo such file file_not_exist.txt\n")

    try:
        print("Testing KeyError...")
        print(keyplants["missing_plant"])
    except KeyError as e:
        print(f"caught KeyError:{e}\n")
    print("Testing multiple errors together")
    try:
        int("abc")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")


def test_error_types():
    print("=== Garden error Types Demo ===\n")
    garden_operations()
    print("all error type tested successfully!")


if __name__ == "__main__":
    test_error_types()
