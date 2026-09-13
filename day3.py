#for loop
'''
#task1

for i in range(6):
    print(i)
'''
'''
#task2

for i in range(10,60,10):
    print(i)
    '''
'''
#task3

for i in range(11,0,-1):
    print(i)
'''
#task4
'''
for i in range(1,6):
    print("patent",i)    
'''
#task5
'''
for i in range(1,6):
    print(F"Test {i} completed")
'''


#while loop

'''
i=1

while i <=5:
    print(i)
    i=i+1
'''

#break
'''
for i in range(1,10):
    if i ==5:
        break
    print(i)
'''

#continue
'''
for i in range(1,10):
    if i==3:
        continue
    print(i)
'''

#mini task
'''
for patient in range(1,4):
    for test in range(1,3):
        print(f"patient {patient} test {test}")
'''


for patient in range(1,6):
    for test in range(1,4):
        if test == 2:
            continue
        print(f"patient {patient} test {test}")