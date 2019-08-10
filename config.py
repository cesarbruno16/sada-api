# coding=utf-8
import configparser

config = configparser.ConfigParser()
if len(config.read('config.ini')) == 0:
    if len(config.read('../config.ini')) == 0:
        raise Exception('Arquivo config.ini não encontrado')


class Res(object):
    DB = config['DB']
