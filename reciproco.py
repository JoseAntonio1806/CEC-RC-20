def reciproco(n):
    try:
        n=1/n
    except ZeroDivisionError:
        print("Division fallida")
        return None
    else:
        print("Todo salió bien")
        return n
print(reciproco(2))
print(reciproco(0))