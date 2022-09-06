import flask
from flask import request, jsonify,render_template
from verificarEntidades import *

app = flask.Flask(__name__)
# app.config["DEBUG"] = True
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

@app.route('/enviarspacy', methods=['POST', 'GET'])
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



# app.run(debug=True)

if __name__ == '__main__':  
    app.debug = True
    app.run(host="0.0.0.0")