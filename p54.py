#heck Whether All Dictionary Values Are Same (Using Lambda)
check_same_values = lambda d: len(set(d.values())) == 1

# Example
my_dict = {"a": 10, "b": 10, "c": 10}
print(check_same_values(my_dict))   # True