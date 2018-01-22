from microbit import *
from tm1637 import TM1637

tm = TM1637(clk=pin1, dio=pin2)

while True:
    tm.show('    ')
    sleep(1000)
    tm.show('1234')
    sleep(1000)
    tm.show('help')
    sleep(1000)
    tm.show('cafe')
    sleep(1000)
    tm.show('beef')
    sleep(1000)
    tm.show('rainbow') # only shows rain
    sleep(1000)
    tm.show('cool')
    sleep(1000)
    tm.show('f') # fool
    sleep(1000)
    tm.show('p') # pool
    sleep(1000)
    tm.show('t') # tool
    sleep(1000)
