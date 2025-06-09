def moth_to_season(n):
    if n == 12 or n == 1 or n == 2:
        return "Зима"
    elif n == 3 or n == 4 or n == 5:
        return "Весна"
    elif n == 6 or n == 7 or n == 8:
        return "Лето"
    else:
        return "Осень"


n = int(input())
print(moth_to_season(n))
