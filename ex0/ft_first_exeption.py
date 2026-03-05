def check_temperature(temp_str):
    print(f"Testung temperatur: {temp_str}")
    try:
        temp: int = int(temp_str)
        if (temp > 40):
            print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
        elif (temp < 0):
            print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
        else:
            print(f"Temperature {temp}°C is perfect for plants!\n")

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")


def test_temperatur_input():
    print("=== Garden Temperature Checker ===\n")
    check_temperature("25")
    check_temperature("falaffel")
    check_temperature("100")
    check_temperature("-50")
    print("All test completed - program didn't crash!")


if __name__ == "__main__":
    test_temperatur_input()
