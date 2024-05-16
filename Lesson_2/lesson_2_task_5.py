
def month_to_season(num):
    if num == 12 and 1 <= num < 3:
        print("Зима")
    if 3 <= num <= 5:
        print("Весна")
    if 3 <= num <= 5:
        print("Лето")
    if 9 <= num <= 11:
        print("Осень")
    else:
        print ("Введите число месяца (от 1 до 12)")

try:
    num = int(input("Введите число месяца: "))
    month_to_season(num)
except ValueError: 
    print("Это не число.")