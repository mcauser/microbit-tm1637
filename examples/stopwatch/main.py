from microbit import *
from tm1637 import TM1637

tm = TM1637(clk=pin1, dio=pin2)

tm.show('stop')

num = 0
started = False

while True:
    if button_a.was_pressed():
        # start/stop
        started = not started
    if button_b.was_pressed():
        # reset
        num = 0
        started = False
        tm.number(num)
    if started:
        num = num + 1
        tm.number(num)
    sleep(1000)
