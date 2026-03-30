#!/usr/bin/env python3
def test_temperature(temp_str) -> None:
    print(f"input data is '{temp_str}'")
    try:
        temp: int = int(temp_str)
        if (temp > 40):
            raise Exception(f"{temp}°C is too hot for plants (max 40°C)")
        elif (temp < 0):
            raise Exception(f"{temp}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature is now {temp}°C\n")

    except Exception as e:
        print(f"caught input_temperature error: {e}\n")


def input_temperatur() -> None:
    print("=== Garden Temperature Checker ===\n")
    test_temperature("25")
    test_temperature("falaffel")
    test_temperature("100")
    test_temperature("-50")
    print("All test completed - program didn't crash!")


if __name__ == "__main__":
    input_temperatur()
