from ooc_features import data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.linear_model import LogisticRegression
from dateutil.parser import parse
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

# create gender dummies
data["M"] = data["gender"].apply(lambda x: 1 if x == "M" else 0)
data["F"] = data["gender"].apply(lambda x: 1 if x == "F" else 0)
data["NB"] = data["gender"].apply(lambda x: 1 if x == "NB" else 0)
# print(data.race.unique())

# get dummies for race
data["White"] = data["race"].apply(lambda x: 1 if x == "W" else 0)
data["OtherRace"] = data["race"].apply(lambda x: 1 if x == "Other" else 0)
data["Black"] = data["race"].apply(lambda x: 1 if x == "B" else 0)
data["Asian"] = data["race"].apply(lambda x: 1 if x == "A" else 0)
data["Indigenous"] = data["race"].apply(lambda x: 1 if x == "I" else 0)
data["PacificIslander"] = data["race"].apply(lambda x: 1 if x == "PI" else 0)
data = data.replace({"Yes":1})
print(data)

# get dummies for zipgp
zip_dummies = pd.get_dummies(data["zipgp"], prefix="zipgp")
df = pd.concat([data, zip_dummies], axis=1)
# delete original race column
df = df.drop("race", axis=1)
df = df.drop("gender", axis=1)
df = df.drop("zipgp", axis=1)
df = df.astype(int)
df["seen_last_3"] = df["seen_last_3"].replace({0:1, 1:0})
df = df.rename(columns={"seen_last_3": "out_of_care"})
# print(df.info())
print(df)

# data = data
features = df[["portalon", "public housing", "age", "incomelevel", "no show",
            "homelessstatus", "cm", "validemail", "M", "F", "NB", "White", "OtherRace", "Black", "Asian", "Indigenous",
            "PacificIslander", "zipgp_0", "zipgp_1", "zipgp_2", "zipgp_4", "zipgp_6", "zipgp_7",
            "zipgp_8", "zipgp_9", "zipgp_10", "zipgp_12"]]
ooc = df["out_of_care"]

X = features
y = ooc

# split dataset in features and target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
# print(features.info())
# print(ooc.info())

# normalize data
#norm_X = preprocessing.normalize(X)

# scale data
scale = StandardScaler()
scale.fit_transform(X)
scale.transform(X)

# instantiate the model
model = LogisticRegression(max_iter=10000)
# fit model to data
model.fit(X_train, y_train)
# score model
score = model.score(X_train, y_train)
# print(score)
print(features)
# analyze coefficients: most impactful are: 1(6.07394312e-01),2(1.14521476e+00),3(6.19469056e-03),
# 4(-6.77397875e-04),6(-6.68157946e-02),8(-1.02819091e+00),9(4.85672334e-02),11(-5.37805742e-01),
# 12(7.14627883e-02),13(-4.83920841e-01),14(2.55248794e-02),15(1.06734027e-01),16(3.01929701e-01),
# 18(-8.82050501e-01),19(1.65924886e-01),21(1.40698573e-01),22(2.30641514e-01),23(1.61086291e-01),
# 24(4.55865428e-02),26(9.32401958e-02),27(6.66030528e-02)

print(model.coef_)

# predicting outcome of a patient
Me = np.array([0, 0, 0, 23, 200, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0])
# new_patients = np.array([Me]).reshape(1, -1)

# fit patient features to model
Me = scale.transform([Me]).reshape(1, -1)
# predict new patient ooc; 0 = out of care, 1 = in care
print(model.predict(Me)) # predicted that I hadn't been seen in the last 3 months/fell out of care (closer to 1 than 0)
print(model.predict_proba(Me))
