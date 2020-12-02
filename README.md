# Heatmap
Create plots of running/cycling routes using bulk exported data from Strava (or Garmin Connect).
Running/cycling events can be accented by certain criteria. In the example below, all events with
an upper-quartile heart-rate exceeding a set threshold are colored red. All other runs are colored black.

# Example
![heatmap_picture](https://harveybarnhard.com/img/heatmap_accent-2.png)

# Files
fit_converter.py converts a set of .fit files (each file corresponding to a single event) into a .csv file where each row corresponds to
a time during an event (i.e. each event has many rows, longer events have more rows). Columns include timestamp, latitude and longitude, heart-rate, distance travelled, and event number.

heatmap.py plots the routes by event number. See example above. Each thread corresponds to a single event.

# Notes
fit_converter.py uses Python 2.7 while heatmap.py uses Python 3.7. Note that depending on your GPS device,
fit_converter.py may not be able to convert GPS files into a single csv file. Most modern Garmin devices should work since
event files are stored in the .fit format. There are other online resources on how to convert other filetypes (e.g. .tcx files) to csv.
fit_converter.py and heatmap.py assume that the data device you are using measures heart-rate.

Instructions on how to bulk-export data from Strava:

https://support.strava.com/hc/en-us/articles/216918437-Exporting-your-Data-and-Bulk-Export
