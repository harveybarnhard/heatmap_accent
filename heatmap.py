"""
    File name: heatmap.py
    Author: Harvey Barnhard
    Date created: 3/23/2019
    Date last modified: 4/01/2019
    Python Version: 3.7
"""

# Import modules
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in .csv file outputted by fit_converter.py
data_path = "C:\\Users\\Harvey\\Dropbox\\Projects\\heatmap\\data\\activities"
out_path = "C:\\Users\\Harvey\\Dropbox\\Projects\\heatmap"
os.chdir(data_path)
fit_df = pd.read_csv("fit_df.csv")

lon = fit_df.LON
lat = fit_df.LAT
ind = fit_df.IND
hrt = fit_df.HRT
dis = fit_df.HRT
tim = fit_df.TIM

# Set longitude and latitude limits. Default is set for Hyde Park to the Loop in Chicago
plt.xlim(-1046508072.9, -1044694627.1)
plt.ylim(498121434.85, 499899488.15)

# Plot each event individually
for event in np.unique(ind):
    idx = ind == event
    hrt_75 = np.percentile(hrt[idx], 75)
    if hrt_75 <= 150:
        color = "black"
    else:
        color = "red"
    plt.plot(lon[idx], lat[idx], color, linewidth=0.02)
plt.axis("off")
# Save plot as a pdf file. Higher dpi for higher resolution. If plot does not save, try lowering dpi
plt.savefig('heartrate.pdf', dpi=3000, bbox_inches="tight", rasterized=True)
plt.clf()