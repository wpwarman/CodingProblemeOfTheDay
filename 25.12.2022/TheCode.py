print("12/25/20022 - Main Problem") 

#inputArray = [1, 2, 3, 4, 5]
inputArray = [7, 3, 11, 2, 14]
# inputArray = [1, 2, 3, 0, 4, 5]
# inputArray = [-1, 2, 3, -4, -5]
outputArray = []
product = 1

for x in inputArray:
    if x != 0:
        product = product * x

for x in inputArray:
    valueToAppend = 0
    if x == 0:
        valueToAppend = product
    elif 0 in inputArray: 
        valueToAppend = 0 
    else:
        valueToAppend = product/x
    outputArray.append(int(valueToAppend))

print("Input: {0}".format(inputArray))
print("Output: {0}".format(outputArray))
