# gui-ping-monitor
GUI tool for monitoring ping responses written in Python. Live updating gui chart showing ping response time. Uses matplotlib for visualization. It has been tested on MacOS and Linux.

![screenshot](/screenshots/screenshot1.jpg)

## Prerequisites
gui-ping-monitor needs a few libraries
```
pip3 install matplotlib
pip3 install icmplib
```

## Example command
```
sudo python3 live_plot.py --host=1.1.1.1
```
