"""
    File name: fit_converter.py
    Author: Harvey Barnhard
    Date created: 3/23/2019
    Date last modified: 3/23/2019
    Python Version: 2.7
"""

from fitparse import FitFile
import os
import pandas as pd

# Read in .fit files
fit_file = FitFile("C:\\Users\\Harvey\\Dropbox\\Projects\\heatmap\\data\\activities\\1850568882.fit")

# For each .fit file, obtain latitude and longitude positions, and mean
for record in fit_file.get_messages():
    if record.type == 'data':
        for field_data in record:
            if field_data.name in ["position_lat", "position_long", "heart_rate"]:
                print ' * {}: {}'.format(field_data.name, field_data.value)