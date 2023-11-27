Inicio: generar aleatoriamente "n" cromosomas (posibles soluciones al problema)
Fitness: evaluar f(x) para cada cromosoma x en la población
Descendencia: crear nueva poblacion
    Seleccion: seleccionar cromosomas de acuerdo a f(x) (mayor fitness mayor oportunidad)
    Cruzamiento: cruzar cromosomas con alguna probabilidad de cruzamiento, sino la descendencia es la copia exacta de los padres.
    Mutación: con probabilidad de mutación mutar la descendencia en su locus.
Reemplazo: usar la descendencia para correr el algoritmo
Test: si se satisface alguna condición parar y retomar la mejor solución del problema.
Loop: retornar al paso 2

Problema:
un ciclista debe llevar en su mochila algunos alimentos de tal manera que pueda asegurar un total minimo de 2000 calorias para soportar un recorrido de 4 horas. La mochila solo tiene capacidad para llevar un peso máximo de 2.0kg. La informacieon de los alimentos diposibles son:

| Articulo      | Calorias      | Peso(kg) |
| Leche de soya | 500           | 0.5      |
| Galleta integral 300 0.1
| Agua mineral 100 0.5
| Pan con pollo 700 0.25
| Huevo duro 300  0.15
| Nueves 400      0.15
| Yogurt  500     0.5
| Manzana 400     0.3

Solución:
Cromosoma binario: 1 lleva y 0 no lleva, ejem: 1 1 0 0 1 1 1 0

Datos:
Poblacion == 4
Minimo de calorias = 2000
Peso máximo = 2.0kg

Primera generación:
Cromosomas      Peso    Calorias        Fitness_Peso    Fitness Calorias        Fitness_total
1 1 0 0 1 1 1 0 1.40    2000            23%             21%                     44%
0 1 0 1 1 1 1 1 1.45    2600            24%             27%                     51%
1 1 0 1 1 1 0 1 1.45    2600            24%             27%                     51%
0 1 1 1 1 0 1 1 1.80    2300            30%             24%                     54%
                6.10    9500
Nota: seleccionamos los que tengan mayor fitness

Seleccion:
El 44% se reemplaza por el 54%
0 1 1 1 1 0 1 1
0 1 0 1 1 1 1 1
1 1 0 1 1 1 0 1
0 1 1 1 1 0 1 1

Cruzamiento:
se mantiene la primera parte y la segunda se cambia con la pareja
Pareja 1:
0 1 | 1 1 1 0 1 1       0 1 0 1 1 1 1 1
0 1 | 0 1 1 1 1 1       0 1 1 1 1 0 1 1
Pareja 2:
1 1 0 | 1 1 1 0 1       1 1 0 1 1 0 1 1
0 1 1 | 1 1 0 1 1       0 1 1 1 1 1 0 1



Based on https://www.youtube.com/watch?v=bNRPk8mX5SA
