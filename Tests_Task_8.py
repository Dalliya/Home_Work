#В одномерном списке поменять местами минимальный и максимальный элементы.Остальные оставить на своих местах.

lst = [15, 7, 10, 68, 12, 99, 108]

def reverse_min_max(lst):
    min_var = min(lst)
    print(min_var)
    max_var = max(lst)
    print(max_var)

    lst[lst.index(max(lst))], lst[lst.index(min(lst))] = lst[lst.index(min(lst))], lst[lst.index(max(lst))]
    return lst

print(reverse_min_max(lst))






