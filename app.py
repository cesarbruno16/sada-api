import os
from flask import Flask, request, json
from werkzeug.exceptions import BadRequest
from Dao.Usuario import Usuario
from passlib.hash import pbkdf2_sha256
from flask_cors import CORS

app = Flask(__name__)

app.url_map.strict_slashes = False
app.secret_key = b"\xe6\xfaJ'\xda\xf1\xc48\x06\x14\x85by\xbb$\x01"

CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World! Sua api funciona!'


@app.route('/login/', methods=["GET", "POST"])
def login():
    try:
        _dados = request.get_json(force=True)
    except Exception as exc:
        print(exc)
        try:
            _dados = request.form
        except Exception as exc:
            print(exc)
            try:
                _dados = request.values
            except KeyError as kerr:
                print(kerr)
                return json.dumps({"Error": "KeyError"}), 406
            except BadRequest as brq:
                print(brq)
                return json.dumps({"Error": "BadRequest"}), 406

    try:
        _email = _dados['email']
        _senha = _dados['senha']
        _usuario = Usuario.obter_usuario_por_email(_email)
        if _usuario is not None:
            if _usuario.login == _email and pbkdf2_sha256.verify(_senha, _usuario.hash):
                _ = os.urandom(64).hex()
                _usuario.set_token(str(_))
                return json.dumps({"token": str(_)}), 200
            return json.dumps({"Erro": "Usuario ou senha incorretos"}), 401
        return json.dumps({"Erro": "Usuario ou senha incorretos"}), 401
    except Exception as exc:
        print(exc)
        return json.dumps({"Erro": "Nao autorizado"}), 401


def _check_token(_request):
    if Usuario.obter_token_por_email(_request.form['email']) == _request.form['token']:
        return True
    return False


if __name__ == '__main__':
    app.run()
