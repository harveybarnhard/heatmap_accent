"""
    File name: fit_converter.py
    Author: Harvey Barnhard
    Date created: 3/23/2019
    Date last modified: 3/23/2019
    Python Version: 2.7
"""

from fitparse import FitFile

# Read in .fit files

fitfile = FitFile("C:\\Users\\Harvey\\Dropbox\\Projects\\heatmap\\data\\activities\\1850568882.fit")

# For each .fit file, obtain latitude and longitude positions

for record in fitfile.get_messages():
    if record.type == 'data':
        for field_data in record:
            if field_data.name in ["position_lat", "position_long"]:
                print ' * {}: {}'.format(field_data.name, field_data.value)
