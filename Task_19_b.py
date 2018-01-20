#Написать функцию для поиска разницы между максимальным и минимальным элементами списка.
#   ```def diff_min_max(lst): # returns int
#            pass```

#пользоваться ею так:
#           ```diff_min_max([32, 1, 44, 55, 10, 78, 5])```
#            должна вернуть 77


lst = [32, 1, 44, 55, 10, 78, 5]


def diff_min_max(lst):
    min_var = min(lst)
    max_var = max(lst)
    for i in range(min_var, max_var):
        diff = max_var - min_var
    return diff

print(diff_min_max(lst))




