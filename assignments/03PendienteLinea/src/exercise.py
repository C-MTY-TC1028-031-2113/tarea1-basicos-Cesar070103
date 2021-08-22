#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys

def main():
    x1 = float(input("Dame x1: "))
    y1 = float(input("Dame y1: "))
    x2 = float(input("Dame x2: "))
    y2 = float(input("Dame y2: "))
    pendiente = float((y2-y1)/(x2-x1))
    print("Pendiente: " + str(pendiente))

if __name__ == '__main__':
    main()
