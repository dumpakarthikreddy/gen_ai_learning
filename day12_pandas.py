import pandas as pd 

#print(pd.__version__)


#creating data frame

patients_data={
    "names":["Ravi","sita","arun"],
    "ages":[23,24,35],
    "tests":["CBC","RFT","ESR"],
    "result":[23,43,32]

}

df=pd.DataFrame(patients_data)

#head() its shows first few rows of the data
#print(df.head())


#we need single column in data
#print(df["ages"])


#we need one or more columns ata time

#print(df[["names","tests"]])


#shape

#print(f'shape{df.shape}')

#columns

#print(df.columns)

#get basic informaton about the data

#print(df.info())


#statical summary

#print(df.describe())


#we can see a specific information of row we use loc

#print(df.loc[0])

#print(df.iloc[1])

#print only age greater than 23

#print(df[df["ages"] > 23])

#print(df[df["result"] > 30])

#using & operator

#print(df[(df["ages"] > 23 ) & (df["result"] > 30)])


#sorting data

#print(df.sort_values("result"))

#sorting=df.sort_values("result",ascending=False)
#print(sorting)


#print(df[df["tests"] == "CBC"])

#(df["tests"] == "CBC") | (df["tests"] == "RFT")

#print(df[(df["tests"] == "CBC") | (df["tests"] == "RFT")])


data = {
    "names": ["Ravi", "sita", "arun", "kiran"],
    "ages": [23, 24, None, 30],
    "tests": ["CBC", "RFT", "ESR", None],
    "result": [23, 43, 32, None]
}

df2 = pd.DataFrame(data)

#print(df2)


#print(df2.isnull())
#print(df2.isnull().sum())

#df_clean = df2.dropna()

#df_filled=df2.copy()

#df_filled["ages"]=df_filled["ages"].fillna(0)

#print(df_filled)


#mean_age=df2["ages"].mean()
#print(mean_age)


df_filled2=df2.copy()

mean_age=df_filled2["ages"].mean()

df_filled2["ages"]=df_filled2["ages"].fillna(mean_age)

df_filled2["tests"]=df_filled2["tests"].fillna("NOt mentioned")

mean_result=df_filled2["result"].mean()
#print(mean_result)

df_filled2["result"]=df_filled2["result"].fillna(mean_result)



#print(df_filled2)

#df_dup = pd.concat([df2, df2.iloc[[0]]], ignore_index=True)

#print(df_dup)




#print(df_dup.duplicated())

#print(df_dup.drop_duplicates())


#rint(df2["tests"].value_counts())

#groupby

#print(df2.groupby("tests")["result"].mean())


#mutiple regression cal min ,max mean ata a time

#print(df2.groupby("tests")["result"].agg(["mean","max","min"]))



#count test names

#print(df2.groupby("tests")["names"].count())


#create csv file

df2.to_csv("patients.csv", index=False)

print("CSV file created successfully")


df_csv = pd.read_csv("patients.csv")

#print(df_csv)

print(df_csv.shape)


print(df_csv.columns)

print(df_csv["result"].mean())