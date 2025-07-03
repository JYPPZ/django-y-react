# 🔍 Búsqueda de Vecinos Numéricos

Un algoritmo eficiente para encontrar los vecinos numéricos más cercanos en una lista ordenada.

## 🚀 Instalación y Ejecución

### Prerrequisitos
- Python 3.6 o superior
- No requiere librerías adicionales (usa solo `bisect` de la librería estándar)

### Instalación
```bash
# Clonar o descargar el archivo
git clone https://github.com/JYPPZ/django-y-react.git
cd django-y-react/algoritmia

# O simplemente descargar solucion_problema.py
```

### Ejecución
```bash
python solucion_problema.py
```

## 📝 Formato de Entrada

El programa solicita los datos en el siguiente orden:

1. **Número de elementos** en la lista base (entero)
2. **Lista base** de números separados por espacios (ordenada de menor a mayor)
3. **Número de consultas** a realizar (entero)
4. **Números a consultar** separados por espacios

### Ejemplo de Entrada
```
5
2 4 5 7 9
4
2 5 6 10
```

## 📤 Formato de Salida

Para cada consulta, imprime una línea con dos valores separados por espacio:
- Primer valor: Mayor número menor (o "X" si no existe)
- Segundo valor: Menor número mayor (o "X" si no existe)

### Ejemplo de Salida
```
X 4
4 7
5 7
9 X
```

## 🔢 Ejemplos de Uso

### Ejemplo 1: Caso básico
```bash
$ python solucion_problema.py
3
1 5 8
3
0 5 10
```
**Salida:**
```
X 1
1 8
8 X
```

### Ejemplo 2: Con números negativos
```bash
$ python solucion_problema.py
4
-3 -1 2 7
4
-2 0 2 8
```
**Salida:**
```
-3 -1
-1 2
-1 7
7 X
```

### Ejemplo 3: Con duplicados
```bash
$ python solucion_problema.py
6
1 3 3 5 5 9
5
1 3 4 5 12
```
**Salida:**
```
X 3
1 5
3 5
3 9
9 X
```

## ⚙️ Cómo Funciona

### Algoritmo
1. **Filtrado**: Elimina números iguales al consultado
2. **Búsqueda binaria**: Encuentra la posición de inserción usando `bisect.bisect_left()`
3. **Vecino izquierdo**: Elemento en `posición - 1` (si existe)
4. **Vecino derecho**: Elemento en `posición` (si existe)
5. **Retorna**: Los vecinos encontrados o "X" si no existen
