# https://www.unitjuggler.com/memory-convertir-MiB-a-B.html?val=9
# https://www.lenovo.com/es/es/glossary/kilobyte/index.html

def separar(valor):
    numero = ""
    indice = 0
    while indice < len(valor) and valor[indice].isdigit():
        numero += valor[indice]
        indice+=1
    
    return int(numero), valor[indice:]


print(separar('1B'))
print(separar('1KiB'))
print(separar('1024MiB'))


def kb_a_bytes(valor):
    return valor * 1024

def mb_a_bytes(valor):
    return valor * 1048576

def gb_a_bytes(valor):
    return valor * 1073741824

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

print(a_bytes(1, 'KiB'))    
print(a_bytes(9, 'MiB')) # 9437184

def comparar_unidades(valor1, valor2):
    valor1_numero, valor1_unidades = separar(valor1)
    valor2_numero, valor2_unidades = separar(valor2)
    valor_1_bytes = a_bytes(valor1_numero, valor1_unidades)
    valor_2_bytes = a_bytes(valor2_numero, valor2_unidades)

    if valor_1_bytes == valor_2_bytes:
        return 0
    elif valor_1_bytes > valor_2_bytes:
        return 1
    else:
        return -1

print(comparar_unidades('1B', '1KiB'))
print(comparar_unidades('1024B', '1KiB'))
print(comparar_unidades('1KiB', '1MiB'))
print(comparar_unidades('1GiB', '1MiB'))
