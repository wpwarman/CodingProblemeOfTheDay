print("12/25/20022 - Temp") 

#inputArray = [1, 2, 3, 4, 5]
inputArray = [7, 3, 11, 2, 14]
# inputArray = [1, 2, 3, 0, 4, 5]
# inputArray = [-1, 2, 3, -4, -5]
reversedInputArray = []
outputArray = []
product = 1

for x in range(len(inputArray)-1, -1, -1):
    product = product * inputArray[x]
    reversedInputArray.insert(0, product)

print(reversedInputArray)

runningProduct = 1
for x in range(0, len(inputArray)-1, 1):
    valueToAppend = reversedInputArray[x+1] * runningProduct
    outputArray.append(valueToAppend)
    runningProduct = runningProduct * inputArray[x]
outputArray.append(runningProduct)





    #if x == 0:
    #    valueToAppend = product
    #elif 0 in inputArray: 
    #    valueToAppend = 0 
    #else:
    #    valueToAppend = product/x
    #outputArray.append(int(valueToAppend))

print("Input: {0}".format(inputArray))
print("Output: {0}".format(outputArray))
