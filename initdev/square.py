from codrone_edu.drone import *
import bea_fun as bf

# times for moving and hovering
dtm = 1
dth = 2
pwr = 30
# (roll, pitch) drifting forward and right
my_trim = [-5, -5]

drone = bf.startup()
# ----------------------------------------------
# draw a square

# move forward
drone.set_pitch(pwr)  # setting forward pitch
drone.move(dtm)  # moving forward!
print('Moved forward')
# reset angles
drone.hover(dth)

# move right
# drone.set_pitch(0)  # resetting pitch to 0, uncomment if not hovering
drone.set_roll(pwr)  # setting roll to the right
drone.move(dtm)  # moving right!
print('Moved right')
drone.hover(dth)

# move backwards
# drone.set_roll(0)  # resetting roll to 0, uncomment if not hovering
drone.set_pitch(-pwr)  # setting backwards pitch
drone.move(dtm)  # moving backwards!
print('Moved backwards')
drone.hover(dth)

# move left
# drone.set_pitch(0)  # resetting pitch to 0, uncomment if not hovering
drone.set_roll(-pwr)  # setting roll to the left
drone.move(dtm)  # moving left!
print('Moved left')
drone.hover(dth)

# land
drone.land()

# close connection
drone.close()
