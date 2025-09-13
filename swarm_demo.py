# Imports
import cflib.crtp
from cflib.crazyflie.swarm import CachedCfFactory,Swarm
from cflib.positioning.position_hl_commander import PositionHlCommander
import asyncio
import time

# List of URIs for the Crazyflies
URI_LIST = [
    'radio://0/40/2M/E7E7E7E7E7',  # First Crazyflie URI
    'radio://0/80/2M/E7E7E7E7E7'   # Second Crazyflie URI
]

def run_sequence(scf):
    radio_address = scf.cf.link_uri
    print(f"{radio_address}")
    drone_id = URI_LIST.index(radio_address)
    print(f"Drone ID: {drone_id}")
    """Defines the flight sequence for each Crazyflie."""
    with PositionHlCommander(scf) as commander:
        # Take off to 0.5 meters
        
        # commander.take_off(height=0.5)

        if drone_id == 1:
            commander.go_to(x=1.0,y=1.0,z=1.0)
        else:
            commander.go_to(x=-1.0,y=-1.0,z=1.0)
        
        # commander.land()
        






def main():
    # Initialize drivers
    cflib.crtp.init_drivers(enable_debug_driver=False)
    factory = CachedCfFactory(rw_cache='./cache')
    # Create and run the swarm
    with Swarm(URI_LIST, factory=factory) as swarm:
        swarm.parallel(run_sequence)
        time.sleep(5)



if __name__== '__main__':
    main()
