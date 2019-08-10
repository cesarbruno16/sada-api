import mysql.connector
from ConManager.Connection import Connection


def _open_con():
    global connection
    global cnx
    global cursor
    connection = Connection()
    cnx = connection.cnx
    cursor = connection.cursor


class Adm(object):
    id = ''
    nome = ''
    id_regional = ''

    def __init__(self, _id, _nome, _id_regional):
        self.id = _id
        self.nome = _nome
        self.id_regional = _id_regional

    @staticmethod
    def inserir_adm(_id, _nome, _id_regional):
        try:
            _open_con()
            sql = """INSERT INTO TB_ADM (nome_adm, id_regional) 
                          VALUES (%(nome)s, %(id_regional)s)"""
            cursor.execute(sql, {"nome": _nome, "id_regional": _id_regional})
            cnx.commit()
            return 1
        except mysql.connector.Error as mysql_error:
            raise mysql_error
        finally:
            cursor.close()
            cnx.close()
