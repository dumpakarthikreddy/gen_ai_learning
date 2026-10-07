#check matplotlib is working or not


import pandas as pd

import matplotlib.pyplot as plt

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

"""

plt.plot(df["Patient_ID"],df["Age"])

plt.xlabel("patient_id")
plt.ylabel("age")
plt.title("Patient Age")
plt.show()

"""

#count the result status 

#result_count=df["Result_Status"].value_counts()

'''
plt.bar(result_count.index,result_count.values)
plt.xlabel("Result Status")
plt.ylabel("No of Patients")
plt.title("Result Status Table")
plt.show()
'''

'''
plt.pie(
    result_count.values,
    labels=result_count.index,
    autopct="%1.1f%%"
)

plt.title("Patient Result Status Distribution")

plt.show()

'''

''''
#caluclate the number of  patients using test count

test_count=df["Test_Names"].value_counts()

plt.Figure(figsize=(8,5))

bars=plt.bar(test_count.index,
        test_count.values,
        color=["blue","green","orange"]
        )
plt.xlabel("Name of the test")
plt.ylabel("NO of patients")
plt.title("Patient By Lab Test")

for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2,
    bar.get_height(),
    str(bar.get_height()),
    ha="center",
    va="bottom")

plt.show()


'''

''''
#crete a line chart using patient age

plt.figure(figsize=(8,5))

lines=plt.plot(df["Patient_ID"],
                df["Age"],
                marker="o")
plt.xlabel("patient id")
plt.ylabel("age")

plt.title("No Of Patients age")

plt.show()

'''

#create scatter plot using two values and add patients ids to the dot
'''
plt.figure(figsize=(8,5))

plt.scatter(df["Age"],
            df["Parameter_Value"],
            s=100) 

plt.xlabel("age")
plt.ylabel("parameter value")

for i in range(len(df)):
        plt.text(
                df["Age"][i],
                df["Parameter_Value"][i],
                df["Patient_ID"][i]
        )
                 



plt.show()
'''

'''
plt.figure(figsize=(8, 5))

counts, bins, patches = plt.hist(
    df["Age"],
    bins=8,
    edgecolor="black"
)

for i in range(len(counts)):
    plt.text(
        (bins[i] + bins[i + 1]) / 2,
        counts[i],
        str(int(counts[i])),
        ha="center",
        va="bottom"
    )

plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.title("Patient Age Distribution")
plt.grid(axis="y")
plt.show()

'''


status_count = df["Result_Status"].value_counts()

plt.figure(figsize=(8, 5))

bars = plt.bar(
    status_count.index,
    status_count.values,
    edgecolor="black"
)

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        str(int(bar.get_height())),
        ha="center",
        va="bottom"
    )

plt.xlabel("Result Status")
plt.ylabel("Number of Patients")
plt.title("Patient Result Status")

plt.show()