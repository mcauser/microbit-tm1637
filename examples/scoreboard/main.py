from microbit import *
from tm1637 import TM1637

tm = TM1637(clk=pin1, dio=pin2)

# write P1:P2
tm.show('P1P2', True)
sleep(1000)

player1 = 0
player2 = 0
tm.numbers(player1, player2)

while True:
    if button_a.is_pressed():
        player1 = player1 + 1
        tm.numbers(player1, player2)
    if button_b.is_pressed():
        player2 = player2 + 1
        tm.numbers(player1, player2)
    sleep(100)
