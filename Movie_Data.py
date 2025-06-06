from Helper.AI_Helper import *
from sklearn.impute import SimpleImputer

""" there are 10002 entries in this dataset! """

movie_data_file = pd.read_csv("Movie_Data_File.csv")


""" print the columns of the dataset you are interested in cleaning """

print(movie_data_file.columns)
print(movie_data_file.info())
print(movie_data_file.describe())
print(movie_data_file.isnull().sum())
print(movie_data_file.describe())

"""how the dataset looks pre-cleaning, you can use what you learned last lecture here!"""

heatmap_fig = sns.heatmap(movie_data_file.corr(numeric_only=True))
heatmap_fig.figure.tight_layout()
print(movie_data_file.info())
plt.show()

"""
option: Drop the unavailable data

drops the [release year] column since it has no data , 
it uses axis = 1 to drop the column not the row and inplace = False means create a new dataframe and store

create a new dataframe with the dropped column then drop all columns with the missing values
"""


new_movie_data_file = movie_data_file.drop('Release_year', axis=1, inplace=False)
new_movie_data_file.dropna(inplace=True)
print(new_movie_data_file.info())


"""how the dataset looks like after dropping"""

dropped_heatmap_fig = sns.heatmap(new_movie_data_file.corr(numeric_only=True))
dropped_heatmap_fig.figure.tight_layout()
plt.show()


"""option: use the average value whenever you see a null / Nan value"""

average_value_movie_rating = movie_data_file.drop('Release_year', axis=1, inplace=False)
replace_with_average = SimpleImputer(strategy="mean")

average_value_movie_rating[["Average_rating"]] = replace_with_average.fit_transform(average_value_movie_rating[["Average_rating"]])
average_value_movie_rating[["Runtime", "Owner_rating"]] = replace_with_average.fit_transform(average_value_movie_rating[["Runtime", "Owner_rating"]])


"""how the dataset looks like after using the average value"""

print(average_value_movie_rating.isnull().sum())
print(average_value_movie_rating.info())

dropped_heatmap_fig = sns.heatmap(average_value_movie_rating.corr(numeric_only=True))
dropped_heatmap_fig.figure.tight_layout()
plt.show()