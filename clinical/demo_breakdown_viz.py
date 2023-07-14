
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.display.max_columns = None

# read in patient data
patients = pd.read_csv("pts_2021.csv")

# create patient DataFrame
df = pd.DataFrame(patients)

# Clean race data
def update_race_gender(df):
    """
    Reassign demographic groups based on issue found in data exploration.
    :param df: Pandas DataFrame of patient appointment and demographic data
    :returns DataFrame: cleaned demographic DataFrame
    """
    for i in df["race"]:
        if i == "Black or African American":
            df["race"] = df["race"].replace(i, "African American")
           
        if i == "African American":
            df["race"] = df["race"].replace(i, "Black")
            
        if i == "American Indian or Alaska Native" or "Mexican American Indian":
            df["race"] = df["race"].replace(i, "American Indian")
            
        if i == "Native Hawaiian or Other Pacific Islander":
            df["race"] = df["race"].replace(i, "Pacific Islander")
            
    for i in df["sex_orient"]:
        if i == "Straight or heterosexual":
                df["sex_orient"] = df["sex_orient"].replace(i, "Straight")
        if i == "Lesbian, gay or homosexual":
                df["sex_orient"] = df["sex_orient"].replace(i, "Homosexual")

    return df


def update_age(df):

    a1 = [18, 19, 20, 21, 22, 23, 24, 25]
    a2 = [26, 27, 28, 29, 30, 31, 32]
    a3 = [33, 34, 35, 36, 37, 38, 39, 40]
    a4 = [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    a5 = [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
    
    for i in df["age"]:
        if i in a1:
            df["age"] = df["age"].replace(i, "18-25")
        elif i in a2:
            df["age"] = df["age"].replace(i, "26-32")
        elif i in a3:
            df["age"] = df["age"].replace(i, "33-40")
        elif i in a4:
            df["age"] = df["age"].replace(i, "41-50")
        elif i in a5:
            df["age"] = df["age"].replace(i, "51+")
    return df


# instantiate demographic DF using function
demo_df = update_race_gender(df)
# print(demo_df.head(20))


age = update_age(demo_df)
print(age)

age = age.groupby("age").size().to_frame(name="count").reset_index()
# set index as age column
age.set_index("age", inplace = True)

print(age)
