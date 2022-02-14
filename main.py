from encode import Encode
import math

#e = Encode()
#data = e.encode("tree.jpg")

data_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
first_data_list = []
second_data_list = []

#for char in str(data):
#    data_list.append(char)

for index in range(len(data_list)):
    if index % 2 == 0:
        first_data_list.append(data_list[index])

for index in range(len(data_list)):
    if index % 2 != 0:
        second_data_list.append(data_list[index])


total_encrypted_list = first_data_list + second_data_list
print(first_data_list)
print(second_data_list)
print(total_encrypted_list)



second_index = round(len(total_encrypted_list) / 2)
first_index = len(total_encrypted_list) - second_index

first_dehash_list = total_encrypted_list[:first_index]
second_dehash_list = total_encrypted_list[second_index+1:]

return_list = []

for a in total_encrypted_list:
    return_list.append("0")

print(return_list)

for ind in range(len(first_dehash_list)):
    if ind == 0:
        return_list.append(first_dehash_list[ind])
    else:
        return_list.insert(ind * 2 - 2, first_dehash_list[ind - 1])
counter = 1
for indy in range(len(second_dehash_list)-1):
    return_list.insert(indy + counter, second_dehash_list[indy])
    counter += 1



print(return_list)