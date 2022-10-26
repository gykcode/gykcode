num = [5, 7, 2, 3, 6, 9, 8, 0, 1, 4]

for i in range(len(num)):
    min_idx = i

    for j in range(len(num)):
        if num[j] < num[min_idx]:
            min_idx = j

    num[i], num[min_idx] = num[min_idx], num[i]
    print(num)

    num.sort()
    print(num)

