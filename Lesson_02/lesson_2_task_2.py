def is_year_leap(x):
    if x % 4 == 0:
        return True
    else:
        return False


x = int(input())
print("Год " + str(x) + ":" + str(is_year_leap(x)))
