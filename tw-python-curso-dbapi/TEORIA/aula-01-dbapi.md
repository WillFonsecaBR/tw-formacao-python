# O que é a DB-API?

A DB-API é, basicamente, um documento que visa prover uma interface para que todas as conexões de banco de dados funcionem de forma semelhante.

Imagine que queremos conectar nossa aplicação Python a um banco de dados MySQL. Após escrever toda a lógica para acesso a conexão, tudo funciona perfeitamente. Porém, após algum tempo de uso, precisamos alterar o banco de dados a ser utilizado para SQL Server. Sem uma especificação, provavelmente as bibliotecas de conexão do MySQL e SQL Server possuem métodos diferentes para a mesma finalidade, fazendo com que a gente tenha que escrever boa parte de código.

Pensando nisso, a equipe de desenvolvimento do Python propôs uma interface para que todas as bibliotecas de conexão com banco de dados sigam um padrão e, assim, evitar transtornos como esse. Essa interface é conhecida como DB-API e pode ser visualizada através do seguinte link: <https://www.python.org/dev/peps/pep-0249/>

Neste curso veremos os principais conceitos da DB-API e como conectar com bancos de dados através dela.
