#functions
'''
def greet():
    print("Hello Karthik")

greet()

#function with input parameter

def greet(name):
    print("Hello",name)
greet("Karthik")
greet("Ravi")
greet("Abhi")



#function with two parameters

def patient_info(name,age):
    print("name",name)
    print("age",age)
patient_info("Karthik",24)

#using return statement
def yearly_sal(monthly):
    return(monthly * 12)
print(yearly_sal(20000))


def add(a,b):
    return a + b
result=add(10,20)
print(result)


def check_labresult(result):
    if result >=40:
        return "Normal"
    else:
        return "Low"
status=check_labresult(30)
print(status)
    '''

def check_result(patient):
    if patient["result"] >= 40:
        return "Normal"
    else:
        return "Low"
patient = {
    "name": "Ravi",
    "age": 25,
    "result": 35
}

print(check_result(patient))