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


#step 1 sort patients by age


sorted_age=df.sort_values("Age")

print(sorted_age)



#step2 sort by parameter value

sorted_paravalue=df.sort_values("Parameter_Value")
print(sorted_paravalue)


#step  how many patients had tests

test_count=df["Test_Names"].value_counts()

print(f"test_count {test_count}")


#count patients by gender

gender_count=df["Gender"].value_counts()

print(gender_count)


#by using group by calacualte the avg parameter of genders

gender_avg=df.groupby("Gender")["Parameter_Value"].mean()

print(gender_avg)


#find patients who are greate than age 40 and status is normal


patients_record=df[(df["Age"] > 40) & (df["Result_Status"] == "Normal")]

print(patients_record)


def age_group(age):
    if age <= 30:
        return "Young"
    elif age <= 50:
        return "Adult"
    else:
        return "Senior"

df["Age_Group"] = df["Age"].apply(age_group)

print(df[["Patient_ID", "Age", "Age_Group"]])



#count age group count


count_agegroup=df["Age_Group"].value_counts()

print(count_agegroup)


#hihest value in age group

highest_value=df["Age_Group"].value_counts().idxmax()

print(highest_value)


high_by_age = df[df["Result_Status"] == "High"].groupby("Age_Group")["Patient_ID"].count()

print(high_by_age)