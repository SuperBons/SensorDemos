from codrone_edu.drone import *
import time
drone = Drone()
drone.pair()
drone.takeoff()

time_elapsed = 0
time_start = time.time()

while time_elapsed < 30:
    time_elapsed = time.time() - time_start
    front_sensor = drone.get_front_range()
    print("front_sensor", front_sensor)

    if front_sensor > 150:
        print("Moving forward!")
        drone.set_yaw(0)
        drone.set_pitch(30)
        drone.move()
        time.sleep(2)
    elif 70 > front_sensor > 50:
        print("Something is getting close.. Slowing down!")
        drone.set_yaw(0)
        drone.set_pitch(20)
        drone.move()
        time.sleep(2)
    else:
        print("Object detected! Turning!")
        drone.set_pitch(0)
        drone.turn_right(180)
        drone.move_forward(distance=2, units="m", speed=1)
        time.sleep(6)
        drone.set_throttle(50)
        drone.move(1.5)
        drone.hover(5)
        drone.flip("back")
        drone.land()

drone.close()