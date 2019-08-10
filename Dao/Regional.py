import mysql.connector
from ConManager.Connection import Connection


def _open_con():
    global connection
    global cnx
    global cursor
    connection = Connection()
    cnx = connection.cnx
    cursor = connection.cursor


class Regional(object):
    id = ''
    nome = ''

    def __init__(self, _id: int = 0, _nome: str = ''):
        self.id = _id
        self.nome = _nome

    @staticmethod
    def obter_regional(_id):
        try:
            _open_con()
            sql = """SELECT id_regional, 
                            nome_regional
                       FROM TB_REGIONAL
                      WHERE id_regional = %(id)s"""
            _regional = Regional()
            cursor.execute(sql, {"id": _id})
            for id_regional, nome_regional in cursor:
                _regional = Regional(id_regional, nome_regional)
            return _regional
        except mysql.connector.Error as mysql_error:
            raise mysql_error

    @staticmethod
    def inserir_regional(_nome):
        try:
            _open_con()
            sql = """INSERT INTO TB_REGIONAL (nome_regional) 
                          VALUES (%(nome)s)"""
            cursor.execute(sql, {"nome": _nome})
            cnx.commit()
            return 1
        except mysql.connector.Error as mysql_error:
            raise mysql_error
        finally:
            cursor.close()
            cnx.close()

    @staticmethod
    def atualizar_regional(_id_regional, _nome):
        try:
            _open_con()
            sql = """UPDATE TB_REGIONAL 
                        SET nome_regional = %(nome)s 
                      WHERE id_regional = %(id_regional)s"""
            cursor.execute(sql, {"nome": _nome, "id_regional": _id_regional})
            cnx.commit()
            return 1
        except mysql.connector.Error as mysql_error:
            raise mysql_error
        finally:
            cursor.close()
            cnx.close()

    @staticmethod
    def excluir_regional(_id_regional):
        try:
            _open_con()
            sql = """DELETE FROM TB_REGIONAL
                           WHERE id_regional = %(id_regional)s"""
            cursor.execute(sql, {"id_regional": _id_regional})
            cnx.commit()
            return 1
        except mysql.connector.Error as mysql_error:
            raise mysql_error
        finally:
            cursor.close()
            cnx.close()
