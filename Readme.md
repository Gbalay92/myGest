Gonzalo Balay

# Gerencia automática

En este programa ejecutado como "script" existen diferentes funcionalidades que todas deben ejecutarse a la misma altura que estan los scripts. 
- Nomina: A partir del fichero empleados en rrhh generará todas las nóminas del mes actual.
- Compras: A partir del fichero compras en la carpeta facturas se leeran y procesaran las compras creando asi un fichero con el resumen de estas en la misma carpeta facturas
- Ventas: funcionamiento similar a las compras, con la diferencia que este leerá todos los archivos de ventas en su carpeta dentro de la carpeta facturas, esto es debido a que cada venta tiene su propio archivo
- Informe de gerencia: a partir de todo lo anterior generado irá completando el informe incluido en la carpeta gerencia.
- Declaracion de iva: similar al informe de gerencia, con las ventas y las compras procesadas rellenará el informe de declaracion-iva en la carpeta facturas.

Si se intentan realizar los informes de gerencia y declaracion de iva antes de que los otros archivos esten actualizados es posible que se pierdan datos, en caso de duda ejecutar los anteriores.

# Anotaciones

Para el funcionamiento de esta aplicación se utilizan las librerias externas de openpyxl y formulas, será necesaria su instlación en el ordenador.(pip install formulas, pip install openpyxl)

Se adjuntan en el proyecto la estructura de carpetas necesaria, asi como las nominas de los meses de enero y febrero para que se vea el procesameinto de sus datos.



