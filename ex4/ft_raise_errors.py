def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name == " ":
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Error: water level {water_level} is too low (min 1)")
    if water_level > 10: 
        raise ValueError(f"Error: water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Error: Sun")
    else: 
        print(f"plant '{plant_name}' is healthy!")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")
    print("testing good values...")
    try:
        check_plant_health("tomato", 8, 8)
    except ValueError as e:
        print(f"{e}")
    print("\ntesting empty plant name..")
    try:
        check_plant_health(" ", 8, 8)
    except ValueError as e:
        print(f"{e}")
    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 8)
    except ValueError as e:
        print(f"{e}")
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 8, 0)
    except ValueError as e:
        print(f"{e}")
    print("\nAl error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()