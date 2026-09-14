#task1

#creating a list
'''
Test=["CBC",
"ESR",
"LFT",
"KFT"]
#print(Test[0])
#print(Test[-1])

#Test.append("Kft")
#Test.remove("ESR")
Test[1]="HbA1c"
print(Test)

'''
'''
Test=["CBC", "ESR", "LFT", "KFT", "HbA1c"]
for test in Test:
    print(test)
'''

'''
tests = ["CBC", "ESR", "LFT", "KFT"]

for _ in tests:
    print(f"{_} test completed")
'''
'''
tests = ["CBC", "ESR", "LFT", "KFT"]

if "HbA1c" in tests:
        print("Hb1ac is availble")
else:
        print("Hb1ac is Not availble")
'''
'''
#print only if t letter is present:
tests = ["CBC", "ESR", "LFT", "KFT", "HbA1c"]

for test in tests:
    if  "T" in test:
        print(test)
'''
'''
results = [25, 45, 60, 30, 80]

for result in results:
    if result >= 40:
        print(result)
'''

'''
#tuples

tests = ("CBC", "ESR", "LFT")
tests[1] = "KFT"
print(tests)

#print(tests[0])
#print(tests[-1])

'''

#sets
''''
tests = {"CBC", "ESR", "LFT"}
tests.add("KFT")
print(tests)
'''

tests = ["CBC", "ESR", "CBC", "LFT", "ESR", "KFT"]

unique_set=set(tests)
print(unique_set)