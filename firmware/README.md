# Precompiled MicroPython firmware for the BBC micro:bit

https://github.com/bbcmicrobit/micropython

#### microbit-micropython-v1.7.9-gbe020eb.hex

* https://github.com/bbcmicrobit/micropython/commits/master
* https://github.com/bbcmicrobit/micropython/tree/09162c6b38d24f464db0fc1fbdf04658baaf9928

#### microbit-micropython-v1.9.2-34-gd64154c73.hex

* https://github.com/bbcmicrobit/micropython/commits/version1
* https://github.com/bbcmicrobit/micropython/tree/e17de0954178d88aa2a1d70b6e6ebc43f5456607

# Installation

* This will overwrite your scripts, so be sure to backup any existing code you wish to keep.
* Connect the micro:bit to your computer via USB and you should see a MICROBIT drive appear.
* Copy the v1.7.9 or v1.9.2 precompiled firmware `.hex` file to the MICROBIT drive and wait for board to reboot.
* Use [ufs](https://github.com/ntoll/microfs) to copy the `tm1637.py` script to the flash.
* Open the /examples folders and use `ufs` to copy one of the `main.py` scripts to the flash.
* Reboot the micro:bit to run `main.py`.
* Edit `main.py` and `ufs put` your changes and reboot.

```
$ ufs put tm1637.py
$ ufs put examples/counter/main.py
```
