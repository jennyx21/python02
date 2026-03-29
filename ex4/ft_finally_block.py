class PlantError(Exception):
    def __init__(self, message, plant):
        self.plant = plant
        super().__init__(message)


def trigger_errors(plant):
    if plant != plant.capitalize():
        raise PlantError(f"invalid plant name to water: '{plant}'", {plant})


def water_plants(plant_name):
    print("Opening Warter systems")
    for plant in plant_name:
        trigger_errors(plant)
        print(f"watering {plant} [OK]")


def test_watering_sytem():
    print("Testing valid plants...")
    list = ["Tomato", "Lettuce", "Carrots"]
    list2 = ["Tomato", "lettuce"]
    try:
        water_plants(list)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print("Closing watering sytstem\n")

    print("Testing invalid plants...")
    try:
        water_plants(list2)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print("Closing watering sytstem\n")
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_sytem()
