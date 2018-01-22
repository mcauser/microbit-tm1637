from microbit import *
from tm1637 import TM1637

tm = TM1637(clk=pin1, dio=pin2)

while True:
    tm.scroll('Hello World', 500)
    sleep(2000)
    tm.scroll('The quick brown fox jumps over the lazy dog')
    sleep(2000)
    tm.scroll('123456789')
    sleep(2000)
