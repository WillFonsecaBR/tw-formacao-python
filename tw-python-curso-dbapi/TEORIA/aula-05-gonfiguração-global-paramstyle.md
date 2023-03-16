# A configuração global paramstyle

Para determinar o tipo dos parâmetros que serão aceitos em nossas consultas, utilizamos a configuração global “paramstyle”. A biblioteca MySQLdb dispõe de dois tipos de parâmetros, o formato ANSI C e o Pyformat. Para utilizá-los, definimos a configuração da seguinte forma:

``` python
#Formato ANSI C
MySQLdb.paramstyle = "format"

#Pyformat
MySQLdb.paramstyle = "pyformat"

```
