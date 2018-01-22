from microbit import *
import random
from tm1637 import TM1637

tm = TM1637(clk=pin1, dio=pin2)

while True:
    tm.number(running_time() // 1000)
    sleep(1000)
