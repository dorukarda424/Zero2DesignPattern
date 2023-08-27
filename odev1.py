
num_list = [100, 1, 43, 5, 12, 32, 54, 20, 12, 3]
temp_list = num_list.copy()
sorted_list = []
count = 0
while count < len(num_list):
    min_num=0
    for j in range(0,len(temp_list)):  
        if min_num == 0:
            min_num = temp_list[j]
        elif temp_list[j] < min_num:
            min_num = temp_list[j]
    sorted_list.append(min_num)
    temp_list.pop(temp_list.index(min_num))
    count+=1
print(sorted_list)
