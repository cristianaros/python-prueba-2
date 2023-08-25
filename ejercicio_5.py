def main():
    def contar_letra(palabra, letra):
        contador = 0
        for caracter in palabra:
            if caracter == letra:
                contador += 1
        return contador

    palabra = input("Ingresa una palabra: ")
    letra = input("Ingresa una letra: ")

    resultado = contar_letra(palabra, letra)
    print(f"La letra '{letra}' aparece {resultado} veces en la palabra '{palabra}'")

if __name__ == '__main__':
    main()