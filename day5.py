#task1
'''
patient={
    "name":"Ravi",
    "age":24,
    "test":"CBC"
}

patient["gender"]="Male"
patient["Result"]=25
#print(patient)
patient["age"]=30
patient["Result"]=45
#print(patient)
'''
'''
'#task2
patient={
    "name":"Ravi",
    "age":24,
    "test":"CBC"
}

for keys in patient:
    print(keys,patient[keys])

print(patient.get("name"))
print(patient.get("gender"))
print(patient.get("gender","not avaible"))

#task3
patient={
    "name":"Ravi",
    "age":24,
    "test":"CBC"
}

for key,value in patient.items():
    print(key,value)
'''

#task4

lab_results={
    "name":"Ravi",
    "age":25,
    "test":"CBC",
    "result":35,
    "status":"Normal"

}

if lab_results["result"] >=40:
    print("normal")
else:
    print("Low")


#for key,value in lab_results.items():
#    print(key,value)