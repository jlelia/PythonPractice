# Unfinished, PEMDAS
# Please excuse my disgraceful attrocious script
# Exercise 33: Comma-Formatted Numbers
def decimal(string):
    string = str(string)
    if ',' in string:
        return True
    else:
        return False

def chop(string):
    string = str(string)
    array = []
    for i in range(len(string)):
        array.append(string[i])
    return array


def commaFormat(number):
    if number < 1000:
        return str(number)
    
    number = str(number)
    
    if '.' in number:
        splitString = number[:number.index('.')], number[number.index('.'):]
        
        return splitString
    array = chop(number)
   # if decimal(array):

    



print(commaFormat(1))
print(commaFormat(10))
print(commaFormat(100))
print(commaFormat(1000))
print(commaFormat(10000))
print(commaFormat(100000))
print(commaFormat(1000000))
print(commaFormat(1234567890))
print(commaFormat(1000.123456))

# assert commaFormat(1) == '1'
# assert commaFormat(10) == '10'
# assert commaFormat(100) == '100'
# assert commaFormat(1000) == '1,000'
# assert commaFormat(10000) == '10,000'
# assert commaFormat(100000) == '100,000'
# assert commaFormat(1000000) == '1,000,000'
# assert commaFormat(1234567890) == '1,234,567,890'
# assert commaFormat(1000.123456) == '1,000.123456'