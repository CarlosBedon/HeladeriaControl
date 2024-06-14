Ice Cream Shop App
==================

Se requiere crear una aplicación interna para el control del producto utilizado en una heladería. 
Al ser de uso interno es importante **desactivar** la opción de **SignUp** ya que los usuarios van 
a ser administrados directamente por el administrador del sistema. 

El objetivo de la aplicación es controlar la cantidad de helado usado en cada turno.

Estructura del Sistema
-----------------------

El sistema se puede dividir en cuatro secciones: 

- **Administración**: sección donde se ingresa la información de los Sabores y Presentaciones
- **Registro de Pesos**: sección que almacena el registro de peso inicial y final diario de cada sabor de helado. 
- **Venta Diaria**: sección que registra la cantidad de productos por presentación que se vendieron en el día. 
- **Dashboard**: sección donde se muestra la diferencia del peso de cada producto antes y después del turno y la 
  discrepancia entre lo usado y lo estimado. 

Administración
---------------

- Se debe almacenar el ``nombre`` de los distintos ``Sabores`` de helado. 
- La tienda tiene distintas ``Presentaciones`` de helado, i.e. Cono Simple, Doble, Banana Split, etc, y cada presentación
  lleva una cantidad distinta de helado. Por lo tanto, se requiere almacenar el ``nombre`` y la ``cantidad_helado`` de cada ``Presentacion``. 
  Por facilidad, la ``cantidad_helado`` se va a almacenar en gramos (y como un número entero positivo).

Venta Diaria
------------
- El usuario va a ingresar en ``VentaDiaria``, la ``fecha`` del ingreso, la ``presentacion`` y la ``cantidad`` vendida. Por ejemplo: 

    - El `13/06/2024` (fecha) se vendieron `4` (cantidad) `conos simples` (presentación). 

- Si el desarrollador desea que el usuario no ingrese `manualmente` la fecha, se debe buscar una forma de almanacer la fecha al 
  momento de guardar el registro. 

    - Solo se debería asignar la fecha actual a ``fecha`` cuando se **crea** el registro, no se debe modificar cuando se **edita**
      el registro.


Registro de Pesos
-----------------

- Se necesita llevar un registro(``RegistroPeso``) del peso al inicio y al final de cada turno de cada sabor de helado. A su vez se desea registrar 
  la fecha y hora a la cual el usuario ingreso el peso inicial y la fecha y hora a la que ingreso el peso final. 

  - Para evitar obtener y almancear el ``user`` del ``request``se va a asumir que únicamente una persona realiza el pesaje e 
    ingreso de todos los productos, 

- Para esto se va a almacenar el ``sabor`` del helado, ``peso_inicial``, ``inicial_ingresado_el``, ``peso_final``, ``final_ingresado_el``. 

  - ``peso_inicial`` y ``peso_final`` se va a almacenar en gramos (y como un número entero positivo).
  - Tanto ``inicial_ingresado_el`` como ``final_ingresado_el`` deben ser obtenido y almacenados automáticamente. 
  - No se puede ingresar ``peso_final`` si ``peso_inicial`` aún no ha sido ingresado. 
  - Solo puede existir **un** registro por ``sabor`` y ``peso_inicial``. Por ejemplo solo puede haber un registro de
    helado de chicle el 13/10/2024.   

    - El atributo `unique_for_date <https://docs.djangoproject.com/en/4.2/ref/models/fields/#unique-for-date>`_ puede ser de utilidad


Dashboard
-------------------

- Se debe crear un dashboard que muestre una tabla con las siguientes columnas: 

    - Fecha
    - Peso Inicial Total 
    - Peso Final Total 
    - Venta Total [en gramos]
    - +/- (Diferencia)

- Para simplificar el modelo, la Diferencia va a ser calculada únicamente por total, 
  no por sabor ni por presentacion. Lo que quiere decir que: 

  - Peso Inicial Total, es la sumatoria del ``peso_inicial`` de todos los sabores 
  - Peso Final Total, es la sumatoria del ``peso_final`` de todos los sabores 
  - Venta Total [en gramos], es la sumatoria de ``VentaDiaria.cantidad * Presentacion.cantidad_helado``. 

    - Recordar que puede haber varios registros de VentaDiaria para una misma fecha

  - +/- (Diferencia), es el resultado de ``uso_helado - venta_total``, donde ``uso_helado``es **Peso Final Total - Peso Inicial Total*

    - Para facilidad visual a esta columna se le va a poner un formato de celda en base a su valor. 
    - Si, ``uso_helado > venta_total`` mostrar celda con background ``bg-danger``
    - Si, ``uso_helado == venta_total`` mostrar celda con background ``bg-success``
    - Si, ``uso_helado < venta_total`` mostrar celda con background ``bg-warning``
    - Debido a que se pueden producir pérdidas al momento de servir, por el método de pesaje, etc. es casi 
      imposible obtener ``uso_helado == venta_total``, por lo tanto para la comparación se va a considerar un 
      margen aceptable de error, i.e del 5% (el margen a usar queda a discreción del desarrollador). 

      - Se recomienda no "quemar" el valor en código, sino almacenar el margen como una constante 
        para que sea de fácil modificación. 

    - Para encontrar los totales de forma eficiente se recomienda utilizar 
      `Aggregation <https://docs.djangoproject.com/en/4.2/topics/db/aggregation/>`_ a nivel de la 
      la base de datos. 

Consideraciones Generales
--------------------------

- Todas las tablas deben tener filtros relevantes 


Consideraciones de Tecnología
------------------------------

Los siguientes paquetes ya están instalados en el proyecto: 

- `django-tables2 <https://github.com/jieter/django-tables2>`_
- `django-filter <https://github.com/carltongibson/django-filter>`_
- `django-htmx <https://github.com/adamchainz/django-htmx>`_
- `django-bootstrap-datepicker-plus <https://github.com/monim67/django-bootstrap-datepicker-plus>`_
- `htmx <https://htmx.org/>`_ (Instalado en package.json y bundled con Gulp)

Si se requieren paquetes adicionales, puedes instalarlos sin ninguna restricción. 

La solución implementada debe cumplir los siguientes puntos: 

- Para hacer la UI más dinámica se utiliza el framework ``htmx``. 

    - Se debe utilizar ``htmx`` para filtrar las tablas sin hacer un full page reload. 
    - En las tablas cuando se ordena por una columna y el pagination debe ser manejado por ``htmx`` para no hacer un full page reload. 
    - Crear por lo menos un modal con un formulario con ``htmx`` para la creación o edición de algún modelo. 

- Las tablas se deben implementar con ``django-tables2``. 
- Para los filtros utilizar ``django-filters``. 
- Utilizar ``django-crispy-forms`` para la creación de formularios. 
- Si puede utilizar ``django-bootstrap-datepicker-plus`` para los datetime fields.
- Utilizar ``pytest`` para las pruebas 

    - El proyecto debe tener un coverage de por lo menos el 90% 

Recursos Útiles
---------------

HTMX

- `Modal forms with Django+HTMX <https://blog.benoitblanchon.fr/django-htmx-modal-form/>`_
- `django-htmx en GitHub <https://github.com/adamchainz/django-htmx/tree/main>`_
- `Responsive table with Django and htmx <https://enzircle.com/responsive-table-with-django-and-htmx>`_
- `dj-htmx-fun <https://github.com/joashxu/dj-htmx-fun>`_
- `How to Create a Responsive Table with HTMX and Django <https://hackernoon.com/how-to-create-a-responsive-table-with-htmx-and-django>`_

Django Crispy Forms

- `Advanced Form Rendering with Django Crispy Forms <https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html>`_

Pytest

- `Playlist de YouTube sobre Pytest <https://www.youtube.com/playlist?list=PLOLrQ9Pn6caw3ilqDR8_qezp76QuEOlHY>`_
- `Python Pytest and Django Course <https://github.com/veryacademy/pytest-mastery-with-django>`_
- `Simplified Django Tests With Pytest and Pytest FactoryBoy <https://schegel.net/posts/simplied-django-tests-with-pytest-and-pytest-factoryboy/>`_

