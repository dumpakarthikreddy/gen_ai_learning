import pandas as pd

data = {
    "Patient_ID": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008"],
    "Age": [24, 35, 42, 51, 29, 46, 33, 58],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "Test_Names": ["CBC", "ESR", "CBC", "RFT", "ESR", "CBC", "RFT", "CBC"],
    "Machine_Name": [
        "Yumizen H500",
        "ESR Analyzer",
        "Yumizen H500",
        "AU480",
        "ESR Analyzer",
        "Yumizen H500",
        "AU480",
        "Yumizen H500"
    ],
    "Parameter_Value": [13.2, 25.0, 11.8, 1.2, 18.0, 14.1, 1.5, 10.9],
    "Result_Status": ["Normal", "High", "Normal", "Normal", "High", "Normal", "High", "Low"]
}

df = pd.DataFrame(data)

print(df)


#print the above 40 years age oof patients

above_40=df[df["Age"] > 40]
print(above_40)

print(f"above_40:{above_40}")

print(f"count of above 40 age:{len(above_40)}")


high_results = df[df["Result_Status"] == "High"]

print(high_results)
print("High result count:", len(high_results))


high_above_30 = df[
    (df["Result_Status"] == "High") &
    (df["Age"] > 30)
]

print(high_above_30)
print("High results above age 30:", len(high_above_30))




#find avrage parameter value for cbc

cbc_data=df[df["Test_Names"] == "CBC"]

average_cbc=cbc_data["Parameter_Value"].mean()

print(cbc_data)
print(f"average parameter value{average_cbc}")


#find the average for each test


average_by_test=df.groupby("Test_Names")["Parameter_Value"].mean()

print(average_by_test)


#find the average machine parameter value


average_by_machine=df.groupby("Machine_Name")["Parameter_Value"].mean()


print(average_by_machine)

print(f"highest average machine parameter value{max(average_by_machine)}")



#count each result status count


status_count=df["Result_Status"].value_counts()

print(status_count)


normal_count=(df["Result_Status"] == "Normal").sum()
total_patients=len(df)

normal_percentage=(normal_count / total_patients) * 100

print(f"normal percentage {normal_percentage} %")



#find the oldest patient

oldest_patient=df.loc[df["Age"].idxmax()] #loc gets the all patient details and idxmax get the highest age persons 

print(oldest_patient)


#find the youngest patient

youngest_patient=df.loc[df["Age"].idxmin()] #loc gets the all patient details and idxmax get the highest age persons 

print(youngest_patient)


#find the highest parameter value 

high_para=df.loc[df["Parameter_Value"].idxmax()] #loc gets the all patient details and idxmax get the highest age persons 

print(high_para)



#find the lowest parameter value

lowest_para=df.loc[df["Parameter_Value"].idxmin()] #loc gets the all patient details and idxmax get the highest age persons 

print(lowest_para)


#find how many females are pattients and status is normal

female_normal=df[(df["Gender"] == "Female") & (df["Result_Status"] == "Normal")]

print(female_normal)
print(f"count of normal count {len(female_normal)}")