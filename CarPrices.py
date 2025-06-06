from Helper.AI_Helper import *
from sklearn.preprocessing import OneHotEncoder

""" there are 13 entries """
carprices = pd.read_csv("carprices.csv")

print(carprices.info())
print(carprices.columns)
print(carprices.head())


"""option: try to use one hot encoding"""

"""you can use one hot encoding either from sklearn or get_dummies from pandas"""
encoded_df= pd.get_dummies(carprices["Age(yrs)"])

print(encoded_df.columns)
print(encoded_df.head())

encoder = OneHotEncoder(sparse_output=False)

encoded_age = encoder.fit_transform(carprices[["Age(yrs)"]])

encoded_age_cols = encoder.get_feature_names_out(["Age(yrs)"])

encoded_age_df = pd.DataFrame(encoded_age, columns=encoded_age_cols)

encoded_carprices = pd.concat([carprices.drop("Age(yrs)", axis = 1), encoded_age_df], axis=1)

# how the dataset looks like after using one hot encoding

print(encoded_carprices.columns)
print(encoded_carprices.head())
print(encoded_carprices.info())


