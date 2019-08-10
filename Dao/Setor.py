import mysql.connector
from ConManager.Connection import Connection


def _open_con():
    global connection
    global cnx
    global cursor
    connection = Connection()
    cnx = connection.cnx
    cursor = connection.cursor


class Setor(object):
    id = ''
    nome = ''

    def __init__(self, _id: int = 0,
                 _nome: str = ''):
        self.id = _id
        self.nome = _nome

    @staticmethod
    def inserir(_nome):
        try:
            _open_con()
            sql = """INSERT INTO TB_SETOR (nome_setor) 
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
    def obter(_id):
        try:
            _open_con()
            sql = """SELECT id_setor, 
                            nome_setor
                       FROM TB_SETOR
                      WHERE id_setor = %(id)s"""
            _setor = None
            cursor.execute(sql, {"id": _id})
            for id_setor, nome_setor in cursor:
                _setor = Setor(id_setor, nome_setor)
            return _setor
        except mysql.connector.Error as mysql_error:
            raise mysql_error

    @staticmethod
    def atualizar(_id, _nome):
        try:
            _open_con()
            sql = """UPDATE TB_SETOR 
                        SET nome_setor = %(nome)s
                      WHERE id_setor = %(id)s"""
            cursor.execute(sql, {"nome": _nome,
                                 "id": _id})
            cnx.commit()
            return True
        except mysql.connector.Error as mysql_error:
            raise mysql_error
        finally:
            cursor.close()
            cnx.close()

    @staticmethod
    def excluir(_id):
        try:
            _open_con()
            sql = """DELETE FROM TB_SETOR 
                           WHERE id_setor = %(id)s"""
            cursor.execute(sql, {"id": _id})
            cnx.commit()
            return 1
        except mysql.connector.Error as mysql_error:
            raise mysql_error
        finally:
            cursor.close()
            cnx.close()
