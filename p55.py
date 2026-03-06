#Create Two Lists and Generate Dictionary
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

result_dict = {}

for i in range(len(list1)):
    result_dict[list1[i]] = list2[i]

print(result_dict)