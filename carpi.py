import subprocess
from time import sleep
# Add gpio imports


locked = True # Current state of vehicle: doors locked (T) or doors unlocked (F)
absent_count = 0 # I may remove these two variables if they are not needed for reliability
ABSENT_COUNT_MAX = 1

while(True):
    # Device is in range, so car should be unlocked
    if inProximity():
        absent_count = 0
        if locked:
            unlock()
        sleep(30) # Sleep after device is in range so devices in proximity are not overwhelmed with requests
    # Device is out of range, so car should be locked after a bit
    else:
        if not locked and absent_count > ABSENT_COUNT_MAX:
            lock()
        else:
            absent_count += 1

    sleep(5) # Sleep for a little so devices just out of range aren't bombarded with requests


def inProximity():
    try:
        resp = subprocess.check_output("sudo hcitool cc 1C:5C:F2:AB:FA:78; sudo hcitool rssi 1C:5C:F2:AB:FA:78", shell=True)
        print(resp)
        rssi = int(resp.split(' ')[3])
        # In range
        if rssi > -10:
            return True
        # Out of range
        else:
            return False
    except:
        # Not found
        return False
    

def lock():
    #Add GPIO on/off calls here
    subprocess.call("sudo bash -c 'echo 0 >/sys/class/leds/led0/brightness'", shell= True)
    global locked
    locked = True
    print("Locking")


def unlock():
    #Add GPIO on/off calls here
    subprocess.call("sudo bash -c 'echo 1 >/sys/class/leds/led0/brightness'", shell= True)
    global locked
    locked = False
    print("Unlocking")