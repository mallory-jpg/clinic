import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.display.max_columns = None

patients = pd.read_csv("pts_2021.csv")
df = pd.DataFrame(patients)
df = df.replace(to_replace="Black or African American", value="African American")
df = df.replace(to_replace="African American", value="Black")
df = df.replace(to_replace="Straight or heterosexual", value="'Straight'")
df = df.replace(to_replace=["American Indian or Alaska Native", "Mexican American Indian"], value="American Indian")
df = df.replace(to_replace="Native Hawaiian or Other Pacific Islander", value="Pacific Islander")
# print(df.head())

# race = df.groupby("race").size().to_frame(name="count").reset_index()
# print(race)

age = df.groupby("age").size().to_frame(name="count").reset_index()
# under_24 = 60
# under_30 = 65
# under_35 = 28
age["age"] = age["age"].replace([18, 19, 20, 21, 22, 23, 24, 25], "18-25")
age["age"] = age["age"].replace([26, 27, 28, 29, 30, 31, 32], "26-32")
age["age"] = age["age"].replace([33, 34, 35, 36, 37, 38, 39, 40], "33-40")
age["age"] = age["age"].replace([41, 42, 43, 44, 45, 46, 47, 48, 49, 50], "41-50")
age["age"] = age["age"].replace([51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], "51+")

age = age.groupby("age").size().to_frame(name="count").reset_index()
age.set_index("age", inplace = True)
print(age)
