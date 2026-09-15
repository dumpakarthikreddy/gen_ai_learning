#file handling

#write mode "w"
'''
file=open("python.text","w")

file.write("patient_name:Ravi")
file.write("\n age:23")
file.write("\n test:CBC")

file.close()


'''
#read mode "r"
'''
file=open("python.text","r")
data=file.read()
print(data)
file.close()

'''


#instead ot writing manually file.close() we can with 
'''
with open("python.text","r") as file:

    data=file.read()
print(data)

'''

'''
#append add something on the existing file

with open("python.text","a") as file:
    file.write("\n result:Normal")


with open("python.text","r") as file:
    data=file.read()
print(data)

'''


#exception handling
'''
try:
    age=int(input("enter a age:"))
    if age >= 18:
        print("Adult Patient")
    else:
        print("minor patient")

except ValueError:
    print("enter a valid numbers only")

'''

'''
patient_name = input("Enter patient name: ")
age = input("Enter patient age: ")
test = input("Enter test name: ")


with open("python.text1","w") as file:

    file.write(f"Patient Name:{patient_name}\n")
    file.write(f"Age:{age}\n")
    file.write(f"Test:{test}\n")

'''

with open("python.text1","r") as file:
    data=file.read()

print(data)



