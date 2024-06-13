from codrone_edu.drone import *
drone = Drone()
drone.pair()

distance = 50

if drone.detect_wall(distance):
    print("Takeoff area is not clear. Shutting down")
else:
    drone.takeoff()
    while True:
        drone.set_pitch(30)
        drone.move(0.2)
        if drone.detect_wall(distance):
            print("Object detected")
            break
    print("Obstacle detected.. Landing!")
    drone.land()
drone.close()