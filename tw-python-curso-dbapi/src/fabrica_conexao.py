import configparser

import MySQLdb


class FabricaConexao():

    @staticmethod
    def conectar():
        config = configparser.ConfigParser()
        config.read('config.ini')
        db = MySQLdb.connect(user=config['DATABASE']['USER'],
                             password=config['DATABASE']['PASSWORD'],
                             host=config['DATABASE']['HOST'],
                             port=config['DATABASE']['PORT'],
                             db=config['DATABASE']['DB'],
                             autocommit=config['DATABASE']['AUTOCOMMIT'])
        return db


