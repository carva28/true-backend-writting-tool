# import flask
# from flask import request, jsonify
# from verificarEntidades import *

# app = flask.Flask(__name__)
# app.config["DEBUG"] = True


# @app.route('/')
# def index():
#     # return json.dumps({'name': 'alice',
#     #                    'email': 'alice@outlook.com'})
#     return jsonify({'name': 'alice',
#                    'email': 'alice@outlook.com'})

# # @app.route('/tests/endpoint', methods=['POST'])
# # def my_test_endpoint():
# #     input_json = request.get_json(force=True)
# #     # force=True, above, is necessary if another developer
# #     # forgot to set the MIME type to 'application/json'
# #     print('data from client:', input_json)
# #     dictToReturn = {'answer':42}
# #     return jsonify(dictToReturn)


# @app.route('/enviarspacy', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':

#         if(request.form['titulo_noticia'] == "" and request.form['conteudo'] == ""):
#             print("Pelo menos uma das variáveis submetidas está vazia")
#             return jsonify({'estado': "As variáveis submetidas estão vazias"})
#         elif(request.form['titulo_noticia'] == "" or request.form['conteudo'] == ""):
#             print("Pelo menos uma das variáveis submetidas está vazia")
#             return jsonify({'estado': "Pelo menos uma das variáveis submetidas está vazia"})
#         else:
#             titulo_noticia = request.form['titulo_noticia']
#             conteudo_pro = request.form['conteudo']
            

#             entidades_titulo = encontrarEntidades(titulo_noticia)
#             entidades_conteudos = encontrarEntidades(conteudo_pro)
#             print("-------------------------")
#             print(entidades_titulo)
#             return jsonify({'estado': "enviado para o spaCy com sucesso 😉", 'titulo_noticia': titulo_noticia, 'conteudo': conteudo_pro, 'entidades_titulo': entidades_titulo, 'entidades_conteudos': entidades_conteudos })


#     return "Não recebemos informação"


# app.run(debug=True)
