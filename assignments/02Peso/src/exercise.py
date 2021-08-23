def main():
    pesoinicial = float(input("Dame el peso inicial: "))
    pesofinal = float(input("Dame el peso final: "))
    meses = int(input("Dame la cantidad de meses: "))
    kilospormes = float((pesoinicial - pesofinal) / meses)
    print("Lo que debes bajar por mes es: " + str(kilospormes))

if __name__ == '__main__':
    main()
