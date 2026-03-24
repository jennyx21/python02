class GardenError(Exception):
    def __init__(self, message):
         super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message, plant):
        self.plant = plant
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message, water):
        self.water = water
        super().__init__(message)


def trigger_errors(water, plant):
    if plant not in ["rose", "tulp", "sunflower"]:
       raise PlantError(f"the plant {plant} is willting!", plant)
    if water < 10: 
        raise WaterError("not enough water in the tank!", water)


def ft_costum_error():
    print("=== Costum Garden Error Demo ===\n")
    test = [
        (11, "tomato"),
        (1, "rose"),
        (20, "rose")
    ]
    print("testing PlantError...")
    try: 
        trigger_errors(11, "tomato")
    except PlantError as e:
        print(f"{e}\n")
    print("testint WaterError...")
    try: 
        trigger_errors(7, "rose")
    except WaterError as e: 
        print(f"{e}\n")
    print("Testing catching all GerdenErrors...")
    for water, plant in test:
        try: 
            trigger_errors(water, plant)
        except GardenError as e: 
            print(f"Caught an Error: {e}")
    print("\n All costum error types work correcly!")


if __name__ == "__main__":
    ft_costum_error()