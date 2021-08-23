def main():
    costocheque = 13
    interes = 0.075
    saldomesanterior = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = float(input("Dame el número de cheques: "))
    saldofinal1 = float((saldomesanterior + ingresos - egresos) - (costocheque * cheques))
    saldofinal2 = saldofinal1 - (saldofinal1*interes)
    print("El saldo final de la cuenta es: " + str(saldofinal2))

if __name__ == '__main__':
    main()
