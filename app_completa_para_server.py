import flask
from flask import request, jsonify,render_template
from verificarEntidades import *
from detetaErros import *
import enchant
from flask_cors import CORS
from verificarSinonimos import *


app = flask.Flask(__name__)
# app.config["DEBUG"] = True

CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/name')
def example():
    
    return 'The value of __name__ is {}'.format(__name__)


@app.route('/')
def index():
    # return json.dumps({'name': 'alice',
    #                    'email': 'alice@outlook.com'})

    # return jsonify({'name': 'alice',
    #                'email': 'alice@outlook.com'})
    #return render_template('index.html')

    return """
    <h1 style='color: #1F8598;'>TRUE Projeto!</h1>
    <p>Universidade de Aveiro</p>
    <code>Código que retorna um conjunto de entidades para um título e um conteúdo  </em></code>
    """

@app.route('/true/enviarspacy', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':

        if(request.form['titulo_noticia'] == "" and request.form['conteudo'] == ""):
            print("Pelo menos uma das variáveis submetidas está vazia")
            return jsonify({'estado': "As variáveis submetidas estão vazias"})
        elif(request.form['titulo_noticia'] == "" or request.form['conteudo'] == ""):
            print("Pelo menos uma das variáveis submetidas está vazia")
            return jsonify({'estado': "Pelo menos uma das variáveis submetidas está vazia"})
        else:
            titulo_noticia = request.form['titulo_noticia']
            conteudo_pro = request.form['conteudo']
            

            entidades_titulo = encontrarEntidades(titulo_noticia)
            entidades_conteudos = encontrarEntidades(conteudo_pro)
            print("-------------------------")
            #print(entidades_titulo)
            return jsonify({'estado': "enviado para o spaCy com sucesso 😉", 'titulo_noticia': titulo_noticia, 'conteudo': conteudo_pro, 'entidades_titulo': entidades_titulo, 'entidades_conteudos': entidades_conteudos })


    return "Não recebemos informação"



#""" Rota para detetar erros no texto escrito"""
@app.route('/true/detetarErros', methods=['POST', 'GET'])
def detetaErros():
    if request.method == 'POST':
        #Verifica se algum campo está vazio
        if(request.form['conteudo_noticia'] == "" and request.form['conteudo_format'] == ""):
            return jsonify({'estado': "As variáveis submetidas estão vazias"})
        elif request.form['conteudo_format'] == "":
            titulo_noticia = request.form['conteudo_noticia']
            array_InfoFormat = ""
            erros_corrigir = recebeTextoParaDetetar(titulo_noticia, array_InfoFormat)
       
            return jsonify({
                'estado': "enviado correção",
                'Html_erros': erros_corrigir[0],
                'sugestoes_erros': erros_corrigir[1], 
                'palavrasErradas': erros_corrigir[2],
                'palavraSinonimo': erros_corrigir[3] })

        else:
            titulo_noticia = request.form['conteudo_noticia']
            array_InfoFormat = request.form['conteudo_format']
            erros_corrigir = recebeTextoParaDetetar(titulo_noticia, array_InfoFormat)
          
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
    print("_-----___ Entras aqui????")
    if request.method == 'POST':
        if(request.form['sinonimos'] == ""):
            #print("Pelo menos terá que escrever alguma coisa")
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



# app.run(debug=True)
#
if __name__ == '__main__':  
    #app.debug = True
    #app.run(host="0.0.0.0")
    #app.run(host='0.0.0.0', port=443)
    app.run(host='0.0.0.0', port=80)
    #app.run()  