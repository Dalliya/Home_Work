#Два поезда движутся на скорости V1 и V2 навстречу друг другу. Между ними 10 км. пути. Через 4 км пути первый поезд может свернуть на запасной путь.
#При заданных скоростях узнать столкнутся ли поезда.

#def have_trains_crashed(v1, v2): # returns boolean value
#			pass


v1 = int(input("Введите скорость первого поезда:"))
v2 = int(input("Введите скорость второго поезда:"))


def have_trains_crashed(v1, v2):
    d = 10
    safe_trains = 4
    if v2 / v1 >= (d - safe_trains) / safe_trains:
        return True #Поезда столкнутся

    else: return False #Поезда не столкнутся

print(have_trains_crashed(v1, v2))