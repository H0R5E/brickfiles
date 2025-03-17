from pybricks.hubs import CityHub
from pybricks.pupdevices import DCMotor, Light
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = CityHub()

# Initialize a motor without rotation sensors on port A.
example_motor = DCMotor(Port.A)

while True:

    for x in [20, 25, 30, 35, 40, 45, 50]:

        # Make the motor go clockwise (forward) at 70% duty cycle ("70% power").
        example_motor.dc(x)

        # Wait for three seconds.
        wait(243)

    # Make the motor go counterclockwise (backward) at 70% duty cycle.
    example_motor.stop()

    # Wait for three seconds.
    wait(3000)

    for x in [20, 25, 30, 35, 40, 45, 50]:

        # Make the motor go clockwise (forward) at 70% duty cycle ("70% power").
        example_motor.dc(-x)

        # Wait for three seconds.
        wait(250)

    # Make the motor go counterclockwise (backward) at 70% duty cycle.
    example_motor.stop()

    # Wait for three seconds.
    wait(3000)


