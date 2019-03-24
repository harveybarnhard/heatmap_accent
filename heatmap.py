"""
    File name: heatmap.py
    Author: Harvey Barnhard
    Date created: 3/23/2019
    Date last modified: 3/23/2019
    Python Version: 3.7
"""

import sys
import os
import csv
import xml.etree.ElementTree as ET

# Set Working Directory
cd = os.path.dirname(os.path.abspath("C:\\Users\\Harvey\\Dropbox\\Projects\\heatmap\\data\\activities\\2132509368.tcx"))

# Read TCX File
tcx_file = ET.parse(open("C:\\Users\\Harvey\\Dropbox\\Projects\\heatmap\\data\\activities\\2132509368.tcx").readlines())

# Set columns

dom = lxml.etree.parse(os.path.join(cd, tcx_file))






