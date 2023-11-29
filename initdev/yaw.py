
import bea_fun as bf

# power
pwr = 25
dtm = 1
dth = 2

drone = bf.startup()

# set yaw power
drone.set_yaw(pwr)
drone.move(dtm)
# pause
drone.hover(dth)

# set throttle
drone.set_throttle(pwr)
drone.move(dtm)


# end
drone.land()
drone.close()