import pandas as pd


import pandas as pd

data = {
    "Patient_ID": ["P001", "P002", "P003", "P004", "P005"],
    "Age": [24, 35, 42, 51, 29],
    "Gender": ["Male", "Female", "Male", "Female", "Male"],
    "Test_Names": ["CBC", "ESR", "CBC", "RFT", "ESR"],
    "Machine_Name": ["Yumizen H500", "ESR Analyzer", "Yumizen H500", "AU480", "ESR Analyzer"],
    "Parameter_Value": [13.2, 25, 11.8, 1.2, 18],
    "Result_Status": ["Normal", "High", "Normal", "Normal", "High"]
}

df = pd.DataFrame(data)

#print(df)


#step1 check number of columns and rows

print(df.shape)

#step2 get the column names

print(df.columns)

#step3 get the first few rows

print(df.head())


#step4 find the missing values in data

print(df.isnull())


#step5count the number of missing values

print(df.isnull().sum())


#step6 check the duplicates

print(df.duplicated())


#step7 count the number of duplicates

print(df.duplicated().sum())


#step7 filter the data 

#fetch the only cbc data

cbc_data=df[df["Test_Names"]=="CBC"]
print(cbc_data)

#fetch the esr data

esr_data=df[df["Test_Names"]=="ESR"]

print(esr_data)


#fetch the RFt data

rft_data=df[df["Test_Names"]=="RFT"]
print(rft_data)


#step8 fetch  cbc data  average pearameter_value
average_cbc=cbc_data["Parameter_Value"].mean()
print(f"average_cbc:{average_cbc}") 



#fetch the esr data avergae parameter value

average_esr=esr_data["Parameter_Value"].mean()
print(f"average_esr:{average_esr}")


#fetch the rft data avergae parameter value

average_rft=rft_data["Parameter_Value"].mean()
print(f"average_rft:{average_rft}")


#step9 get the the data by groupy of each and every test name average by individual using group by


average_bytests=df.groupby("Test_Names")["Parameter_Value"].mean()
print(average_bytests)

average_machines=df.groupby("Machine_Name")["Parameter_Value"].mean()
print(average_machines)


#step10 count the result_status

count_resultstatus=df["Result_Status"].value_counts()
print(count_resultstatus)


#step11 create a healthcare insights

#step1 count total records

total_records = len(df)
print(f"total_rcords:{total_records}")

#step2 calucluate the count of Normal value in result stsaus 

Normal_Count=(df["Result_Status"] == "Normal").sum()

print(f"count_Normal:{Normal_Count}")

#step3 calculate the percentage of normal value in total records

Normal_percentage=(Normal_Count / total_records) * 100
print(f"Normal_percentage:{Normal_percentage}")

#step12 create a healthcare insights

#step1 count total records

total_records = len(df)
print(f"total_rcords:{total_records}")

#step2 calucluate the count of HIGH value in result stsaus 

High_Count=(df["Result_Status"] == "High").sum()

print(f"count_High:{High_Count}")

#step3 calculate the percentage of normal value in total records

High_percentage=(High_Count / total_records) * 100
print(f"High_percentage:{High_percentage}")


#step 13 craete healthcare insights
print("------------------------------")
print("Healthcare_Insights")

print("-----------------------------")

print("Total records:", total_records)
print("Normal results:", Normal_Count)
print("Normal percentage:", Normal_percentage, "%")
print("High results:", High_Count)
print("High percentage:", High_percentage, "%")




#step14 count the toatal number of cbc status ==normal

cbc_normal = df[(df["Test_Names"] == "CBC") & (df["Result_Status"] == "Normal")]

print(cbc_normal)
print("CBC Normal count:", len(cbc_normal))