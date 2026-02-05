<img width="300" height="214" alt="image" src="https://miro.medium.com/v2/resize:fit:750/format:webp/1*Bv4vlSEMIQRgLxiijeNE5Q.gif" />


🗺️ Generador de Mapa con Coordenadas en Python
-----------------------------------------------

Este proyecto consiste en la creación de un mapa bidimensional representado por una matriz, donde el usuario define el tamaño del mapa y selecciona manualmente un **punto de inicio** y un **punto de salida**, validando que las coordenadas sean correctas.

El mapa se visualiza en consola utilizando **emojis**, lo que lo hace más intuitivo y fácil de entender.

* * * * *

🎯 Objetivos del proyecto
-------------------------

-   Practicar el uso de **matrices** en Python

-   Aplicar **funciones** para organizar el código

-   Validar entradas del usuario

-   Representar datos visualmente en consola

-   Implementar constantes y símbolos para mayor claridad

* * * * *

🧱 Elementos del mapa
---------------------

Cada celda del mapa representa un tipo de terreno:

-   ⬛ Libre

-   🏢 / 🏦 / 🏨 Edificios (obstáculos)

-   🟦 Agua

-   🚦 Obstáculo

-   🟢 Punto de inicio

-   🔴 Punto de salida

* * * * *

⚙️ Funcionamiento
-----------------

1.  El usuario ingresa la cantidad de filas y columnas del mapa.

2.  El programa genera automáticamente la matriz.

3.  Se muestra el mapa inicial en consola.

4.  El usuario ingresa las coordenadas del punto de inicio.

    -   Se valida que estén dentro del mapa y en una celda libre.

5.  El usuario ingresa las coordenadas del punto de salida.

    -   Se aplica la misma validación.

6.  El mapa se actualiza y se vuelve a mostrar en consola.

* * * * *

▶️ Ejecución
------------

Ejecutar el archivo principal con:

`python main.py`

(Sustituir `main.py` por el nombre real del archivo si es distinto)

* * * * *

📌 Requisitos
-------------

-   Python 3.x

-   Consola compatible con emojis

* * * * *

📚 Conceptos aplicados
----------------------

-   Listas anidadas (matrices)

-   Funciones

-   Validación de datos

-   Uso de constantes

-   Estructura `main`

-   Entrada de datos por consola
