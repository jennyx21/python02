def gerden_operations():
    number = "abce"
    num = 42
    file = "file_not_exist.txt"
    key = "not_a_key"

    try:
        print("Testing ValueError...")
        value = int(number)
        print(value)
    except ValueError:
        print("caught ValueError: invalid literal for int()")

    try:
        print("Testing ZeroDivisionError...")
        num = num / 0
    except ZeroDivisionError:

        print("Caught ZeroDivitionError: division by zero")

    try:
        print("Testing FileNotFoundError...")
        f = open(file)
        print(f)
        f.close()
    except FileNotFoundError:
        print("caught FileNotFoundError: No such file 'file_not_exist.txt'")

