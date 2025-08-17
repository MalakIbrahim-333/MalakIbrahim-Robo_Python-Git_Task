# Raspberry pi setup
import RPi.GPIO as GPIO
import keyboard
import time

# Motor control pins
# L=LEFT / R=Right / FOR=forward / BACK=backward
L_MOTOR_FOR = 17
L_MOTOR_BACK = 18
R_MOTOR_FOR = 19
R_MOTOR_BACK = 20

# Setting Pins mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(L_MOTOR_FOR, GPIO.OUT)
GPIO.setup(L_MOTOR_BACK, GPIO.OUT)
GPIO.setup(R_MOTOR_FOR, GPIO.OUT)
GPIO.setup(R_MOTOR_BACK, GPIO.OUT)


def stop_motors():
    GPIO.output(L_MOTOR_FOR, False)
    GPIO.output(L_MOTOR_BACK, False)
    GPIO.output(R_MOTOR_FOR, False)
    GPIO.output(R_MOTOR_BACK, False)


def move_forward():
    GPIO.output(L_MOTOR_FOR, True)
    GPIO.output(L_MOTOR_BACK, False)
    GPIO.output(R_MOTOR_FOR, True)
    GPIO.output(R_MOTOR_BACK, False)


def move_backward():
    GPIO.output(L_MOTOR_FOR, False)
    GPIO.output(L_MOTOR_BACK, True)
    GPIO.output(R_MOTOR_FOR, False)
    GPIO.output(R_MOTOR_BACK, True)


def turn_left():
    GPIO.output(L_MOTOR_FOR, False)
    GPIO.output(L_MOTOR_BACK, True)
    GPIO.output(R_MOTOR_FOR, True)
    GPIO.output(R_MOTOR_BACK, False)


def turn_right():
    GPIO.output(L_MOTOR_FOR, True)
    GPIO.output(L_MOTOR_BACK, False)
    GPIO.output(R_MOTOR_FOR, False)
    GPIO.output(R_MOTOR_BACK, True)


def main():
    print("Rover Control is Intiated")
    print("W=Forward | S=Backward | A=Left | D=Right | Q=Stop")

    try:
        while True:
            if keyboard.is_pressed('w'):
                move_forward()
            elif keyboard.is_pressed('s'):
                move_backward()
            elif keyboard.is_pressed('a'):
                turn_left()
            elif keyboard.is_pressed('d'):
                turn_right()
            elif keyboard.is_pressed('q'):
                print("Stopped...")
                break
            else:
                stop_motors()

            time.sleep(0.1)

        UserExit = KeyboardInterrupt

    except UserExit:
        pass
    finally:
        stop_motors()
        GPIO.cleanup()


if __name__ == "__main__":
    main()
