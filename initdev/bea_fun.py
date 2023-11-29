from codrone_edu.drone import *


def startup(my_trim=None):
    """Startup routine"""
    # create object
    myDrone = Drone()
    # pair
    myDrone.pair()
    print("Paired", end=", ")

    # trim settings
    # get current trim
    if my_trim is None:
        trim = myDrone.get_trim()
    else:
        # set trim (eg: drone is drifting right, so trim to roll left a little bit, (-5, 0))
        myDrone.set_trim(my_trim[0], my_trim[1])
        # time to set the trim before takeoff
        time.sleep(1)
        trim = myDrone.get_trim()
    print("trim: %s" % str(trim))

    # takeoff
    myDrone.takeoff()
    print('In flight')
    myDrone.hover(2)

    return myDrone


def shut_down(drone):
    drone.land()
    drone.close()
    return


def rise_until(drone, height: float):
    # activate throttle until desired height

    print('Desired height: %.2f m' % height)
    # acceptable error threshold (cm)
    th = 0.01

    # bad measurement (room ceiling)
    outlier = 3.000

    # moving time
    dt = 1
    # power
    pwr = 30

    while True:
        # read height
        h = drone.get_bottom_range(unit="m")
        print('Measured height: %s' % str(h), end=" ")

        # ignore bad measurements, skip to next iteration
        if h > outlier or h < 0:
            drone.hover(0.5)
            continue

        # get error
        er = height - h
        print(", error: %.3f " % er, end= "")
        # if above threshold
        if abs(er) > th:
            if er > 0:
                # needs to go higher
                direction = 1
                print("going up ", end="")
            else:
                # come down
                direction = -1
                print("going down ", end="")

            k = pwr
            u = round(k * direction)

            print("command u = %.3f" %u)
            drone.set_throttle(u)
            drone.move(dt)
        else:
            break

    print("Achieved desired height, %s" % str(drone.get_bottom_range()))
    return drone
