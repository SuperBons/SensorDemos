from codrone_edu.drone import *


drone = Drone()
drone.pair()

print("Temperature is: ", drone.get_temperature(), "C")
print("Pressure is:", drone.get_pressure(), "Pascals (Pa)")
print("Battery is: ", drone.get_battery(), "%")
print("Angle is: ", drone.get_x_angle(), "degrees, ", drone.get_y_angle(), "degrees,", drone.get_z_angle(), "degrees")


drone.close()
