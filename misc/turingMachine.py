"""
While reading Melanie Mitchell's Complexity book, the
following Turing Machine was described. I thought it would
be a fun intuition check to rewrite it in Python.
"""
def chuggaChugga(string):
    evenOrOdd = 1
    zeroCounter = 0

    for i in string:
        if i == '0':
            zeroCounter += 1
            if zeroCounter == 2:
                break
        elif i == '1' and zeroCounter == 1:
            evenOrOdd *= -1
        
    return 'Even!' if evenOrOdd == 1 else 'Odd!'
    
string1 = '011110'
string2 = '010'
string3 = '01111110'
string4 = '101110'
string5 = '1011101'
string6 = '10110'
string7 = '101101'

print(chuggaChugga(string1))
print(chuggaChugga(string2))
print(chuggaChugga(string3))
print(chuggaChugga(string4))
print(chuggaChugga(string5))
print(chuggaChugga(string6))
print(chuggaChugga(string7))