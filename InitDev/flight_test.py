from codrone_edu.drone import *
import time

# create object
drone = Drone()

# pair
drone.pair()
print("Paired")

# trim settings
# get current trim
print(drone.get_trim())
# set trim (eg: drone is drifting right, so trim to roll left a little bit, (-5, 0))
drone.set_trim(0, 0)

# time to set the trim before takeoff
time.sleep(1)

# take off
drone.takeoff()
print('In the air!')

# hover for 3 sec
drone.hover(3)

# land
print("Landing...")
drone.land()

# close connection
drone.close()