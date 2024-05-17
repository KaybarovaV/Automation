def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False
year_23 = is_year_leap(2023)
year_24 = is_year_leap(2024)
print("Год 2023:", year_23)
print("Год 2024:", year_24)

