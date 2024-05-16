def month_to_season(a):
    if a == 1 or a == 2 or a ==12:
        return ("Зима")
    elif a == 3 or a == 4 or a == 5:
        return ("Весна")
    elif a == 6 or a == 7 or a == 8:
        return ("Лето")
    elif a == 9 or a == 10 or a == 11:
        return ("Осень")
    else:
        return ("Error! Введите число от 1 до 12")
month = (input("Введите число от 1 до 12: "))
month = int(month)
print(month_to_season(month))