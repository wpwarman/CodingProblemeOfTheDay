print("12/25/20022 - Follow Up") 

#inputArray = [1, 2, 3, 4, 5]
inputArray = [7, 3, 11, 2, 14]
# inputArray = [1, 2, 3, 0, 4, 5] - This code doesn't take care of this case.  It could be easily modified to do so along the lnes of the main solution.
# inputArray = [-1, 2, 3, -4, -5]
reversedInputArray = []
outputArray = []
product = 1

for x in range(len(inputArray)-1, -1, -1):
    product = product * inputArray[x]
    reversedInputArray.insert(0, product)

product = 1
for x in range(0, len(inputArray)-1, 1):
    valueToAppend = reversedInputArray[x+1] * product
    outputArray.append(valueToAppend)
    product = product * inputArray[x]
outputArray.append(product)





    #if x == 0:
    #    valueToAppend = product
    #elif 0 in inputArray: 
    #    valueToAppend = 0 
    #else:
    #    valueToAppend = product/x
    #outputArray.append(int(valueToAppend))

print("Input: {0}".format(inputArray))
print("Output: {0}".format(outputArray))
