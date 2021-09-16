""" Graphing based on diagnoses; HIV, PrEP/PEP, HepC, STI only"""

import pandas as pd
from matplotlib import rc
import matplotlib.pyplot as plt

rc("font", **{"family":"serif", "serif":["Times"]})

appointments = pd.read_csv("patient_appts.csv")
total_appts = 7803
# print(appointments.head())

df = pd.DataFrame(appointments)
# print(df.appttype.unique())

# consolidate appointment types
df["appttype"] = df["appttype"].replace(to_replace=["ANY 15", "Any", "FOLLOW UP 15"], value="Any 15")
df["appttype"] = df["appttype"].replace(to_replace=["HCV: 4 Week Therapy Labs", "HCV: Lab Review with Client",
                                                    "Hep C: F/U Labs Only", "Hep C: F/U Labs and Provider",
                                                    "Hep C: Initial Labs Only", "Hep C: Rx (No Labs)"], value="Hep C")
df["appttype"] = df["appttype"].replace(to_replace=["HIV: F/U Labs and Provider", "HIV: Initial (New Care)",
                                                    "HIV: Initial (Transfer)", "HIV: Lab review with Client",
                                                    "HIV: Labs Only (No Provider)", "HIV: Provider F/U (No Labs)",
                                                    "HIV: Restart"], value= "HIV Care")
df["appttype"] = df["appttype"].replace(to_replace=["HRT: Follow Up", "HRT: Initial"], value="HRT")
df["appttype"] = df["appttype"].replace(to_replace=["PEP: 2 PrEP", "PEP: A/R (Assault/Rape)", "PEP: Follow Up",
                                                    "PEP: Initial (Existing)", "PEP: Initial (New to Care)",
                                                    "PEP: Labs"], value="PEP")
df["appttype"] = df["appttype"].replace(to_replace=["PrEP Rx", "PrEP: 1 Month", "PrEP: 2 PEP", "PrEP: 3 Month",
                                                    "PrEP: 6 Month", "PrEP: Follow Up", "PrEP: Initial (New to Care)",
                                                    "PrEP: Initial (Transfer)", "PrEP: L/C F/U", "PrEP: L/C Initial (New)",
                                                    "PrEP: Labs", "PrEP: Restart", "Outreach: PrEP",
                                                    "Prep: L/C Initial (Transfer)"], value="PrEP")
df["appttype"] = df["appttype"].replace(to_replace=["STI: Non Primary Services", "STI: Symptomatic", "Outreach: Testing"],
                                        value="STI Non-Primary Services")
df["appttype"] = df["appttype"].replace(to_replace=["STI: PrEP", "STI: Labs and Treatment", "STI: Testing/Labs"],
                                        value="STI Primary Services")
df["appttype"] = df["appttype"].replace(to_replace=["TeleHealth Appointment"], value="Unspecified Telehealth")

# deleting unused columns
del df["apptdate"]
del df["patientid"]

df = df.groupby("appttype").size().to_frame(name="count").reset_index()
# print(df)

# deleting unnecessary rows
df = df[~df.appttype.str.contains("Medication Pick Up")]
df = df[~df.appttype.str.contains("Labs")]
df = df[~df.appttype.str.contains("Any 15")]
df = df[~df.appttype.str.contains("Acute")]
df = df[~df.appttype.str.contains("STI: Treatment Only")]
df = df[~df.appttype.str.contains("Education Consult")]
df = df[~df.appttype.str.contains("Vaccine")]

print(df)

appointment_types = ["HIV Care", "HRT", "Hep C", "PEP", "PrEP", "STI Non-Primary", "STI Primary",
                     "Unspecified Telehealth", "Well Person"]

plt.pie(df["count"], autopct="%0.1f%%", pctdistance=1.1, rotatelabels=True, colors=["xkcd:melon", "xkcd:pistachio",
                                                                                    "xkcd:pastel yellow", "xkcd:pale salmon",
                                                                                    "xkcd:soft blue", "xkcd:maize", "xkcd:pale lilac",
                                                                                    "xkcd:really light blue", "xkcd:dull teal"])
plt.legend(appointment_types, loc="lower left", prop={"size":8}, bbox_to_anchor=[-0.36, 0.0])
plt.title("ASHwell Patients by Appointment Type")
plt.show()
