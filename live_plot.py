import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from icmplib import ping
import random
import argparse

# Setup argparse
parser = argparse.ArgumentParser()
parser.add_argument('--host', type=str, required=True, help='Host name or IP address to ping')
parser.add_argument('--warn', type=int, default=50, help='Int in milliseconds. Warning level for chart. Yellow color bars')
parser.add_argument('--crit', type=int, default=100, help='Int in milliseconds. Critical level for chart. Red color bars')
parser.add_argument('--ping_count', type=int, default=2, help='Number of pings to send')
parser.add_argument('--debug', action='store_true', help='Print debug out')
args = parser.parse_args()

# initial data
hostname = args.host
crit_value = args.crit
warn_value = args.warn
ping_count = args.ping_count
total_interval = 120
data = [0] * total_interval

# create figure and axes objects
fig, ax = plt.subplots()

# Set the width and height
fig.set_figwidth(10)
fig.set_figheight(5)
fig.canvas.manager.set_window_title('ping monitoring for host ' + hostname)
ax = fig.add_axes((0.06, 0.06, 0.9, 0.94))

# animation function
def animate(i):
    host = ping(hostname, count=ping_count, interval=0.1)
    data.pop(0)
    if host.min_rtt == 0 and host.packet_loss > 0:
        data.append(crit_value * 2)
    else:
        data.append(host.min_rtt)
    if args.debug:
        print(host)
    ax.clear()
    for point in range(0, total_interval):
        if data[point] >= crit_value:
            bar_color = 'red'
        elif data[point] >= warn_value and data[point] < crit_value:
            bar_color = 'y'
        else:
            bar_color = 'green'
        ax.bar(point, data[point], color=bar_color)
    ax.axhline(y=warn_value, color='y', linestyle='dotted')
    ax.axhline(y=crit_value, color='red', linestyle='dotted')
    ax.set_ylabel('Avg Resp Time in ms')
    ax.set_title(hostname +' Ping response time for past ' + str(total_interval) + ' seconds')
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_ylim(ymin=0)

# call the animation
ani = FuncAnimation(fig, animate, interval=1000)

# show the plot
plt.show()
