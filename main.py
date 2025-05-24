from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

api = KaggleApi()
api.authenticate()
"""


 
the datasets used in this lecture

api.dataset_download_file("ky1338/10000-movies-letterboxd-data", "Movie_Data_File.csv")
api.dataset_download_file("atharvasoundankar/global-cybersecurity-threats-2015-2024", "Global_Cybersecurity_Threats_2015-2024.csv")
api.dataset_download_file("imtkaggleteam/airplane-crashes", "Airplane_Crashes_and_Fatalities_Since_1908.csv")
api.dataset_download_file("raihan150146/car-price-dataset-for-one-hot-encoding" , "carprices.csv")

 if the file doesn't download properly , try downloading it as a zip file then just drag and drop to the project folder
 
"""

""" there are 13 entries """
carprices = pd.read_csv("carprices.csv")

print(carprices.info())
print(carprices.columns)
print(carprices.head())
"""
there are 10002 entries in this dataset!
"""

movie_data_file = pd.read_csv("Movie_Data_File.csv")

"""
there are 3000 entries in this dataset!
also the missing value is inserted as "Unknown" and most of the values are text
"""

#cybersecurity_threats = pd.read_csv("Global_Cybersecurity_Threats_2015-2024.csv")

"""there are 5268 entries in this dataset!"""

#airplane_data = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv")



"""print the columns of the dataset you are interested in cleaning"""

"""
print(movie_data_file.columns)
print(movie_data_file.info())
print(movie_data_file.describe())
print(movie_data_file.isnull().sum())
print(movie_data_file.describe())
"""


"""
print(cybersecurity_threats.columns)
print(cybersecurity_threats.info())
print(cybersecurity_threats.describe())
print(cybersecurity_threats.isnull().sum())

"""

"""
print(airplane_data.columns)
print(airplane_data.info())
print(airplane_data.describe())
print(airplane_data.isnull().sum())

"""

"""how the dataset looks pre-cleaning, you can use what you learned last lecture here!"""

# heatmap_fig = sns.heatmap(movie_data_file.corr(numeric_only=True))
# heatmap_fig.figure.tight_layout()
# print(movie_data_file.info())
# plt.show()
#
# hist_fig = sns.scatterplot(cybersecurity_threats)
# print(cybersecurity_threats.head())
# print(cybersecurity_threats.info())
# plt.show()

"""
option 1 : Drop the unavailable data

drops the [release year] column since it has no data , 
it uses axis = 1 to drop the column not the row and inplace = False means create a new dataframe and store

create a new dataframe with the dropped column then drop all columns with the missing values
"""


#new_movie_data_file = movie_data_file.drop('Release_year', axis=1, inplace=False)
#new_movie_data_file.dropna(inplace=True)
#print(new_movie_data_file.info())


"""how the dataset looks like after dropping"""

#dropped_heatmap_fig = sns.heatmap(new_movie_data_file.corr(numeric_only=True))
#dropped_heatmap_fig.figure.tight_layout()
#plt.show()


"""option 2 : use the average value whenever you see a null / Nan value"""

# average_value_movie_rating = movie_data_file.drop('Release_year', axis=1, inplace=False)
# replace_with_average = SimpleImputer(strategy="mean")
#
# average_value_movie_rating[["Average_rating"]] = replace_with_average.fit_transform(average_value_movie_rating[["Average_rating"]])
# average_value_movie_rating[["Runtime", "Owner_rating"]] = replace_with_average.fit_transform(average_value_movie_rating[["Runtime", "Owner_rating"]])


"""how the dataset looks like after using the average value"""

# print(average_value_movie_rating.isnull().sum())
# print(average_value_movie_rating.info())
#
# dropped_heatmap_fig = sns.heatmap(average_value_movie_rating.corr(numeric_only=True))
# dropped_heatmap_fig.figure.tight_layout()
# plt.show()


"""option 3 : try to use one hot encoding"""

"""you can use one hot encoding either from sklearn or get_dummies from pandas"""
# encoded_df= pd.get_dummies(carprices["Age(yrs)"])
#
# print(encoded_df.columns)
# print(encoded_df.head())


encoder = OneHotEncoder(sparse_output=False)

encdoded_age = encoder.fit_transform(carprices[["Age(yrs)"]])

encdoded_age_cols = encoder.get_feature_names_out(["Age(yrs)"])

encdoded_age_df = pd.DataFrame(encdoded_age, columns=encdoded_age_cols)

encoded_carprices = pd.concat([carprices.drop("Age(yrs)", axis = 1), encdoded_age_df], axis=1)

# how the dataset looks like after using one hot encoding

print(encoded_carprices.columns)
print(encoded_carprices.head())
print(encoded_carprices.info())
"""
special case : if you want to replace a value with another random in a categorical column

the reason why we do this is that there is a significant amount of unknown attack sources,
but since there are 3 other categories we can assume that the unknown attack source is one of the 3.
so we will increase the amount of times the others have happened at random.

"""

"""
What we want here is:

1- iterate through the entire "Attack source" column
2- find every instance of "Unknown"
3- replace that instance with a valid attack source at random

Note : the function isn't being called , call it for demonstration

"""

def Replace_Unknown(threats):

    # create a list of attack sources and keep count if their recurring instances

    attack_source_count = {}
    for var in threats["Attack Source"]:
        if var not in attack_source_count:
            attack_source_count[var] = 0
            continue
        attack_source_count[var] += 1

    # create a list of only the attack sources that aren't unknown
    valid_attack_source = ["Hacker Group" , "Nation-state", "Insider"]

    # using numpy to iterate through the Attack source column and replace it with a random valid attack
    mask = threats["Attack Source"].isin(["Unknown"])
    threats.loc[mask, "Attack Source"] = np.random.choice(valid_attack_source, size=mask.sum())

    # count the new values
    new_attack_source_count = {}
    for var in threats["Attack Source"]:
        if var not in new_attack_source_count:
            new_attack_source_count[var] = 0
            continue
        new_attack_source_count[var] += 1


    print(attack_source_count)
    print(new_attack_source_count)
    """
    you can also use SimpleImputer here 
    
    cat_imputer = SimpleImputer(strategy='most_frequent')
    cat_imputer = SimpleImputer(strategy='constant', fill_value='Unknown')
    threats[["Attack_source"]] = cat_imputer.fit_transform(threats[["Attack_source"]])
    
    """


