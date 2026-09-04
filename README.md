# cs350RaspPi

Derek Hui CS-350 

## Progressive circuit builds using a Raspberry Pi and various components.

> These modules were basic builds of the RPi, starting from simple blinks of an LED to a functional machine that read ambient temperature. The final project was to build a working thermometer that could read temperature and react based on a set state (cool/heating). The setup was the pi with a breakout board to extend the GPIO pins to a breadboard. A 16x2 LCD screen was used to display the current state and temperature and push buttons to change the states of the thermostat. 2 buttons were used to increase or decrease the set temperature which would affect the state of the machine.
 IMAGE

The temperature sensor used was the AHT20 temp+humidity sensor
IMAGE

The problem to solve here was creating a proper state machine that would set the correct state depending on a set temperature relative to the actual temperature read from the sensor. The way to solve this was using the python StateMachine library. It's an easy to use library where you create states, cycle that moves through the states, and transitions between states.

IMAGE OF CLASS
LINK TO FILE

> Each transition will automatically call a callback function that will perform the physical action on the components, in this case a few LEDs to act a visual queues for the current state by fading in and out.
