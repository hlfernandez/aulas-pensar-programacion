# https://www.unitjuggler.com/memory-convertir-MiB-a-B.html?val=9
# https://www.lenovo.com/es/es/glossary/kilobyte/index.html

def separar(valor):
    valor = valor.replace(" ", "")
    numero = ""
    indice = 0
    while indice < len(valor) and valor[indice].isdigit():
        numero += valor[indice]
        indice+=1
    
    return int(numero), valor[indice:]

def kb_a_bytes(valor):
    return valor * (2 ** 10)

def mb_a_bytes(valor):
    return valor * (2 ** 20)

def gb_a_bytes(valor):
    return valor * (2 ** 30)

def a_bytes(valor, unidades):
    match unidades:
        case 'B':
            return valor
        case 'KiB':
            return kb_a_bytes(valor)
        case 'MiB':
            return mb_a_bytes(valor)
        case 'GiB':
            return gb_a_bytes(valor)

def comparar_unidades(valor1, valor2):
    valor1_numero, valor1_unidades = separar(valor1)
    valor2_numero, valor2_unidades = separar(valor2)

    valor_1_bytes = a_bytes(valor1_numero, valor1_unidades)
    valor_2_bytes = a_bytes(valor2_numero, valor2_unidades)

    if valor_1_bytes == valor_2_bytes:
        print(f'Los valores {valor1} y {valor2} son iguales.')
    elif valor_1_bytes > valor_2_bytes:
        print(f'El valor {valor1} es mayor que {valor2}.')
    else:
        print(f'El valor {valor2} es mayor que {valor1}.')

if __name__ == "__main__":
    print('Pruebas separar:')
    print(separar('1B'))
    print(separar('1KiB'))
    print(separar('1024MiB'))

    print('\nPruebas a_bytes:')
    print(a_bytes(1, 'B'))
    print(a_bytes(1, 'KiB'))
    print(a_bytes(1, 'MiB'))
    print(a_bytes(9, 'MiB'))
    print(a_bytes(1, 'GiB'))
    
    print('\nPruebas comparar_unidades:')
    comparar_unidades('1B', '1KiB')
    comparar_unidades('1023B', '1KiB')
    comparar_unidades('1024B', '1KiB')
    comparar_unidades('1025B', '1KiB')
    comparar_unidades('1KiB', '1MiB')
    comparar_unidades('1GiB', '1MiB')