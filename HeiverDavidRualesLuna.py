print('\nPunto 1 -------------------------------------------------------------------------------------')

def recorrer_matriz(matriz: list[list], i: int, j: int, direccion: str = None, resultado: str = ''):
    if direccion is None:
        return f"Izquierda: {recorrer_matriz(matriz, i, j, 'izquierda')} \nDerecha: {recorrer_matriz(matriz, i, j, 'derecha')} \nArriba: {recorrer_matriz(matriz, i, j, 'arriba')} \nAbajo: {recorrer_matriz(matriz, i, j, 'abajo')}"
    if direccion == 'izquierda':
        if j == -1:
            return resultado
        resultado = resultado + matriz[i][j]
        return recorrer_matriz(matriz, i, j-1, 'izquierda', resultado)
    if direccion == 'derecha':
        if j == len(matriz[0]):
            return resultado
        resultado = resultado + matriz[i][j]
        return recorrer_matriz(matriz, i, j+1, 'derecha', resultado)
    if direccion == 'arriba':
        if i == -1:
            return resultado
        resultado = resultado + matriz[i][j]
        return recorrer_matriz(matriz, i-1, j, 'arriba', resultado)
    if direccion == 'abajo':
        if i == len(matriz):
            return resultado
        resultado = resultado + matriz[i][j]
        return recorrer_matriz(matriz, i+1, j, 'abajo', resultado)


matriz = [['A','B','C','X'],
          ['D','E','F','Y'],
          ['G','H','I','Z']]
i = 1
j = 1
print(recorrer_matriz(matriz, i, j))

# Temporal (Big‑O): n
# Porque solo recorre
# Espacial (Big‑O): n


print('\nPunto 2 -------------------------------------------------------------------------------------')

def compresion_RLE(caracteres: str, i: int = 0, resultado: str = '  '):
    if caracteres == '':
        return ''
    if i == len(caracteres):
        return resultado
    if caracteres[i] != resultado[-2]:
        resultado = resultado + caracteres[i] + str(1)
    return compresion_RLE(caracteres, i+1, resultado)

print(compresion_RLE("aaabbc"))
print(compresion_RLE("xxxxxyyyzz"))
print(compresion_RLE("ab"))


print('\nPunto 3 -------------------------------------------------------------------------------------')

def tipo_de_letra(palabra: str, contador: list[int] = [0,0],  i: int = 0, resultado = None):
    if i == len(palabra):
        return resultado
    resultado = tipo_de_letra(palabra, contador, i+1, resultado)
    if palabra[i] in 'aeiou':
        contador[0] += 1
    else:
        contador[1] += 1
    if i == 0:
        if contador[0] > contador[1]:
            return "más vocales"
        else:
            return "más consonantes"


print(tipo_de_letra("aymuchachos", [0,0]))
print(tipo_de_letra("nocanceleeeeeeeeeeeeeeemos", [0,0]))

# Temporal (Big‑O): n
# Porque solo recorre
# Espacial (Big‑O): n



# Punto 4 -------------------------------------------------------------------------------------
# Temporal (Big‑O): n*log(n)


# Punto 5 -------------------------------------------------------------------------------------
# Temporal (Big‑O): n^2

