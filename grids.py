import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as AxisArtist
import matplotlib.ticker as ticker

plt.style.use('seaborn')

def simple_grid_10x10(x,y):
    mpl.rc('lines', linestyle='-', marker='o')
    fig = plt.figure(1, figsize=(7,7))
    ax = AxisArtist.Axes(fig, [-1, -1, 1, 1])
    fig.add_axes(ax)

    ax.axis['top','bottom','right','left'].set_visible(False)
    ax.axis['y=0'] = ax.new_floating_axis(nth_coord=0, value=0)
    ax.axis['x=1'] = ax.new_floating_axis(nth_coord=1, value=0)
    ax.axis["x=1"].set_axis_direction("left")

    ax.axis[:].major_ticks.set_tick_out(True)
    ax.axis[:].label.set_pad(10)
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)

    plt.plot(x,y)
    startx, endx = ax.get_xlim()
    ax.xaxis.set_ticks(np.arange(startx, endx, 1))
    starty, endy = ax.get_ylim()
    ax.yaxis.set_ticks(np.arange(starty, endy, 1))
    ax.grid(True)
    
def unit_circle(x,y):
    mpl.rc('lines', linestyle='-', marker='o')
    fig = plt.figure(1, figsize=(7, 7))
    ax = AxisArtist.Axes(fig, [-1, -1, 1, 1])
    fig.add_axes(ax)

    ax.axis['top','bottom','right','left'].set_visible(False)
    ax.axis['y=0'] = ax.new_floating_axis(nth_coord=0, value=0)
    ax.axis['x=1'] = ax.new_floating_axis(nth_coord=1, value=0)
    ax.axis["x=1"].set_axis_direction("left")

    ax.axis[:].major_ticks.set_tick_out(True)
    ax.axis[:].label.set_pad(10)
    ax.set_xlim(-1.5,1.5)
    ax.set_ylim(-1.5,1.5)
    
    circle = mpatches.Circle((0,0), 1, ec="black", fc="gray", lw=1.5, alpha=0.12, zorder=5)
    ax.add_artist(circle)

    plt.plot(x,y)
    startx, endx = ax.get_xlim()
    ax.xaxis.set_ticks(np.arange(startx, endx, 0.5))
    starty, endy = ax.get_ylim()
    ax.yaxis.set_ticks(np.arange(starty, endy, 0.5))
    ax.grid(True)
