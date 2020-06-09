# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 20:56:20 2020

@author: Alfredo
"""

#!/usr/bin/python
#
# Copyright (c) 2018, 2019 TainiTec Ltd.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import os.path
import numpy as np
import matplotlib.pyplot as plt

number_of_channels = 16
sample_rate = 1000
sample_datatype = 'int16'
display_decimation = 10



def main(fn):
    '''Check the input data format, load it and then plot it'''
    
    print("Parsing file \"" + fn + "\"")
    # Simple error checking
    assert os.path.isfile(fn)       # input file must exist
    assert fn[-4:] == ".dat"        # input file must be a .dat
    assert os.path.getsize(fn) > 0  # input file must be nonempty

    # Load the data (won't work for long recordings, you will need to chunk)
    dat, t = load_dat(fn)

    # Plot the data
    plot_dat(dat, t)


def load_dat(fn):
    '''Load a .dat file by interpreting it as int16 and then de-interlacing the 16 channels'''

    # Load the raw (1-D) data
    dat_raw = np.fromfile(fn, dtype=sample_datatype)

    # Reshape the (2-D) per channel data
    step = number_of_channels * display_decimation
    dat_chans = [dat_raw[c::step] for c in range(number_of_channels)]

    # Build the time array
    t = np.arange(len(dat_chans[0]), dtype=float) / sample_rate

    return dat_chans, t


def legend_pick(event):
    '''Event handler for selecting which channels to display in the plot'''

    global fig, line_lookup

    # Get the current visibility of the clicked line
    legend_line = event.artist
    ch_line = line_lookup[legend_line]
    visible = ch_line[0].get_visible()

    # Change the visibility
    ch_line[0].set_visible(not visible)

    # Update the label visibility
    if visible:
        legend_line.set_alpha(0.3)
    else:
        legend_line.set_alpha(1.0)

    # Redraw the plot
    fig.canvas.draw()


def plot_dat(dat, t):
    '''Plot the data in a matplotlib figure'''

    global fig,line_lookup

    # Setup plot
    fig, ax = plt.subplots()
    ax.set_title('Legend can be clicked to toggle channels on and off...')

    # Plot each channel
    ch_lines = []
    for c_idx in range(len(dat)):
        ch_lines.append(ax.plot(t, dat[c_idx], label='Ch'+str(c_idx)))

    # Set the legend and properties
    ax_legend = ax.legend(loc=1)

    # Create a dictionary of the lines and their associated legend
    line_lookup = dict()
    legend_lines = ax_legend.get_lines()
    for ch_line, legend_line in zip(ch_lines, legend_lines, ):
        legend_line.set_picker(10)
        line_lookup[legend_line] = ch_line

    # Set the callback
    fig.canvas.mpl_connect('pick_event', legend_pick)

    # Display
    plt.show()



if __name__ == "__main__":

    fn = "C:\\Users\\Alfredo\\Desktop\\Tainitec\\TAINI_1033_1240_Group2_5dpKA-2020_03_02-0000.dat"
    main(fn)