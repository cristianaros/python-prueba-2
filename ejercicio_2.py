def main():
    print("Menú")
    print("1. Convertir km a millas")
    print("2. Convertir millas a km")
    print("3. Convertir kg a libras")
    print("4. Convertir libras a kg")
    print("5. Convertir grados Celcius a grados Farenheit")
    print("6. Convertir grados Farenheit a grados Celcius")
    print("7. Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        km = float(input("Ingrese la cantidad de kilómetros: "))
        millas = km * 0.621
        print(f"{km} km son {millas} millas")

    elif opcion == "2":
        millas = float(input("Ingrese la cantidad de millas: "))
        km = millas * 1.609934
        print(f"{millas} millas son {km:} km")

    elif opcion == "3":
        libras = float(input("Ingrese la cantidad de libras: "))
        kg = libras * 0.453592
        print(f"{libras} libras son {kg} kg")
    
    elif opcion == "4":
        kg = float(input("Ingrese la cantidad de kg: "))
        libras = kg * 2.20462
        print(f"{kg} kg son {libras} libras")

    elif opcion == "5":
        celcius = float(input("Ingrese la cantidad de grados Celsius: "))
        farenheit = (celcius * 9/5) + 32
        print(f"{celcius} grados Celcius son {farenheit} grados Farenheit")

    elif opcion == "6":
        farenheit = float(input("Ingrese la cantidad de grados Farenheit: "))
        celcius = (farenheit - 32) * 5/9
        print(f"{farenheit} grados Farenheit son {celcius} grados Celcius")

    elif opcion == "7":
        print("Gracias por usar el programa")
    else:
        print("Opción inválida. Intente de nuevo.")
    
if __name__ == '__main__':
    main()