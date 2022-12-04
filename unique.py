nums=[1, 2, 5, 2, 5, 1, 3, 7, 9]
unique_nums=[]
for a in nums:
    if a not in unique_nums:
        unique_nums.append(a)
print(unique_nums)