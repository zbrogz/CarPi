import subprocess
from time import sleep

# Add led setup

while(True):
    try:
        resp = subprocess.check_output("sudo hcitool cc 1C:5C:F2:AB:FA:78; sudo hcitool rssi 1C:5C:F2:AB:FA:78", shell=True)
        print(resp)
        rssi = int(resp.split(' ')[3])
        print(rssi)
        if rssi > -10:
            subprocess.call("sudo bash -c 'echo 1 >/sys/class/leds/led0/brightness'", shell= True)
            #add delay
        else:
            subprocess.call("sudo bash -c 'echo 0 >/sys/class/leds/led0/brightness'", shell= True)
    except:
        print("Device not in range")
        subprocess.call("sudo bash -c 'echo 0 >/sys/class/leds/led0/brightness'", shell= True)
    sleep(5)
