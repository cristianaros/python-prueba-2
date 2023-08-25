def main():
    def es_primo(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    num = int(input("Ingrese un número: "))
    if es_primo(num):
        print(f"{num} es primo")
    else:
        print(f"{num} no es primo")

if __name__ == '__main__':
    main()