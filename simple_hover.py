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
URI = 'radio://0/30/2M/E7E7E7E7E7' # Change this to your Crazyflie URI

# Main Script
def main():

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
    
    # Wait for 5 seconds
    time.sleep(5)
    
    # Land
    commander.land()
    
    # =================== END FLIGHT SEQUENCE ===================

    # Close Link to Crazyflie
    scf.close_link()


# Only execute code if directly executed as a script.
if __name__ == '__main__':
    main()
