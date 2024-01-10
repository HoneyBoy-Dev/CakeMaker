# Text.
> Un componente de tipo texto que puede renderizar y asignar propiedades.
## Propiedades.
* **text** Utiliza un valor de tipo string para renderizar un texto.
* **font_size** Asigna el tamaño de la fuente.
* **font_family** Asigna un tipo/familia de fuente (.ttf)
* **color** Asigna un color al texto (RGB).
* **side** Puedes anclar el componente en una posicion. Valores:
    * 'top' arriba del componente padre.
    * 'bottom' debajo del componente padre.
    * 'left' lateral izquierda del componente padre.
    * 'right' lateral derecha del componente padre.
* **anti_aliasing** filtro de suavisado.
    * True ó  False.
* **limit_str**
    * 0: desactivado
    * 1 o mayor: tamaño del limite
* **bg** Establece un fondo con un color (RGB).
    * (255, 255, 255): color blanco.
* **padding** Establece el tamaño del relleno.

## Funciones.
* **get_size()** devuelve el ancho y el alto.
* **get_width()** devuelve el ancho.
* **get_height()** devuelve el alto.
