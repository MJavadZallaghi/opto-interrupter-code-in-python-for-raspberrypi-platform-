# coed by M. Javad Zallaghi
# email: MohammadJavadZallaghi@Gmail.com

import RPi.GPIO as GPIO

OISignalPin = 11 # opto interrupter signal
GreenPin = 12 # green led pin number
RedPin = 13 # Red led pin number

# define setup function :)

def setup():
    GPIO.setmode(GPIO.BOARD) # Numbers GPIO pins by physical location
    GPIO.setup(GreenPin, GPIO.OUT) # Set Green led pin mode to output
    GPIO.setup(RedPin, GPIO.OUT)   # """ Red   """ """ """" "" """"""
    GPIO.setup(OISignalPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.add_event_detect(OISignalPin, GPIO.BOTH, callback = detect, bouncetime = 200)
    

# define led function for turning on or off both led

def led(x):
    if x == 0:
        GPIO.output(RedPin, 1)
        GPIO.output(GreenPin, 0)
    if x == 1:
        GPIO.output(RedPin, 0)
        GPIO.output(GreenPin, 1)
        
# function that is attached to interrupt pin

def detect(chn):
    led(GPIO.input(OISignalPin))
    

def loop():
    while True:
        pass
    
def destroy():
    GPIO.output(GreenPin, GPIO.HIGH)
    GPIO.output(RedPin, GPIO.HIGH)
    GPIO.cleanup()
    
if __name__ == '__main__' :
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
    

