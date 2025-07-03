import bisect

#   Input
#5
#2 4 5 7 9
#4
#2 5 6 10

#   Output
#x 4
#4 7
#5 7
#9 X



# la lista ya debe estar ordenada
def solucion(lista_base, numero_consulta):
    """
    Usa búsqueda binaria para encontrar posiciones eficientemente
    """
    # Crear lista sin duplicados del número consultado
    lista_filtrada = [num for num in lista_base if num != numero_consulta]
    
    if not lista_filtrada:
        return "X", "X"
    
    # Encontrar posición donde insertaría el número
    pos = bisect.bisect_left(lista_filtrada, numero_consulta)
    
    # Vecino izquierdo (mayor número menor)
    vecino_izquierdo = lista_filtrada[pos - 1] if pos > 0 else "X"
    
    # Vecino derecho (menor número mayor)
    vecino_derecho = lista_filtrada[pos] if pos < len(lista_filtrada) else "X"
    
    return vecino_izquierdo, vecino_derecho

def main():
    """Función principal para ejecutar por consola"""
    # Leer cantidad de elementos
    n = int(input())
    
    # Leer lista base
    lista_base = list(map(int, input().split()))
    
    # Leer cantidad de consultas
    m = int(input())
    
    # Leer números a consultar
    consultas = list(map(int, input().split()))
    
    # Procesar cada consulta
    for numero in consultas:
        izq, der = solucion(lista_base, numero)
        print(f"{izq} {der}")

if __name__ == "__main__":
    main()