#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys

def main():
    c1 = float(input("Calificación de la materia: "))
    c2 = float(input("Calificación de la materia: "))
    c3 = float(input("Calificación de la materia: "))
    c4 = float(input("Calificación de la materia: "))
    prom = float((c1+c2+c3+c4)/4)
    print("El promedio es: " + str(prom))

if __name__ == '__main__':
    main()