2025-06-18: dia cero. foco en la familia.
2025-06-26: dia cero. foco en mi bienestar mental y emocional.
2025-06-27: comprension de conceptos.
    1- sqlite3.connect: lo utilizamos como permiso de entrada para establecer una conexion a una base de datos en memoria para el manejo de datos de manera eficiente.
    2- connection.cursor: es el comando que vamos a utilizar para comunicarnos dentro de la base de datos, combinándolo con diferentes sentencias.
    3- Lenguaje SQL: este NO es python, lo utilizamos para definir(CREATE TABLE), insertar (INSERT TO), consultar(SELECT), modificar(UPDATE) y eliminar(DELETE). Lo escribiremos en cadenas dentro de python pero lo interpretara el motor de la base de datos
    4- Parametros (?): es por asi decirlo, el comando con el que marcamos el hueco para un dato, es decir le decimos al sistema que no lo ejecute ni lo interprete ya que es solo un dato y debe tratarlo como tal. De esta manera tambien nos aseguramos que aunque haya algun usuario malicioso, no va a poder modificar nuestra base de datos ya que esta no va a ejecutar lo que el usuario introduzcaen ese "hueco".
