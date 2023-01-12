year=input("Ingrese el año que desea evaluar, ejemplo 1998: ")
try:
    year = int(year)
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print('El año',year, "es bisiesto.")
    else:
        print('El año',year, "no es bisiesto.")    

except:
    print('No ingreso un valor valido')
    exit()