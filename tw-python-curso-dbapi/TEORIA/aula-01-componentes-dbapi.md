# Principais componentes da DB-API

Há diversos componentes presentes na especificação da DB-API no Python, das quais veremos as mais importantes durante o curso. Todos os componentes podem ser vistos através da sua documentação no link <https://www.python.org/dev/peps/pep-0249/>

A DB-API provê uma série de recursos para a comunicação e manipulação dos dados no banco de dados, são eles:

Connect: Construtor da classe que irá receber uma série de parâmetros de acesso ao banco de dados;
Apilevel: Com essa propriedade, podemos especificar qual versão da DB-API queremos utilizar em nosso projeto;
Paramstyle: Definimos o formato dos parâmetros que enviaremos através das nossas consultas utilizando a DB-API;
Begin, Commit e Rollback: Métodos para realizar transações utilizando a DB-API;
Cursor: Com o cursor, conseguimos obter e enviar comandos SQL para o banco de dados que estamos utilizando. Vamos usar bastante os cursores ao longo do curso.
Esses são alguns dos principais métodos/propriedades da DB-API. Vale lembrar que nós veremos, detalhadamente, cada um individualmente.
