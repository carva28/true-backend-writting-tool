import json
import flask
from flask import request, jsonify
from scripts.deteta_erros import check_text
from flask_cors import CORS
from scripts.verificar_sinonimos import procurar_sinonimos
from scripts.check_plagiarism import check_plagirism

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
@app.route('/true/check-errors', methods=['POST'])
def check_errors():
    text = request.form['text']
    if text == "":
        return jsonify({'estado': "As variáveis submetidas estão vazias"})

    else:
        results = check_text(text)
        jsdata = json.dumps({"results": results})
        return jsdata

@app.route('/true/related-words', methods=['POST'])
def related_words():
    word = request.form['sinonimos']
    if word == "":
        return jsonify({'estado': "As variáveis submetidas estão vazias"})
    else:
        related_words = procurar_sinonimos(word)
        return jsonify({
            'estado': "enviado sinonimo",
            'palavras_enviados': related_words })

@app.route('/true/check-plagiarism', methods=['POST'])
def check_plagiarism():
    text = request.form['text']
    if text == "":
        return jsonify({'estado': "As variáveis submetidas estão vazias"})
    else:
        results = check_plagirism(text)
        jsdata = json.dumps({"results": results})
        return jsdata

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=80)