def unique_elements(lst):
    flat_list = []
    
    def flatten(current):
        for item in current:
            if isinstance(item, list):
                flatten(item)
            else:
                flat_list.append(item)
    
    flatten(lst)
    
    unique = []
    for n in flat_list:
        if flat_list.count(n) == 1 and n not in unique:
            unique.append(n)
    
    return unique

list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print(unique_elements(list_a)) 