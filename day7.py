#strings 

#indexing

"""
name="karthik"
print(name[0])
print(name[3])
print(name[-1])
"""

#sliceing
"""
name="karthik"
print(name[0:4])
print(name[2:6])

"""

#string methoods
"""
test="cBc"
print(test.upper())
print(test.lower())

"""

#strip it removes the space fromthe starting and ending of the string
"""
test=" CBC "
print(test)
print(test.strip())

"""

#replace
'''
test="CBC"
new_test=test.replace("CBC","LFT")
print(test)
print(new_test)
'''

#split break a string into separate pieces
'''
tests="CBC LFT ESR"
print(tests.split())
'''

#join
'''
tests=['CBC', 'LFT', 'ESR']

result="-".join(tests)
print(result)

'''

#length function
'''
test="CBC"
print(len(test))
'''


test="  cbc report"

test=test.upper()
test=test.strip()

print(test)
print(len(test))


