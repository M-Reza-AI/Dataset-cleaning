import random

from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#api = KaggleApi()
#api.authenticate()

#api.dataset_download_file("ky1338/10000-movies-letterboxd-data", "Movie_Data_File.csv")

#api.dataset_download_file("atharvasoundankar/global-cybersecurity-threats-2015-2024", "Global_Cybersecurity_Threats_2015-2024.csv")

# if the file doesn't download properly , try downloading it as a zip file then just drag and drop to the project folder
#api.dataset_download_file("imtkaggleteam/airplane-crashes", "Airplane_Crashes_and_Fatalities_Since_1908.csv")

# there are 10002 entries in this dataset!
#movie_data_file = pd.read_csv("Movie_Data_File.csv")

# there are 3000 entries in this dataset!
# also the missing value is inserted as "Unknown" and most of the values are text
cybersecurity_threats = pd.read_csv("Global_Cybersecurity_Threats_2015-2024.csv")

# there are 5268 entries in this dataset!
#airplane_data = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv")


#print(movie_data_file.columns)
print(cybersecurity_threats.columns)
#print(airplane_data.columns)

# how the dataset looks like before changes

#heatmap_fig = sns.heatmap(movie_data_file.corr(numeric_only=True))
#heatmap_fig.figure.tight_layout()
#print(movie_data_file.info())
#plt.show()

#hist_fig = sns.scatterplot(cybersecurity_threats)
#print(cybersecurity_threats.head())
#print(cybersecurity_threats.info())
#plt.show()

# option 1 : Drop the unavailable data


# drops the [release year] column since it has no data , it uses axis = 1 to drop the column not the row
# and inplace = False means create a new dataframe and store

# create a new dataframe with the dropped column then drop all columns with the missing values
#new_movie_data_file = movie_data_file.drop('Release_year', axis=1, inplace=False)
#new_movie_data_file.dropna(inplace=True)
#print(new_movie_data_file.info())


# how the dataset looks like after dropping

#dropped_heatmap_fig = sns.heatmap(new_movie_data_file.corr(numeric_only=True))
#dropped_heatmap_fig.figure.tight_layout()
#plt.show()



# option 2 : use the average value whenever you see a null / Nan value
# TODO FINISH THIS LATER


# how the dataset looks like after using the average value


# option 3 : try to use one hot encoding
# TODO FINISH THIS LATER


# how the dataset looks like after using one hot encoding

# special case : if you want to replace a value with another random in a categorical column

# the reason why we do this is that there is a significant amount of unknown attack sources,
# but since there are 3 other categories we can assume that the unknown attack source is one of the 3.
# so we will increase the amount of times the others have happened at random.

def Replace_Unknown(threats):

    attack_source_count = {}
    for var in threats["Attack Source"]:
        if var not in attack_source_count:
            attack_source_count[var] = 0
            continue
        attack_source_count[var] += 1

    valid_attack_source = ["Hacker Group" , "Nation-state", "Insider"]
    for var in threats:
        if threats.loc("Attack Source", var) != threats.loc(var):

            pass # TODO FINISH THIS LATER

    threats.replace(to_replace="Unknown", value= 0)

    print(attack_source_count)


Replace_Unknown(cybersecurity_threats)