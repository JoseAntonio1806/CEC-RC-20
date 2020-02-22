import pandas as pd
titulos = pd.read_csv('titles.csv' )
print(titulos.head(100))
print("\n"*2)
elenco = pd.read_csv('cast.csv', encoding='utf-8')
print(elenco.head(10))
#cuantas peliculas estan listadas
print(len(titulos))
print(titulos[titulos.title=="Romeo and Juliet"].sort_values("year").head(5))
print(titulos[titulos.title.str.contains("Batman")].sort_values("year"))
print(titulos[titulos.year.between(1980,2000)])
print(len( titulos[ (titulos.year >= 1980) & (titulos.year <= 2000)]))