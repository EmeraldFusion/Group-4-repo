from pyfirmata import Arduino, SERVO
from time import sleep

# speed here works like in arduino
# 180 = full speed ahead
# 0 = full speed reverse
# 90 = stopped
# values between 90 and 0 are slower reverse
# values between 90 and 180 are slower forward

# port might need to be edited by each person who runs this, unavoidable
port = 'COM4'                           # the port you use to connect to Arduino
pin = 10                                # like a GPIO pin, but on arduino
board = Arduino(port)                   # sets up the arduino board with your port

board.digital[pin].mode = SERVO         # sets the arduino pin to accept Servo input

def full_speed_front(pin):
    board.digital[pin].write(180)
    print('full ahead')
    sleep(2)

def full_speed_back(pin):
    board.digital[pin].write(0)
    print('full reverse')
    sleep(2)

def slower_front(pin):
    board.digital[pin].write(135)
    print('half speed forward')
    sleep(2)

def slower_back(pin):
    board.digital[pin].write(45)
    print('half speed reverse')
    sleep(2)

def stop(pin):
    board.digital[pin].write(90)
    print('stopped')
    sleep(2)

### MAIN ###

while True:  
    full_speed_front(pin)
    full_speed_back(pin)
    stop(pin)
    slower_front(pin)
    slower_back(pin)
    stop(pin)









    
