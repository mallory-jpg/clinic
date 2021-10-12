
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.display.max_columns = None

# read in patient data
patients = pd.read_csv("/Users/mallory/ashwell_refactor/clinic/clinical/pts_2021.csv")

# create patient DataFrame
df = pd.DataFrame(patients)

# Clean race data
def update_race_gender(df):
    """
    Reassign demographic groups based on issue found in data exploration.
    :param df: Pandas DataFrame of patient appointment and demographic data
    :returns DataFrame: cleaned demographic DataFrame
    """
    if "Black or African American":
        df = df.replace("African American")
        return df
    if "African American":
        df = df.replace("Black")
        return df
    if "American Indian or Alaska Native" or "Mexican American Indian":
        df = df.replace("American Indian")
        return df
    if "Native Hawaiian or Other Pacific Islander":
        df = df.replace("Pacific Islander")
        return df
    if "Straight or heterosexual":
        df = df.replace("Straight")
        return df
    return df


def update_age(df):

    a1 =[18, 19, 20, 21, 22, 23, 24, 25]
    a2 = [26, 27, 28, 29, 30, 31, 32]
    a3 = [33, 34, 35, 36, 37, 38, 39, 40]
    a4 = [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    a5 = [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
    
    if df.age.isin(a1):
        df = df[a1]
        df = df.replace("18-25")
        return df
    elif df.age.isin(a2):
        df = df[a2]
        df = df.replace("26-32")
        return df
    elif df.age.isin(a3):
        df = df[a3]
        df = df.replace("33-40")
        return df
    elif df.age.isin(a4):
        df = df[a4]
        df = df.replace("41-50")
        return df
    else:
        df = df[a5]
        df = df.replace("51+")
        return df
    
    # return df

# instantiate demographic DF using function
demo_df = update_race_gender(df)
# print(demo_df.head(20))

# under_24 = 60
# under_30 = 65
# under_35 = 28

age = update_age(demo_df)

age = age.groupby("age").size().to_frame(name="count").reset_index()
# set index as age column
age.set_index("age", inplace = True)

print(age)
