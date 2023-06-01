"""verificador y metodo burbuja"""
def verificador_precio(productos):
    '''verifica que el arreglo este ordenado de menor a mayor'''
    n = len(productos)
    for i in range(n-1):
        for j in range(i+1,n):
            if productos[j].precio < productos[i].precio:
                burbuja_precio(productos)
                return True
def burbuja_precio(arreglo):
    '''ordena los numeros del arreglo'''
    n = len(arreglo)
    for i in range(n-1):
        for j in range(i+1,n):
            if arreglo[i].precio > arreglo[j].precio:
                temp = arreglo[i]
                arreglo[i] = arreglo[j]
                arreglo[j] = temp