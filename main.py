from encode import Encode
import math

e = Encode()
data = e.encode("tree.jpg")

data_list = []
first_data_list = []
second_data_list = []

for char in str(data):
    data_list.append(char)

for index in range(len(data_list)):
    if index % 2 == 0:
        first_data_list.append(data_list[index])

for index in range(len(data_list)):
    if index % 2 != 0:
        second_data_list.append(data_list[index])

total_encrypted_list = first_data_list + second_data_list


print(len(second_data_list))
second_half_index_slice = math.trunc(len(total_encrypted_list) / 2)

first_half_index_slice = len(total_encrypted_list) - second_half_index_slice
