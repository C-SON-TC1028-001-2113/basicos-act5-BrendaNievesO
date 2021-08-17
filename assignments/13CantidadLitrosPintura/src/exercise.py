import math
def main():
    #escribe tu código abajo de esta línea
    area=float(input('Area de la pared: '))
    redim=float(input('Redimiento (m2/l): '))
    litros=math.ceil(area/redim)
    print('La cantidad necesaria de litros a comprar: '+str(litros))


if __name__ == '__main__':
    main()
