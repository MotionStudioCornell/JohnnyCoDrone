from codrone_edu.drone import *

# create object
drone = Drone()
print("Drone object created")

# pair
drone.pair()
print("Paired!")

# close connection
drone.close()
