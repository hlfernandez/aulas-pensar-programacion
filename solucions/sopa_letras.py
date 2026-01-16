import random as rnd

def imprimir(matriz):
    resultado = []
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            resultado.append(matriz[i][j])
            resultado.append(' ')
        resultado.append('\n')
    return ''.join(resultado)

def posicion_aleatoria(filas, columnas):
    fila = rnd.randint(0, filas - 1)
    columna = rnd.randint(0, columnas - 1)
    return fila, columna

def orientacion_aleatoria():
    if rnd.randint(0, 1) == 0:
        return 'v'
    else:
        return 'h'

def libres_fila(matriz, f, c):
    col_index = c
    libres = 0
    while col_index < len(matriz[f]) and matriz[f][col_index] == '-':
        libres+=1
        col_index+=1
    print('\t\t\t libres fila: ', libres)
    return libres

def libres_columna(matriz, f, c):
    fila_index = f
    libres = 0
    while fila_index < len(matriz) and matriz[fila_index][c] == '-':
        libres+=1
        fila_index+=1
    print('\t\t\t libres col: ', libres)    
    return libres

def sopa_letras(filas, columnas, palabras):
    matriz = []
    for fila in range(0, filas):
        matriz.append(['-'] * columnas)

    for p in palabras:
        colocada = False
        print('# ', p)
        while not colocada:
            f, c = posicion_aleatoria(filas, columnas)
            if matriz[f][c] == '-':
                print('Libre!')
                o = orientacion_aleatoria()
                if o == 'h':
                    print('\tHorizontal')
                    print('\t', p, len(p), f, c)
                    if len(p) <= libres_fila(matriz, f, c):
                        print('\t\t Hai sitio!')
                        col_index = c
                        for i in p:
                            matriz[f][col_index] = i
                            col_index+=1
                        colocada = True
                        print('# colocada ', p)
                else:
                    print('\tVertical')
                    print('\t', p, len(p), f, c)
                    if len(p) <= libres_columna(matriz, f, c):
                        print('\t\t Hai sitio!')
                        fila_index = f
                        for i in p:
                            matriz[fila_index][c] = i
                            fila_index+=1
                        colocada = True
                        print('# colocada ', p)


    return matriz


filas = 12
columnas = 12
palabras = ['ESEI', 'PROII', 'GRIA']
sopa = sopa_letras(filas, columnas, palabras)
print(imprimir(sopa))
