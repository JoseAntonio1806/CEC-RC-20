def readint(prompt, min, max):
#
# put your code here
#
    try:
        value=int(input(prompt))
        if value >= min and value <= max:
            return value
    except ValueError:
        print("Wrong input enter a number again")
        v = readint("Enter a number from -10 to 10: ", -10, 10)
    else:
        print("the value is not within permitted range({},{})".format(min,max))
        v = readint("Enter a number from -10 to 10: ", -10, 10)
    finally:
        print("Codigo acabado")

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
