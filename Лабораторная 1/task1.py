numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

cnt = 0
index = 0
for i in numbers:
    if i is not None:
        cnt += i
    else:
        index = numbers.index(i)


average = cnt/len(numbers)
numbers[index] = average

print("Измененный список:", numbers)
