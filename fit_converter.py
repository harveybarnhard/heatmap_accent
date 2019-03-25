"""
    File name: fit_converter.py
    Author: Harvey Barnhard
    email: harveybarnhard@uchicago.edu
    Date created: 3/23/2019
    Date last modified: 3/25/2019
    Python Version: 2.7
"""
# Modules
from fitparse import FitFile
import os
import pandas as pd

# Set working directory
path = "C:\\Users\\Harvey\\Dropbox\\Projects\\heatmap\\data\\activities"
os.chdir(path)

# Initialize lists that will eventually be columns in a dataframe
lat = list()
lon = list()
hrt = list()
dis = list()
tim = list()
ind = list()

# For each .fit file, obtain latitude and longitude positions, and mean
i=1
for filename in os.listdir(path):
    ind.append(i)
    if filename.endswith(".fit"):
        fit_file = FitFile(filename)
        for record in fit_file.get_messages():
            if record.type == 'data':
                lat_flag = 0
                lon_flag = 0
                hrt_flag = 0
                dis_flag = 0
                tim_flag = 0
                for field_data in record:
                    if field_data.name == "position_lat":
                        lat.append(field_data.value)
                        lat_flag = 1
                    if field_data.name == "position_long":
                        lon.append(field_data.value)
                        lon_flag = 1
                    if field_data.name == "heart_rate" and lat_flag == 1 and lon_flag == 1:
                        hrt.append(field_data.value)
                        hrt_flag = 1
                    if field_data.name == "distance" and lat_flag == 1 and lon_flag == 1:
                        dis.append(field_data.value)
                        dis_flag = 1
                    if field_data.name == "timestamp" and lat_flag == 1 and lon_flag == 1:
                        tim.append(field_data.value)
                        tim_flag = 1
                if lat_flag == 1 and lon_flag == 1 and hrt_flag == 0:
                    if hrt_flag == 0:
                        hrt.append([-1])
                    if dis_flag == 0:
                        dis.append([-1])
                    if tim_flag == 0:
                        tim.append([-1])
                    #if field_data.name in ["position_lat", "position_long", "heart_rate"]:
                    #    print ' * {}: {}'.format(field_data.name, field_data.value)
    i+=1

# Create dataframe and save as csv to working directory
fit_data = {"LON":lon, "LAT":lat, "HRT":hrt, "DIS":dis, "TIM":tim}
fit_df = pd.DataFrame(fit_data)
fit_df.to_csv("fit_df.csv", sep=",", index=False)
