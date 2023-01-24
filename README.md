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

## Command Line Options
```
usage: live_plot.py [-h] --host HOST [--warn WARN] [--crit CRIT] [--ping_count PING_COUNT] [--debug]

optional arguments:
  -h, --help            show this help message and exit
  --host HOST           Host name or IP address to ping
  --warn WARN           Int in milliseconds. Warning level for chart. Yellow color bars
  --crit CRIT           Int in milliseconds. Critical level for chart. Red color bars
  --ping_count PING_COUNT
                        Number of pings to send
  --debug               Print debug out
```