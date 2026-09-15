import math
'''
print(math.sqrt(25))

print(math.ceil(4.2))
print(math.floor(4.8))


print(math.pi)

'''

#calculating circle area
'''
import math

radius=5

area=math.pi *radius * radius

print(area)

'''

#random module
'''
import random

#numbers=random.randint(1,10)
#print(numbers)

tests=["CBC","RFT","ESR","LFT"]

test=random.choice(tests)

print(test)
'''

#datetime
'''
import datetime

now=datetime.datetime.now().time()

today=datetime.date.today()
print(today)

print(now)

'''

import datetime

patient_name=input("enter a patient name:")
test_name=input("enter a test name:")

today=datetime.date.today()

print(f"patient{patient_name}")
print(f"Test {test_name}")
print(f"Todaydate{today}")

