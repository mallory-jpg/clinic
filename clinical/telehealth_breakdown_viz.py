"""
Pie chart breakdown of telehealth appointments using appointment notes
"""

import pandas as pd
from matplotlib import rc
import matplotlib.pyplot as plt


rc("font", **{"family":"serif", "serif":["Times"]})
pd.options.mode.chained_assignment = None
pd.set_option("display.max_colwidth", None)

# read csv to DF
df = pd.read_csv("telehealth_appts.csv")
# print(telehealth.head())

def telehealth(df):
    """
    Parse out appointment instances that are telehealth, or over the phone.
    :param df: Pandas DataFrame of patient appointment data
    :returns unspec_list: list of appointments that are specified using appointment notes, rather than the pre-determined EMR system options
    :returns specified: list of appointments that are specified using the pre-determined EMR options
    """

    th_specified = df[df["apptnote"].str.contains("TH")]
    unspecified = df[~df["apptnote"].str.contains("TH")]
    # print(unspecified.apptnote.unique())

    th_specified["appt_type"] = th_specified["apptnote"].str.split("TH").str[-1]
    # reformat values for column using unnamed lambda function
    th_specified["appt_type"] = th_specified["appt_type"].apply(lambda x: x.split("||")[0])
    # print(th_specified.appt_type.unique())

    # only include apptnote's with appointment types
    u_appts = unspecified[unspecified["apptnote"].str.contains("f/u|FOLLOW UP|follow up|UP|PrEP|STI|sti|prep|pep|Prep|hrt|hiv"
                                                            "|HRT|STI-|PeP|PEP|HIV|HEP C|Hep")]
    # apptnote to list
    unspec_list = u_appts["apptnote"].tolist()
    specified = th_specified["appt_type"].tolist()
    #print(specified)

    return unspec_list, specified

def get_totals(unspec_list, specified):
    """
    Get totals for telehealth appointment types.
    :param unspec_list: list of telehealth appointments that are not specified
    :param specified: list of telehealth appointments that have been specified in appointment notes
    :returns unspecified_th: a list of the totals for each type of telehealth appointment 
    """
    hiv = sum("hiv" in i for i in unspec_list and specified) + sum("HIV" in i for i in unspec_list and specified)
    sti = sum("sti" in i for i in unspec_list and specified) + sum("STI" in i for i in unspec_list and specified)
    prep = sum("prep" in i for i in unspec_list and specified) + sum("Prep" in i for i in unspec_list and specified) + sum("PrEP" in i for i in unspec_list and specified)
    pep = sum("pep" in i for i in unspec_list and specified) + sum("PeP" in i for i in unspec_list and specified) + sum("PEP" in i for i in unspec_list and specified)
    hrt = sum("hrt" in i for i in unspec_list and specified) + sum("HRT" in i for i in unspec_list and specified)
    hepc = sum("hep" in i for i in unspec_list and specified) + sum("HEP" in i for i in unspec_list and specified) + sum("Hep" in i for i in unspec_list and specified)

    unspecified_th = [hiv, sti, prep, pep, hrt, hepc]
    
    return unspecified_th


# unpack tuples returned by functions
u,s = telehealth(df)
totals = get_totals(u,s)

# chart keys
diagnoses = ["HIV", "STI-Non Primary", "PrEP", "PEP", "HRT", "Hep C"]

# create pie chart
plt.pie(totals, autopct="%0.1f%%", pctdistance=1.1, rotatelabels=True, colors=["xkcd:melon", "xkcd:pistachio",
                                                                                    "xkcd:pastel yellow", "xkcd:pale salmon",
                                                                                    "xkcd:soft blue", "xkcd:pale lilac"])
plt.legend(diagnoses, loc="lower left", prop={"size":8}, bbox_to_anchor=[-0.36, 0.0])
plt.title("Telehealth Appointments by Care Needs")
plt.show()
