
from codrone_edu.drone import *
import bea_fun as bf

# times for moving and hovering
# dtm = 1
# dth = 2
# pwr = 30

# takeoff
drone = bf.startup()

# in m
hbar = 1.5
drone = bf.rise_until(drone, hbar)

drone.hover(2)
bf.shut_down(drone)