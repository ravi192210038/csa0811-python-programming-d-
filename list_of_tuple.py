my_list = [45,46,47,48,49]
print("The list is ")
print(my_list)
print("The resultant tuple is :")
my_result = [(val, pow(val, 2)) for val in my_list]
print(my_result)
