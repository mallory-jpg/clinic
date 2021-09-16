"""Predict factors that are most impactful on patients falling out of care"""

import pandas as pd
import datetime as dt
from datetime import date, datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from dateutil.parser import parse
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn import preprocessing

df = pd.read_csv("out_of_care.csv")
pd.options.display.max_columns = 60
pd.options.display.max_colwidth = 500

# delete unnecessary columns
df = df.drop(["ptnt ptnt ssstnc prgrm stts", "APPTCANCELREASONTYP", "ptnt dsblty", "license expiration",
              "firstapptdate", "patientsex"], axis=1)
# delete patients missing vital info
df = df.dropna(subset=["patientlastseend"])

# fill empty values
df.fillna({"pblchouspat": "N",
           "incomelevel": 0,
           "apptcancelreason": "not no show",
           "ptnt shwll cs mngmnt": "N",
           "homelessstatus": "N",
           "race": "Other Race",
           "pat gender identity": "NB"},
           inplace=True)

#print(df.race.unique())

df["race"] = df["race"].replace(["Black or African American", "African American", "Black", "African"], "B")
df["race"] = df["race"].replace("Middle Eastern or North African", "Arab")
df["race"] = df["race"].replace("White", "W")
df["race"] = df["race"].replace(["Other Race", "Patient Declined"], "Other")
df["race"] = df["race"].replace(["Other Pacific Islander", "Native Hawaiian or Other Pacific Islander"], "PI")
df["race"] = df["race"].replace("Asian", "A")
df["race"] = df["race"].replace(["American Indian or Alaska Native", "Mexican American Indian", "American Indian"], "I")

df["pblchouspat"] = df["pblchouspat"].replace("P", "Y")

df = df.rename(columns={"apptcancelreason": "no show",
                        "ptnt shwll cs mngmnt": "cm",
                        "pat gender identity": "gender",
                        "patient age": "age",
                        "patient zip": "zip_code",
                        "patientlastseend": "seen_last_3_mo",
                        "pblchouspat": "public housing"})

df["no show"] = df["no show"].replace(["not no show", "PATIENT RESCHEDULED", "PATIENT CANCELLED",
                                                         "SCHEDULING ERROR"], "N")
df["no show"] = df["no show"].replace("PATIENT NO SHOW", "Y")
df["cm"] = df["cm"].replace("No", "N")
df["homelessstatus"] = df["homelessstatus"].replace("P", "Y")

df["gender"] = df["gender"].replace("Male", "M")
df["gender"] = df["gender"].replace(["Genderqueer", "Genderqueer (neither exclusively male nor female)"], "NB")
df["gender"] = df["gender"].replace("Additional gender category or other", "NB")

df["seen_last_3_mo"] = pd.to_datetime(df["seen_last_3_mo"])

today = datetime.now().date()
last_seen = df["seen_last_3_mo"]

def time_change(data):
    cutoff = today - timedelta(days=90)
    list = []
    for i in data:
        converted_date = datetime.date(i)
        if converted_date <= cutoff:
            list.append("No")
        else:
            list.append("Yes")
    return pd.Series(list, index=df.patientid)
    #return pd.Series(list, index=df.index) # df["seen_last_3_mo"])

df2 = time_change(last_seen).to_frame()
df2 = df2.rename(columns={0: "seen_last_3"})

df3 = df2.merge(df, how="inner", on="patientid")
df3 = df3.drop("seen_last_3_mo", axis=1)

# y = 1, n = 0
df3 = df3.replace("Y", 1)
df3 = df3.replace(["N", "No"], 0)
sorted_zips = sorted(df3.zip_code.unique())

df3.drop_duplicates(subset ="patientid",
                     keep = False, inplace = True)
#print(df3)

# replace zip codes with zip code groupings: urban, suburban, city
def zip_code_grouping(data):
    zips = []
    for i in data:
        i = str(i)
        first_two = i[:2]
        if first_two == "22":
            zips.append("1")
        elif first_two == "27":
            zips.append("2")
        elif first_two == "28":
            zips.append("3")
        elif first_two == "33":
            zips.append("4")
        elif first_two == "44":
            zips.append("5")
        elif first_two == "59":
            zips.append("6")
        elif first_two == "75":
            zips.append("7")
        elif first_two == "76":
            zips.append("8")
        elif first_two == "77":
            zips.append("9")
        elif first_two == "78":
            zips.append("10")
        elif first_two == "85":
            zips.append("11")
        elif first_two == "98":
            zips.append("12")
        else:
            zips.append("0")
    return pd.Series(zips, index=df3["patientid"])

zip_df = zip_code_grouping(df3.patientid)

zip_df = zip_df.to_frame("zipgp")
zip_df = zip_df.reset_index()
zip_df = zip_df.set_index("patientid")
#print(zip_df)
df3 = df3.set_index("patientid")
#print(df3)

# join dataframes
data = df3.join(zip_df)
data = data.drop(["zip_code", "apptday"], axis=1)
print(data.seen_last_3.unique())

