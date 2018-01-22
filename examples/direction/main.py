from microbit import *
from tm1637 import TM1637

tm = TM1637(clk=pin1, dio=pin2)

compass.calibrate()

while True:
    tm.number(compass.heading())
    needle = ((15 - compass.heading()) // 30) % 12
    display.show(Image.ALL_CLOCKS[needle])
    sleep(10)
