import numpy as np 
''''
ages=np.array([23,35,42,51,29])

print("addition",ages + 2)
print("subtraction",ages - 2)
print("multipilication",ages * 2)

#print(ages[0])
#print(ages[2])
#print(ages[-1])

'''



ages = np.array([23, 35, 42, 51, 29])

#print(f"average:{np.mean(ages)}")
#print(f"minimum:{np.min(ages)}")
#print(f"maximum:{np.max(ages)}")

#print(f"total:{np.sum(ages)}")

#print(f"number of patients:{len(ages)}")

#print("Shape:", ages.shape)

#print(f"datatype:{ages.dtype}")
#print("Add:", ages + 10)
#print("Subtract:", ages - 10)


#two dimensional array

patient_details=np.array([
    [23, 100],
    [35, 120],
    [42, 110],
    [51, 130]
])

#print(patient_details)
#print(f"shape {patient_details.shape}")

#indexing

#print(patient_details[0,0])
#print(patient_details[1,1])
#print(patient_details[2,0])

#print(patient_details[0])

#print(patient_details[:,1])

#print(f"number of patients {len(patient_details)}")
#print(f"shape{patient_details.shape}")
#print(f"Ages{patient_details[:,0]}")
#print(f"Values{patient_details[:,1]}")


print(f'average {np.mean(patient_details[:,1])}')