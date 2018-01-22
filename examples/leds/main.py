from microbit import *
from tm1637 import TM1637

tm = TM1637(clk=pin1, dio=pin2)

num = 0
class Stop(Exception):
    pass

try:
    # walk through all possible LED combinations
    # press A or B buttons to stop
    while True:
        for i in range(128):
            tm.number(i)
            tm.write([i])
            if button_a.is_pressed() or button_b.is_pressed():
                num = i
                raise Stop
            sleep(100)
except Stop:
    while True:
        # Press A to increment
        if button_a.is_pressed():
            num = num + 1
            if num > 255:
                num = 0
            tm.number(num)
            tm.write([num])
        # Press B to decrement
        elif button_b.is_pressed():
            num = num - 1
            if num < 0:
                num = 255
            tm.number(num)
            tm.write([num])
        sleep(100)
