# Clinical Data Analysis
This project uses the following libraries.
* Numpy: `pip3 install numpy`
* Pandas: `pip3 install pandas`
* MatPlotLib: `pip3 install matplotlib`

## Demographic Data
### Patient Gender Breakdown by Race
![final gender breakdown by race](https://user-images.githubusercontent.com/65197541/138353056-d819745c-520b-4179-b912-27ee9a677ab5.png)

**Gender Types**
* Trans woman
* Trans man
* Cis woman
* Cis man
* Gender non-conforming

### Clinical Patients by Appointment Type
`demo_breakdown_viz.py` + `pts_2021.csv`
![patients_by_appt_type](https://user-images.githubusercontent.com/65197541/136875269-93a98c2d-8432-411b-ad3a-30e2c8828302.png)
**Appointment Types**
* "Any 15" - Any 15-minute appointment slot (This was the go-to appointment type.)
* "Hep C" - Any appointment to treat Hepatitis C, including lab draw appointments, lab review appointments, initial & follow-up provider visits
* "HIV Care" - Appointments to treat and manage HIV, including initial appointments, transfers, labs, and provider visits
* "HRT" - Gender care (esp. hormone therapy management) appointments
* "PEP" - Appointments to administer or follow-up on Post-Exposure Prophylaxis for prevention of HIV
* "STI Non-Primary Services" - Patients not utilizing regular PrEP services who wanted to get tested or treated for STIs
* "STI Primary Services" - Patients utilizing PrEP services wanting testing or treatment for STIs
* "Unspecified Telehealth" - Patients scheduled to be seen over the phone for any reason after the start of the pandemic 

### Telehealth Appointments Broken Down by Care Needs
`diagnosis_viz.py` + `patient_appts.csv`
![Telehealth Appointments by Care Needs](https://user-images.githubusercontent.com/65197541/134558140-9f55dc1c-19bd-4b00-8244-aaca216f0d5d.PNG)


The telehealth appointments at this clinic were not assigned using pre-determined options from the electronic health record system (EMR). Instead, when clinical staff scheduled appointments, the option 'Telehealth' was chosen as appointment type then the specific reason was added as a note.

* Initial data exploration showed a diversity of notation styles for each type of appointment
* The appointment types were parsed using string methods on the encompassing Pandas DataFrames

### Number of New Patients by Month vs Mask Requests
I began a campaign to distribute free COVID-19 face masks around Austin, Texas in late summer of 2020. We advertised along the local university's bus route, targeting folks under 33 (33 is Austin's average age). 
* The following graphs show a corresponding uptick in new patient enrollment for younger people under the age of 33.* 
* Our marketing campaign corresponds with an increase in younger patient enrollment up to 30%!*

**Number of COVID-19 Masks Requested by Month**
![final_masks_by_month](https://user-images.githubusercontent.com/65197541/136866089-4de5bd21-20f0-4b1c-b72b-7daac23d7331.png)

**Number of New Patients by Month**
![new_pt_by_month_merge](https://user-images.githubusercontent.com/65197541/136866095-1374a585-dcb4-4274-8f6f-b42a5a23e490.png)

**Percentage of New Patients by Age, by Month**

The percentage at the top of the graph indicates the percentage of newly enrolled patients under the age of 33 for that month.


![final_new_pt_by_month](https://user-images.githubusercontent.com/65197541/136866076-41bc2857-449e-41f7-89b6-87d80820d0ce.png)
