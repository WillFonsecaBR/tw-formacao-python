import MySQLdb

import fabrica_conexao


class ClienteRepositorio():
  @staticmethod
  def listar_clientes():
    fabrica = fabrica_conexao.FabricaConexao.conectar()
    cursor = fabrica.cursor()
    
    fabrica.close()
    
