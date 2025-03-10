
newArray = ["IT", "ECE", "SWE", "WRE", "MCM", "ME", "EE", "A" , "ICE", "MRE"]

newArraylen = len(newArray)
new_array = []

for index in range(newArraylen):
    elements = newArray[index]
    new_array.append(elements.lower())
for secondindex in range(len(new_array)):
    print(new_array[secondindex])
