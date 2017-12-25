name_date = input()

lst = name_date.split('*')

birth = lst[1].split('-')
death = lst[2].split('-')

print(lst[0], ',', int(death[0]) - int(birth[0]))













