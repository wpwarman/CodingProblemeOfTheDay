print("12/27/2022 - Main Problem")

# inputArray = [3, 4, -1, 1, 3]
inputArray = [3, 4, -1, 2, 1, 9, -27, -2]
# inputArray = [1, 2, 0]
sortedInputArray = []
outputArray = []

# First sort the array using a count sort algorithm with an offset.
# Count sort is linear even in worse case and the space requirements are now
# from the beginning and don't change during implementation (and so consistant).

lowestValue = min(inputArray)
highestValue = max(inputArray)
numberOfSlotsNeeded = highestValue - lowestValue + 1
offset = 0

# calculate the offset
if lowestValue < 0:
    offset = abs(lowestValue)

# build the array of slots
for x in range(0, numberOfSlotsNeeded, 1):
    outputArray.insert(x, 0)

# adjust the input array for the offet
for x in inputArray:
    index = x + offset
    valueAtIndex = outputArray[index]
    outputArray[index] = valueAtIndex + 1

# sort the input array into the slots
for x in range(0, len(outputArray), 1):
    if outputArray[x] > 0:
        valueToInsert = x - offset
        for counter in range(0, outputArray[x], 1):
            sortedInputArray.append(valueToInsert)

# find the correct output value
outputValue = 1
for x in range(1, highestValue+1, 1):
    outputValue = x
    if x not in sortedInputArray:
        break
    outputValue = x + 1

print("input array: {0}".format(inputArray))
print("sorted input array: {0}".format(sortedInputArray))
print("output: {0}".format(outputValue))