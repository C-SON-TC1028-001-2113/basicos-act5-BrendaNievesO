import math
def main():
    #escribe tu código abajo de esta línea
    alt=float(input('Altura de la casa: '))
    ang=float(input('Angulo en grados: '))
    escalera=round(alt/math.sin(math.radians(ang)))
    print('Largo de la escalera: '+str(escalera))

if __name__ == '__main__':
    main()
