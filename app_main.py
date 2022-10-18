import json
import flask
from flask import request, jsonify
from scripts.deteta_erros import checkText
from flask_cors import CORS
from scripts.verificar_sinonimos import procurarSinonimos
from scripts.check_plagiarism import checkPlagirism

app = flask.Flask(__name__)

CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/name')
def example():
    return 'The value of __name__ is {}'.format(__name__)

@app.route('/')
def index():
    return """
    <h1 style='color: #1F8598;'>TRUE Projeto!</h1>
    <p>Universidade de Aveiro</p>
    <code>Código que retorna um conjunto de entidades para um título e um conteúdo  </em></code>
    """

#""" Rota para detetar erros no texto escrito"""
@app.route('/true/detetarErros', methods=['POST'])
def detetaErros():
    text = request.form['conteudo_noticia']
    if(text == "" ):
        return jsonify({'estado': "As variáveis submetidas estão vazias"})

    else:
        results = checkText(text)
        jsdata = json.dumps({"results": results})
        return jsdata

@app.route('/true/sinonimos', methods=['POST'])
def apresentaSinonimos():
    word = request.form['sinonimos']
    if(word == ""):
        return jsonify({'estado': "As variáveis submetidas estão vazias"})
    else:
        sinonimos = procurarSinonimos(word)
        return jsonify({
            'estado': "enviado sinonimo",
            'palavras_enviados': sinonimos, })

@app.route('/true/plagcheck', methods=['POST'])
def checkPlagerism():
    text = request.form['text']
    if(text == ""):
        return jsonify({'estado': "As variáveis submetidas estão vazias"})
    else:
        results = checkPlagirism(text)
        jsdata = json.dumps({"results": results})
        return jsdata

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=80)