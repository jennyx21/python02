
class PlantError(Exception):
    def __init__(self, message, plant):
        self.plant = plant
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



if __name__ == "__main__":
    test_watering_sytem()