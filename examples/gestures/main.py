from microbit import *
from tm1637 import TM1637

tm = TM1637(clk=pin1, dio=pin2)

while True:
    gesture = accelerometer.current_gesture()
    if gesture == "up":
        tm.scroll('up');
    elif gesture == "down":
        tm.scroll('down');
    elif gesture == "left":
        tm.scroll('left');
    elif gesture == "right":
        tm.scroll('right');
    elif gesture == "face up":
        tm.scroll('face up');
    elif gesture == "face down":
        tm.scroll('face down');
    elif gesture == "freefall":
        tm.scroll('freefall');
    elif gesture == "3g":
        tm.scroll('3g');
    elif gesture == "6g":
        tm.scroll('6g');
    elif gesture == "8g":
        tm.scroll('8g');
    elif gesture == "shake":
        tm.scroll('shake');
