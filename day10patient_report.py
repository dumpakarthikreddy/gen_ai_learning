patient_name = input("Enter patient name: ")

try:
    age = int(input("Enter patient age: "))
    result = float(input("Enter test result: "))
except ValueError:
    print("enter the numbers only for age and result")
    exit()
test_name = input("Enter test name: ")

def check_result(result):
    if result >= 40:
        return "Normal"
    else:
        return "Low"
status=check_result(result)


patient = {
    "name": patient_name,
    "age": age,
    "test": test_name,
    "result": result,
    "status": status
}

print(patient)


with open("reports.txt", "w") as file:
    file.write(f"Patient Name: {patient['name']}\n")
    file.write(f"Age: {patient['age']}\n")
    file.write(f"Test: {patient['test']}\n")
    file.write(f"Result: {patient['result']}\n")
    file.write(f"Status: {patient['status']}\n")

with open("reports.txt", "r") as file:
    report = file.read()

print(report)
