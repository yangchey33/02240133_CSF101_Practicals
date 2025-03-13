#blackpink = ('lisa', 'rose', 'jennie', 'jisoo')
#newstack = []
#array_length = len(blackpink)

#for index in range(array_length):
   # temporarypopholder = blackpink.pop(0)
    #newstack.append(temporarypopholder)

    #print(blackpink)
    #print(newstack)

#first_list = [0,1,2,3,4,5,6,7,8,9]
#inverse_list = []
#array_length = len(first_list) 


#for index in range(array_length):
    #temporaryPopholder = first_list.pop()
    #inverse_list.append(temporaryPopholder)


    #print(inverse_list)


first_list = [0,1,2,3,4,5,6,7,8,9]
inverse_list = []

index = len(first_list)-1
while index >=0 :
    inverse_list.append(first_list.pop(index))
    index -=1

print(inverse_list)
print(first_list)

#another way

first_list = [0,1,2,3,4,5,6,7,8,9]
inverse_list = []

length_of_first_list = len(first_list)
index = 0

while index < length_of_first_list:
    inverse_list.append(first_list.pop())
    index += 1

print(first_list)
print(inverse_list)

#function

def multiplyfunction(firstnumber:int,secondnumber:int):
    product = firstnumber * secondnumber
    return product

firstnumber = 12
secondnumber = 13

print(multiplyfunction(firstnumber,secondnumber))

def squarefunction(element1:int):
    square = element1**3
    return square


print(squarefunction(2))

#set and tuple

new_tuple = (11, 12, 13, 14,12, "sonam")
print(len(new_tuple))

pythonset = {1,2,3,4,5,6,7}
print(pythonset)

var = {1,2,3,5,8,9,4,5}

sampleset = set(var)

diff = len(var) - len(sampleset)
print('there are',diff, 'duplicates')


