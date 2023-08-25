def main():
    def es_palindromo(palabra):
        if len(palabra) < 3:
            return False
        palabra = palabra.lower()
        palabra_sin_espacios = "".join(palabra.split())
        #palabra_sin_espacios[::-1] se inviierte la palabra
        if(palabra_sin_espacios == palabra_sin_espacios[::-1]):#se verifica si la palabra es igual a la normal
            return True
        else:
            return False
    
    palabra = input("Introduce una palabra: ")
    if es_palindromo(palabra):
        print("La palabra es un palíndromo")
    else:
        print("La palabra no es un palíndromo")

if __name__ == '__main__':
    main()