""" Graphing based on diagnoses; HIV, PrEP/PEP, HepC, STI only"""

import pandas as pd
from matplotlib import rc
import matplotlib.pyplot as plt

rc("font", **{"family":"serif", "serif":["Times"]})

appointments = pd.read_csv("patient_appts.csv")
# total_appts = 7803
# print(appointments.head())

df = pd.DataFrame(appointments)
# print(df.appttype.unique())

def get_appt_type(df):
    """    
    Reassign and regroup appointment types.
    :param df: Pandas DataFrame of patient appointment data
    :returns DataFrame: cleaned appointment DataFrame
    """
    for i in df["appttype"]:
        if i in ["ANY 15", "Any", "FOLLOW UP 15"]:
            df["appttype"] = df["appttype"].replace(i, "Any 15")
        
        if i in ["HCV: 4 Week Therapy Labs", "HCV: Lab Review with Client",
                                                    "Hep C: F/U Labs Only", "Hep C: F/U Labs and Provider",
                                                    "Hep C: Initial Labs Only", "Hep C: Rx (No Labs)"]:
            
            df["appttype"] = df["appttype"].replace(i, "Hep C")
        
        if i in ["HIV: F/U Labs and Provider", "HIV: Initial (New Care)",
                                                    "HIV: Initial (Transfer)", "HIV: Lab review with Client",
                                                    "HIV: Labs Only (No Provider)", "HIV: Provider F/U (No Labs)",
                                                    "HIV: Restart"]:
            df["appttype"] = df["appttype"].replace(i, "HIV Care")

        if i in ["HRT: Follow Up", "HRT: Initial"]:
            df["appttype"] = df["appttype"].replace(i, "HRT")

        if i in ["PEP: 2 PrEP", "PEP: A/R (Assault/Rape)", "PEP: Follow Up",
                                                    "PEP: Initial (Existing)", "PEP: Initial (New to Care)",
                                                    "PEP: Labs"]:
            df["appttype"] = df["appttype"].replace(i, "PEP") 

        if i in["PrEP Rx", "PrEP: 1 Month", "PrEP: 2 PEP", "PrEP: 3 Month",
                                                    "PrEP: 6 Month", "PrEP: Follow Up", "PrEP: Initial (New to Care)",
                                                    "PrEP: Initial (Transfer)", "PrEP: L/C F/U", "PrEP: L/C Initial (New)",
                                                    "PrEP: Labs", "PrEP: Restart", "Outreach: PrEP",
                                                    "Prep: L/C Initial (Transfer)"]:
            df["appttype"] = df["appttype"].replace(i, "PrEP")

        if i in ["STI: Non Primary Services", "STI: Symptomatic", "Outreach: Testing"]:
            df["appttype"] = df["appttype"].replace(i, "STI Non-Primary Services")

        if i in ["STI: PrEP", "STI: Labs and Treatment", "STI: Testing/Labs"]:
            df["appttype"] = df["appttype"].replace(i, "STI Primary Services")

        if i == "TeleHealth Appointment":
            df["appttype"] = df["appttype"].replace(i, "Unspecified Telehealth")

    return df

def cleanup(df):
    """
    Delete unnecessary rows and columns.
    :param df: Pandas DataFrame of patient data
    :returns DataFrame: cleaned DataFrame
    """
    # delete unused columns
    del df["apptdate"]
    del df["patientid"]

    # deleting unnecessary rows
    df = df[~df.appttype.str.contains("Medication Pick Up")]
    df = df[~df.appttype.str.contains("Labs")]
    df = df[~df.appttype.str.contains("Any 15")]
    df = df[~df.appttype.str.contains("Acute")]
    df = df[~df.appttype.str.contains("STI: Treatment Only")]
    df = df[~df.appttype.str.contains("Education Consult")]
    df = df[~df.appttype.str.contains("Vaccine")]

    return df


# run functions
df = get_appt_type(df)
df = cleanup(df)

# groupby appointment type
df = df.groupby("appttype").size().to_frame(name="count").reset_index()

# QA
print(df)

# keys
appointment_types = ["HIV Care", "HRT", "Hep C", "PEP", "PrEP", "STI Non-Primary", "STI Primary",
                     "Unspecified Telehealth", "Well Person"]
# create pie chart
plt.pie(df["count"], autopct="%0.1f%%", pctdistance=1.1, rotatelabels=True, colors=["xkcd:melon", "xkcd:pistachio",
                                                                                    "xkcd:pastel yellow", "xkcd:pale salmon",
                                                                                    "xkcd:soft blue", "xkcd:maize", "xkcd:pale lilac",
                                                                                    "xkcd:really light blue", "xkcd:dull teal"])
# label chart                                                                                    
plt.legend(appointment_types, loc="lower left", prop={"size":8}, bbox_to_anchor=[-0.36, 0.0])
plt.title("Clinic Patients by Appointment Type")
plt.show()
