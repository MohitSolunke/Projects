import time
import RPi.GPIO as GPIO

RUNNING = True

HIGH = 1
LOW = 0
PIRpin = 4
DOORpin = 21
LIGHT1pin = 23
LIGHT2pin = 24
LIGHT3pin = 25
FAN1pin = 6
FAN2pin = 16
FAN3pin = 5
APPLLIANCE1pin = 27
APPLLIANCE2pin = 22

def initSystem():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIRpin,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(DOORpin,GPIO.OUT)
    GPIO.setup(LIGHT1pin,GPIO.OUT)
    GPIO.setup(LIGHT2pin,GPIO.OUT)
    GPIO.setup(LIGHT3pin,GPIO.OUT)
    GPIO.setup(FAN1pin,GPIO.OUT)
    GPIO.setup(FAN2pin,GPIO.OUT) 
    GPIO.setup(FAN3pin,GPIO.OUT)
    GPIO.setup(APPLLIANCE1pin,GPIO.OUT)
    GPIO.setup(APPLLIANCE2pin,GPIO.OUT)
    return

def detectPerson():
    input_state = GPIO.input(PIRpin)
    time.sleep(0.3)
    if input_state == HIGH:
        return True
    else:    
        return False
    
try :
    print ("\n\n  Home Automation Testing \n\n")
    print("-----------------------------------\n")
    initSystem()
    count =0
    count_flag =0
    door_flag =0
    elapsed =0
    while RUNNING:
        state = detectPerson()
        if state == HIGH:
            if count_flag ==1:
                count_flag =0
                count +=1
                print ("Person Detected\n")
        else:
            count_flag =1
            print("wait for next Person\n")

        if count == 0:
            GPIO.output(LIGHT1pin,0)
            GPIO.output(LIGHT2pin,0)
            GPIO.output(LIGHT3pin,0)
            GPIO.output(FAN1pin,0)
            GPIO.output(FAN2pin,0)
            GPIO.output(FAN3pin,0)
            GPIO.output(APPLLIANCE1pin,0)
            GPIO.output(APPLLIANCE2pin,0)
            GPIO.output(DOORpin,0)
            print("All Devices are OFF\n")

            door_flag = 1
        elif count == 1:
            if(door_flag == 1):
                door_flag = 0
                GPIO.output(DOORpin,1)
                time.sleep(1)
                GPIO.output(DOORpin,0)
        elif count == 2:
            GPIO.output(LIGHT1pin,1)
            GPIO.output(FAN1pin,1)
        elif count == 3:
            GPIO.output(LIGHT2pin,1)
            GPIO.output(FAN2pin,1)
        elif count == 4:
            GPIO.output(LIGHT3pin,1)
            GPIO.output(FAN3pin,1)
        else:
            GPIO.output(APPLLIANCE1pin,1)
            GPIO.output(APPLLIANCE2pin,1)
            time.sleep(5)
            count(0)
        elapsed = time.time()-start
        if elapsed > 120:
            print("Timeout Occured, Restart the Program\n")
            break
except KeyboardInterrupt:
    RUNNING = False
    print("Program Terminated\n")
finally:
    GPIO.cleanup()
    print("GPIO Cleaned\n")

            
                
        






