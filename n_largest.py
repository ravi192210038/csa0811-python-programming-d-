def N_max_elements(list, N):
    result_list = []
    for i in range(0, N): 
        maximum = 0
        for j in range(len(list)):     
            if list[j] > maximum:
                maximum = list[j]      
        list.remove(maximum)
        result_list.append(maximum)
    return result_list
list1 = [14,67,48,23,5,62]
N = 1
print(N, "max elements in ",list1)
print(N_max_elements(list1, N))
