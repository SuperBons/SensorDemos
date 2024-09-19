from codrone_edu.drone import *

import time

drone = Drone()

drone.pair()


pressure_1 = drone.get_pressure() # ground level


drone.takeoff()

pressure_2 = drone.get_pressure() # after takeoff level 1


drone.set_throttle(30)

drone.move(1)

pressure_3 = drone.get_pressure() # level 2


drone.move(1)

pressure_4 = drone.get_pressure() # level 3


drone.land()


print("On the Ground: ", pressure_1, "Pascals (Pa)")

print("Level 1: ", pressure_2, "Pascals (Pa)")

print("Level 2: ", pressure_3, "Pascals (Pa)")

print("Level 3: ", pressure_4, "Pascals (Pa)")

print("Difference between ground and level 3: ", pressure_1 - pressure_4, "Pascals (Pa)")