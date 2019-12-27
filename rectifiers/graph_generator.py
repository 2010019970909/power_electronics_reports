# -*- coding: utf-8 -*-
"""
@author: Vincent

Requirement:
pip install matplotlib PyQt5 + MikTex
"""

# Global variables:
SAVE_PATH = 'figures'
EXTENSION = 'pdf'

# Locale settings
import locale
# Set to locale to get comma or dot as decimal separater
locale.setlocale(locale.LC_NUMERIC,'')

# Import the useful libs to plot the graph
import matplotlib
# import matplotlib.colors
matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt

plt.rcdefaults()
plt.rcParams['axes.formatter.use_locale'] = True
plt.rc('font', family='serif')

# Import numpy for the math
import numpy as np

# Import the data from the data file
import pandas as pd

xl = pd.ExcelFile('data.xlsx')
sheet = xl.sheet_names  # see all sheet names in the file

# Import system related lib
import os

# Generate the path the save folder
def gen_path(filename, save_path=SAVE_PATH, extension=EXTENSION):
    path = os.path.join(os.getcwd(), save_path, filename) + '.' + extension
    create_folder(os.path.join(os.getcwd(), save_path))
    return path

# Create the directory
def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

if __name__ == "__main__":
    print("This is a module, not a script.")
    print("Usage:")
    print('from graph_generator import *')

"""
else:
    print(sheet)
"""