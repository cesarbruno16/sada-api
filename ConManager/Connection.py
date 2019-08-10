import mysql.connector
from config import Res


class Connection(object):
    """
    Classe de conexao com a base de dados
    """
    def __init__(self):
        try:
            host = Res.DB['host']
            user = Res.DB['user']
            password = Res.DB['password']
            port = Res.DB['port']
            db = Res.DB['db']
            self.cnx = mysql.connector.connect(user=user, password=password,
                                               host=host,
                                               port=port,
                                               database=db)
            self.cursor = self.cnx.cursor()
        except mysql.connector.Error as exception:
            raise exception
