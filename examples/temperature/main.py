from microbit import *
from tm1637 import TM1637

tm = TM1637(clk=pin1, dio=pin2)

while True:
    tm.temperature(temperature())
    sleep(1000)
