from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


api = KaggleApi()
api.authenticate()

#api.dataset_download_file("ky1338/10000-movies-letterboxd-data", "Movie_Data_File.csv")

#api.dataset_download_file("atharvasoundankar/global-cybersecurity-threats-2015-2024", "Global_Cybersecurity_Threats_2015-2024.csv")

# if the file doesn't download properly , try downloading it as a zip file then just drag and drop to the project folder
#api.dataset_download_file("imtkaggleteam/airplane-crashes", "Airplane_Crashes_and_Fatalities_Since_1908.csv")

# there are 10002 entries in this dataset!
#movie_data_file = pd.read_csv("Movie_Data_File.csv")

# there are 3000 entries in this dataset!
#cybersecurity_threats = pd.read_csv("Global_Cybersecurity_Threats_2015-2024.csv")

# there are 5268 entries in this dataset!
airplane_data = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv")

print(airplane_data.head())
print(airplane_data.shape)
# how the dataset looks like before changes

# option 1 : Drop the unavailable data

# how the dataset looks like after dropping

# option 2 : use the average value whenever you see a null / Nan value

# how the dataset looks like after using the average value