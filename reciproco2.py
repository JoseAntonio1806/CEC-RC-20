def reciproco(n):
    try:
        n=1/n
    except ZeroDivisionError:
        print("Division fallida")
        return None
    else:
        print("Todo salió bien")
    finally:
        print("Es el momento de decir adiós")
        return n
print(reciproco(2))
print(reciproco(0))