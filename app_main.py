import flask
from flask import request, jsonify
from scripts.deteta_erros import *
from flask_cors import CORS
from scripts.verificar_sinonimos import *

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
@app.route('/true/detetarErros', methods=['POST', 'GET'])
def detetaErros():
    if request.method == 'POST':
        #Verifica se algum campo está vazio
        if(request.form['conteudo_noticia'] == "" and request.form['conteudo_format'] == ""):
            return jsonify({'estado': "As variáveis submetidas estão vazias"})

        elif request.form['conteudo_format'] == "":
            titulo_noticia = request.form['conteudo_noticia']
            erros_corrigir = recebeTextoParaDetetar(titulo_noticia)
       
            return jsonify({
                'estado': "enviado correção",
                'sugestoes_erros': erros_corrigir[0], 
                'palavrasErradas': erros_corrigir[1],
                'palavraSinonimo': erros_corrigir[2],
                'lista_palavrasBemMal': erros_corrigir[3],
                'lista_posPalavras': erros_corrigir[4],
                'lista_posPalavrasCorret': erros_corrigir[5],
                 })

        else:
            titulo_noticia = request.form['conteudo_noticia']
            erros_corrigir = recebeTextoParaDetetar(titulo_noticia)
          
            return jsonify({
                'estado': "enviado correção",
                'sugestoes_erros': erros_corrigir[0], 
                'palavrasErradas': erros_corrigir[1],
                'palavraSinonimo': erros_corrigir[2],
                'lista_palavrasBemMal': erros_corrigir[3],
                'lista_posPalavras': erros_corrigir[4],
                'lista_posPalavrasCorret': erros_corrigir[5],
                 })

    return "Não recebemos informação porque está em GET"

@app.route('/true/sinonimos', methods=['POST', 'GET'])
def apresentaSinonimos():
    if request.method == 'POST':
        if(request.form['sinonimos'] == ""):
            return jsonify({'estado': "As variáveis submetidas estão vazias"})
        else:
            palavra_pesquisar = request.form['sinonimos']
            sinonimos_Sistema = procurarSinonimos(palavra_pesquisar)
            print(palavra_pesquisar)
            print("-------------------------")
            print(sinonimos_Sistema)
            return jsonify({
                'estado': "enviado sinonimo",
                'palavras_enviados': sinonimos_Sistema, })

    return "Não recebemos informação porque está em G"

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=80)