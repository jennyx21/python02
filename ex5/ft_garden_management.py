class GardenManager():
    def __init__(self):
        self.plants = []

    def add_plants(self, plant):
        self.plants.append(plant)
        print(f"Added {plant} successfully")

class PlantError(Exception):
    def __init__(self, message, plant):
        self.plant = plant
        super().__init__(message)

class WaterError(Exception):
    def __init__(self, message, water):
        self.water = water
        super().__init__(message)

def trigger_errors(plant):
    if plant not in ["rose", "sunflower", "tomato", "lettuce", "carrots"]:
       raise PlantError(f"Error: Cannot water {plant} - invalid plant!", plant)


def water_plants(plant_list):
    print("Opening Warter systems")
 
    try: 
        for plant in plant_list:
            trigger_errors(plant)
            print(f"watering {plant}")
    except PlantError as e:
        print(f"{e}")
    finally:
        print("Closing watering sytstem (cleanup)")




def test_watering_sytem():
    print("Testing normal Watering...")
    list = ["tomato", "lettuce", "carrots"]
    list2 = ["tomato", "none"]
    water_plants(list)
    print("Watering completed successfully!\n")
    water_plants(list2)
    print("\nCleanup always happens, even with errors!")


def trigger_errors(water, plant):
    if plant not in ["rose", "tulp", "sunflower"]:
       raise PlantError(f"the plant {plant} is willting!", plant)
    if water < 10: 
        raise WaterError("not enough water in the tank!", water)


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