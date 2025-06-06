from Helper.AI_Helper import *




"""
there are 3000 entries in this dataset!
also the missing value is inserted as "Unknown" and most of the values are text
"""

cybersecurity_threats = pd.read_csv("Global_Cybersecurity_Threats_2015-2024.csv")


print(cybersecurity_threats.columns)
print(cybersecurity_threats.info())
print(cybersecurity_threats.describe())
print(cybersecurity_threats.isnull().sum())

"""how the dataset looks pre-cleaning, you can use what you learned last lecture here!"""


hist_fig = sns.scatterplot(cybersecurity_threats)
print(cybersecurity_threats.head())
print(cybersecurity_threats.info())
plt.show()

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

Replace_Unknown(cybersecurity_threats)



"""
you can also use SimpleImputer here 

cat_imputer = SimpleImputer(strategy='most_frequent')
cat_imputer = SimpleImputer(strategy='constant', fill_value='Unknown')
threats[["Attack_source"]] = cat_imputer.fit_transform(threats[["Attack_source"]])

"""