from microbit import *
import random
from tm1637 import TM1637

tm = TM1637(clk=pin1, dio=pin2)

random.seed(1337)

tm.show('rand')

while True:
    if button_a.was_pressed():
        tm.number(random.randint(1, 9999))
