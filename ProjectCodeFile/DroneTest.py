# the module used for this code can be found here.
'https://pypi.org/project/pyFirmata/'

# Or you can open a command prompt to use pip and type in:
'pip install pyfirmata'

# You also need to download and/or have the official Arduino IDE found here.
# Follow the directions and download the proper IDE for your system.
'https://www.arduino.cc/en/Guide'

from pyfirmata import Arduino, SERVO, util
from time import sleep, time

# developer debug on/off
DEBUG = True

# name of the port being used to connect to the arduino board
#==========##### IMPORTANT NOTE #####==========#
# The name of the port will vary from device to device.
# Port (probably) needs to be manually updated each time is used because of this
# or no connection to the arduino board will be made.
# This code relies on Arduino, so the wrong/no port means this code won't work.
port = 'COM4'

# the number of each arduino pin being used for the wheels
RightWheels = 2
LeftWheels = 13


# sets "board" as the arduino board connected to the port being used so we can
# use arduino commands
board = Arduino(port)

# the pins for the wheels will take servo commands
board.digital[RightWheels].mode = SERVO
board.digital[LeftWheels].mode = SERVO

# detects infrared input from digital pins
INF1 = board.get_pin('d:4:i')
'''
INF2 = board.get_pin('d:5:i')
INF3 = board.get_pin('d:6:i')
INF4 = board.get_pin('d:7:i')
'''
it = util.Iterator(board)
it.start()




def forward(Rwheel=RightWheels, Lwheel=LeftWheels):
    board.digital[Rwheel].write(45)
    board.digital[Lwheel].write(135)
    sleep(.02)

def reverse(Rwheel=RightWheels, Lwheel=LeftWheels):
    board.digital[Rwheel].write(135)
    board.digital[Lwheel].write(45)
    sleep(.02)

def stop(Rwheel=RightWheels, Lwheel=LeftWheels):
    board.digital[Rwheel].write(90)
    board.digital[Lwheel].write(90)
    sleep(.02)

def turn_left(Rwheel=RightWheels, Lwheel=LeftWheels):
    pass

def turn_right(Rwheel=RightWheels, Lwheel=LeftWheels):
    pass


# detects infrared sensor input
def inf_sense():
    value = INF1.read()
    sleep(.1)
    if DEBUG:
        print(value)
    return float(value)


def main():
    stop()
    go = 0
    while go < 150:
        sense = inf_sense()
        if sense < .5:
            stop()
        else:
            forward()
        go+=1

    stop()



if __name__ == '__main__':
    main()
