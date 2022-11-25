#선택정렬-오름차순

data = [32,11,5,6,8,10]
temp = 0

for i in range(len(data)):
    min_index = i
    for j in range(i,len(data)):
        if data[min_index] > data[j]:
            min_index = j
        temp = data[i]
        data[i] = data[min_index]
        data[min_index] = temp
        print(data)

print(data)