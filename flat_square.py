# Imports
## Crazyradio Driver
import cflib.crtp

## High Level Commander
from cflib.positioning.position_hl_commander import PositionHlCommander

## Crazyflie Imports
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie

## Utilities
import time

# URI for crazyflie
URI = 'radio://0/80/2M/E7E7E7E7E7' # Change this to your Crazyflie URI

# Main Script
def main():

    # Init Radio Drivers (USB)
    cflib.crtp.init_drivers(enable_debug_driver=False)

    # Create Crazyflie Object
    cf = Crazyflie()

    # Create Synchronous Crazyflie Object
    scf = SyncCrazyflie(URI, cf=cf)

    # Connect to Crazyflie
    scf.open_link()

    # Create High Level Commander for Crazyflie
    commander = PositionHlCommander(scf)

    # =================== FLIGHT SEQUENCE ===================
    
    # Takeoff to 0.5 meters
    commander.take_off(height=0.5)
    
    # Point 1
    commander.go_to(x=0.5,y=0.5,z=0.5)
    time.sleep(1)
    # Point 2
    commander.go_to(x=-0.5,y=0.5,z=0.5)
    time.sleep(1)
    # Point 3
    commander.go_to(x=-0.5,y=-0.5,z=0.5)
    time.sleep(1)
    # Point 4
    commander.go_to(x=0.5,y=-0.5,z=0.5)
    time.sleep(1)
    # Point 1
    commander.go_to(x=0.5,y=0.5,z=0.5)
    time.sleep(1)
    
    # Return to Center
    commander.go_to(x=0.0,y=0.0,z=0.5)
    time.sleep(1)
    
    # Land
    commander.land()

    # =================== END FLIGHT SEQUENCE ===================

    # Close Link to Crazyflie
    scf.close_link()


# Only execute code if directly executed as a script.
if __name__ == '__main__':
    main()
