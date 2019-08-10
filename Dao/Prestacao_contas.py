import mysql.connector
from ConManager.Connection import Connection


def _open_con():
    global connection
    global cnx
    global cursor
    connection = Connection()
    cnx = connection.cnx
    cursor = connection.cursor


class PrestacaoContas(object):
    id = ''
    id_igreja = 0
    total_coletas = 0.0
    valor_depositado = 0.0
    despesa_manutencao = 0.0
    construcao_retido = 0.0
    assinada_anciao = False
    assinada_aux_escrita = False
    assinada_cooperador = False
    assinada_diacono = False
    assinada_porteiro = False

    def __init__(self, _id: int = 0,
                 _id_igreja: str = '',
                 _total_coletas: float = 0.0,
                 _valor_depositado: float = 0.0,
                 _despesa_manutencao: float = 0.0,
                 _construcao_retido: float = 0.0,
                 _assinada_anciao: bool = False,
                 _assinada_aux_escrita: bool = False,
                 _assinada_cooperador: bool = False,
                 _assinada_diacono: bool = False,
                 _assinada_porteiro: bool = False
                 ):
        self.id = _id
        self.id_igreja = _id_igreja
        self.total_coletas = _total_coletas
        self.valor_depositado = _valor_depositado
        self.despesa_manutencao = _despesa_manutencao
        self.construcao_retido = _construcao_retido
        self.assinada_anciao = _assinada_anciao
        self.assinada_aux_escrita = _assinada_aux_escrita
        self.assinada_cooperador = _assinada_cooperador
        self.assinada_diacono = _assinada_diacono
        self.assinada_porteiro = _assinada_porteiro

    @staticmethod
    def inserir(_prestacao_contas):
        try:
            _open_con()
            sql = """INSERT INTO TB_PRESTACAO_CONTAS 
            (
            id_igreja, 
            total_coletas,
            valor_depositado,
            despesa_manutencao,
            construcao_retido,
            assinada_anciao, 
            assinada_auxiliar_escrita, 
            assinada_cooperador, 
            assinada_diacono, 
            assinada_porteiro
            ) 
            VALUES 
            (
            %(id_igreja)s,
            %(total_coletas)s,
            %(valor_depositado)s,
            %(despesa_manutencao)s,
            %(construcao_retido)s,
            %(assinada_anciao)s,
            %(assinada_aux_escrita)s,
            %(assinada_cooperador)s,
            %(assinada_diacono)s,
            %(assinada_porteiro)s
            )"""
            cursor.execute(sql, {"id_igreja": _prestacao_contas.id_igreja,
                                 "total_coletas": _prestacao_contas.total_coletas,
                                 "valor_depositado": _prestacao_contas.valor_depositado,
                                 "despesa_manutencao": _prestacao_contas.despesa_manutencao,
                                 "construcao_retido": _prestacao_contas.construcao_retido,
                                 "assinada_anciao": _prestacao_contas.assinada_anciao,
                                 "assinada_aux_escrita": _prestacao_contas.assinada_aux_escrita,
                                 "assinada_cooperador": _prestacao_contas.assinada_cooperador,
                                 "assinada_diacono": _prestacao_contas.assinada_diacono,
                                 "assinada_porteiro": _prestacao_contas.assinada_porteiro})
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
            sql = "SELECT " \
                  "id_prestacao_contas, " \
                  "id_igreja, " \
                  "total_coletas, " \
                  "valor_depositado, " \
                  "despesa_manutencao, " \
                  "construcao_retido, " \
                  "assinada_anciao, " \
                  "assinada_auxiliar_escrita, " \
                  "assinada_cooperador, " \
                  "assinada_diacono, " \
                  "assinada_porteiro " \
                  "FROM " \
                  "TB_PRESTACAO_CONTAS " \
                  "WHERE id_prestacao_contas = %(id)s"
            _prestacao_contas = None
            cursor.execute(sql, {"id": _id})
            for id_prestacao_contas, \
                id_igreja, \
                total_coletas, \
                valor_depositado, \
                despesa_manutencao, \
                construcao_retido, \
                assinada_anciao, \
                assinada_auxiliar_escrita, \
                assinada_cooperador, \
                assinada_diacono, \
                    assinada_porteiro in cursor:
                _prestacao_contas = PrestacaoContas(id_prestacao_contas,
                                                    id_igreja,
                                                    total_coletas,
                                                    valor_depositado,
                                                    despesa_manutencao,
                                                    construcao_retido,
                                                    assinada_anciao,
                                                    assinada_auxiliar_escrita,
                                                    assinada_cooperador,
                                                    assinada_diacono,
                                                    assinada_porteiro)

            return _prestacao_contas
        except mysql.connector.Error as mysql_error:
            raise mysql_error

    @staticmethod
    def atualizar(_prestacao_contas):
        try:
            _open_con()
            sql = "UPDATE TB_PRESTACAO_CONTAS " \
                  "SET " \
                  "id_igreja = %(id_igreja)s, " \
                  "total_coletas = %(total_coletas)s, " \
                  "valor_depositado = %(valor_depositado)s, " \
                  "despesa_manutencao = %(despesa_manutencao)s, " \
                  "construcao_retido = %(construcao_retido)s, " \
                  "assinada_anciao = %(assinada_anciao)s, " \
                  "assinada_auxiliar_escrita = %(assinada_auxiliar_escrita)s, " \
                  "assinada_cooperador = %(assinada_cooperador)s, " \
                  "assinada_diacono = %(assinada_diacono)s, " \
                  "assinada_porteiro = %(assinada_porteiro)s " \
                  "WHERE id_prestacao_contas = %(id)s "

            cursor.execute(sql, {"id_igreja": _prestacao_contas.id_igreja,
                                 "total_coletas": _prestacao_contas.total_coletas,
                                 "valor_depositado": _prestacao_contas.valor_depositado,
                                 "despesa_manutencao": _prestacao_contas.despesa_manutencao,
                                 "construcao_retido": _prestacao_contas.construcao_retido,
                                 "assinada_anciao": _prestacao_contas.assinada_anciao,
                                 "assinada_auxiliar_escrita": _prestacao_contas.assinada_aux_escrita,
                                 "assinada_cooperador": _prestacao_contas.assinada_cooperador,
                                 "assinada_diacono": _prestacao_contas.assinada_diacono,
                                 "assinada_porteiro": _prestacao_contas.assinada_porteiro,
                                 "id": _prestacao_contas.id})
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
            sql = """DELETE FROM TB_PRESTACAO_CONTAS 
                           WHERE id_prestacao_contas = %(id)s"""
            cursor.execute(sql, {"id": _id})
            cnx.commit()
            return 0
        except mysql.connector.Error as mysql_error:
            raise mysql_error
        finally:
            cursor.close()
            cnx.close()
