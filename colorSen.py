from codrone_edu.drone import *

drone = Drone()
drone.pair()

def drone_change_color():
    color = drone.get_back_color()
    if color == "Blue":
        drone.set_drone_LED(0, 0, 255, 100)  # Change to blue
    elif color == "Red":
        drone.set_drone_LED(255, 0, 0, 100)  # Change to red
    elif color == "Green":
        drone.set_drone_LED(0, 255, 0, 100)  # Change to green
    elif color == "Yellow":
        drone.set_drone_LED(255, 255, 0, 100)  # Change to yellow
    elif color == "Purple":
        drone.set_drone_LED(255, 0, 255, 100)  # Change to purple
    elif color == "Cyan":
        drone.set_drone_LED(0, 255, 255, 100)  # Change to cyan
    elif color == "White":
        drone.set_drone_LED(255, 255, 255, 100)  # Change to white
    else:
        drone.set_drone_LED(0, 0, 0, 100)  # Turn off


while True:
    drone_change_color()

