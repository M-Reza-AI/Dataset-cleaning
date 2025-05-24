import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

movie_data_file = pd.read_csv("Movie_Data_File.csv")

print(movie_data_file['Runtime'])