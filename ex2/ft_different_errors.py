def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        try:
            number = "abce"
            value = int(number)
            print(value)
            print("Operation completed succesfully\n")
        except ValueError as e:
            print(f"caught ValueError: {e}\n")

    elif operation_number == 1:
        try:
            num = 42
            num = num / 0
            print("Operation completed succesfully\n")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivitionError: {e}\n")

    elif operation_number == 2:
        try:
            file = "file_not_exist.txt"
            open(file)
            print("Operation completed succesfully\n")
        except FileNotFoundError as e:
            print(f"caught FileNotFoundError: {e}\n")

    elif operation_number == 3:
        try:
            a = 3
            b = "4"
            print(a - b)
            print("Operation completed succesfully\n")
        except TypeError as e:
            print(f"caught TypeError: {e}\n")

    elif operation_number == 4:
        try:
            int("1234")
            print("Operation completed succesfully\n")
        except ValueError as e:
            print(f"caught ValueError: {e}\n")


def test_error_types():
    print("=== Garden error Types Demo ===\n")
    for i in range(5):
        print(f"Testing operation {i}")
        garden_operations(i)
    print("All error type tested successfully!")


if __name__ == "__main__":
    test_error_types()
