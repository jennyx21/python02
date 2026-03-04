def check_temperature(temp_str):
    try:
        temp: int = int(temp_str)
        if (temp > 40):
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        elif (temp < 0):
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")

    finally:
        print("All test completed - program didn't crash!")


def ft_first_exception():
    print("=== Garden Temperature Checker ===\n")
    temp_str = input("Testing temperature: ")
    check_temperature(temp_str)


if __name__ == "__main__":
    ft_first_exception()
