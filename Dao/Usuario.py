import mysql.connector
from ConManager.Connection import Connection


def _open_con():
    global connection
    global cnx
    global cursor
    connection = Connection()
    cnx = connection.cnx
    cursor = connection.cursor


class Usuario(object):
    id = ''
    email = ''
    senha = ''
    nome = ''

    def __init__(self, _id='', _email='', _nome='', _hash=''):
        self.id = _id
        self.email = _email
        self.nome = _nome
        self.hash = _hash

    @staticmethod
    def obter_usuario_por_id(_id):
        try:
            _open_con()
            sql = """SELECT 
                     id_usuario, 
                     email_usuario, 
                     nome_usuario, 
                     senha  
                     FROM TB_USUARIO
                     WHERE id_usuario = %(id)s"""
            user = Usuario()
            cursor.execute(sql, {"id": _id})
            for id_usuario, email_usuario, nome_usuario, senha in cursor:
                user = Usuario(id_usuario, email_usuario, nome_usuario, senha)
            return user
        except mysql.connector.Error as mysql_error:
            raise mysql_error

    @staticmethod
    def obter_usuario_por_email(_email):
        try:
            _open_con()
            sql = """SELECT 
                     id_usuario, 
                     email_usuario, 
                     nome_usuario, 
                     senha  
                     FROM TB_USUARIO
                     WHERE email_usuario = %(email)s"""
            user = Usuario()
            cursor.execute(sql, {"email": _email})
            for id_usuario, email_usuairo, nome_usuairo, hash in cursor:
                user = Usuario(id_usuario, email_usuairo, nome_usuairo, hash)
            cnx.commit()
            return user
        except mysql.connector.Error as mysql_error:
            raise mysql_error
        finally:
            cursor.close()
            cnx.close()

    @staticmethod
    def inserir_usuario(_email, _hash, _nome):
        try:
            _open_con()
            sql = """INSERT INTO TB_USUARIO (email_usuario, nome_usuario, senha) 
                          VALUES (%(email)s, %(nome)s, %(hash)s)"""
            cursor.execute(sql, {"email": _email, "nome": _nome, "hash": _hash})
            cnx.commit()
            return 1
        except mysql.connector.Error as mysql_error:
            raise mysql_error
        finally:
            cursor.close()
            cnx.close()

    @staticmethod
    def atualizar_usuario(_id_usuario, _email, _nome, _hash):
        try:
            _open_con()
            sql = """UPDATE TB_USUARIO 
                        SET email_usuario = %(email)s, 
                            nome_usuario = %(nome)s, 
                            senha = %(hash)s
                      WHERE id_usuario = %(id_usuario)s"""
            cursor.execute(sql, {"email": _email, "nome": _nome, "hash": _hash, "id_usuario": _id_usuario})
            cnx.commit()
            return 1
        except mysql.connector.Error as mysql_error:
            raise mysql_error
        finally:
            cursor.close()
            cnx.close()

    @staticmethod
    def excluir_usuario(_id_usuario):
        try:
            _open_con()
            sql = """DELETE FROM TB_USUARIO
                           WHERE id_usuario = %(id_usuario)s"""
            cursor.execute(sql, {"id_usuario": _id_usuario})
            cnx.commit()
            return 1
        except mysql.connector.Error as mysql_error:
            raise mysql_error
        finally:
            cursor.close()
            cnx.close()

    def set_token(self, _token):
        try:
            _open_con()
            _query = 'UPDATE TB_USUARIO ' \
                     '   SET V_TOKEN_AUTH_TEMP = %(token)s ' \
                     ' WHERE id_usuario = %(id)s'
            cursor.execute(_query, {"token": _token, "id": self.id})
            cnx.commit()
            cnx.close()
        except mysql.connector.Error as merr:
            raise merr

    @staticmethod
    def obter_token_por_email(_email):
        try:
            _open_con()
            _query = 'SELECT V_TOKEN_AUTH_TEMP ' \
                     '  FROM TB_USUARIO ' \
                     ' WHERE email_usuario = %(email)s'
            cursor.execute(_query, {"login": _email})
            _token = None
            for V_TEMP_AUTH_TOKEN in cursor:
                _token = str(V_TEMP_AUTH_TOKEN[0])
            cnx.commit()
            cnx.close()
            return str(_token)
        except mysql.connector.Error as _merr:
            raise _merr
