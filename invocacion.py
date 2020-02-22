def hi(name):
    print("Hi, ", name)
hi("Jose")
hi("Andres")
hi("Pedro")
hi("Carlos")

def hiAll(name1, name2):
    print("Hi, ", name2)
    print("Hi, ", name1)
hiAll("Sebastian", "Ivan")

def address(street, city, postalcode):
    print("Your address is:", street, "St.", city, "with postal code", postalcode)
s = input("Street: ")
pC = input("Postal Cose: ")
c = input("City: ")
address(s,c,pC)

def subtra(a,b):
    print(a-b)
subtra(5,2)
subtra(2,5)

