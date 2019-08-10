import mysql.connector
from ConManager.Connection import Connection


def _open_con():
    global connection
    global cnx
    global cursor
    connection = Connection()
    cnx = connection.cnx
    cursor = connection.cursor


class Igreja(object):
    id = ''
    numero = ''
    nome = ''
    id_adm = ''
    id_setor = ''

    def __init__(self, _id: int = 0,
                 _numero: int = 0,
                 _nome: str = '',
                 _id_adm: int = 0,
                 _id_setor: int = 0):
        self.id = _id
        self.numero = _numero
        self.nome = _nome
        self.id_adm = _id_adm
        self.id_setor = _id_setor

    @staticmethod
    def inserir_igreja(_numero, _nome, _id_adm, _id_setor):
        try:
            _open_con()
            sql = """INSERT INTO TB_IGREJA (numero_igreja, 
                                            nome_igreja, 
                                            id_adm, 
                                            id_setor) 
                                    VALUES (%(numero)s, 
                                            %(nome)s, 
                                            %(id_adm)s, 
                                            %(id_setor)s)"""
            cursor.execute(sql, {"numero": _numero,
                                 "nome": _nome,
                                 "id_adm": _id_adm,
                                 "id_setor": _id_setor})
            cnx.commit()
            return 1
        except mysql.connector.Error as mysql_error:
            raise mysql_error
        finally:
            cursor.close()
            cnx.close()

    @staticmethod
    def obter_igreja(_id):
        try:
            _open_con()
            sql = """SELECT id_igreja, 
                            numero_igreja,
                            nome_igreja,
                            id_adm,
                            id_setor
                       FROM TB_IGREJA
                      WHERE id_igreja = %(id)s"""
            _igreja = Igreja()
            cursor.execute(sql, {"id": _id})
            for id_igreja, \
                nome_igreja, \
                numero_igreja, \
                id_adm, \
                    id_setor in cursor:
                _igreja = Igreja(id_igreja,
                                 numero_igreja,
                                 nome_igreja,
                                 id_adm,
                                 id_setor)
            return _igreja
        except mysql.connector.Error as mysql_error:
            raise mysql_error

    @staticmethod
    def atualizar_igreja(_id, _nome, _numero, _id_adm, _id_setor):
        try:
            _open_con()
            sql = """UPDATE TB_IGREJA 
                        SET nome_igreja = %(nome)s,
                            numero_igreja = %(numero)s,
                            id_adm = %(id_adm)s,
                            id_setor = %(id_setor)s 
                      WHERE id_igreja = %(id)s"""
            cursor.execute(sql, {"nome": _nome,
                                 "numero_igreja": _numero,
                                 "id_adm": _id_adm,
                                 "id_setor": _id_setor,
                                 "id": _id})
            cnx.commit()
            return True
        except mysql.connector.Error as mysql_error:
            raise mysql_error
        finally:
            cursor.close()
            cnx.close()

    @staticmethod
    def excluir_igreja(_id):
        try:
            _open_con()
            sql = """DELETE FROM TB_IGREJA 
                           WHERE id_igreja = %(id)s"""
            cursor.execute(sql, {"id": _id})
            cnx.commit()
            return 1
        except mysql.connector.Error as mysql_error:
            raise mysql_error
        finally:
            cursor.close()
            cnx.close()
