def main():
    cesta = {}
    objeto = input("Introduce el artículo (o escribe 'fin' para terminar): ")
    while objeto != "fin":
        precio = float(input("Introduce el precio: "))
        cesta[objeto] = precio
        objeto = input("Introduce el artículo (o escribe 'fin' para terminar): ")

    print("Lista de la compra\n")
    total_costo = 0
    for objeto, precio in cesta.items():
        print(f"{objeto}         {precio}")
        total_costo += precio
    print(f"\nCoste total: {total_costo}")


if __name__ == '__main__':
    main()