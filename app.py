import csv
from os import write
from os.path import exists
from flask import Flask, render_template, request, url_for, redirect
from google import genai
import banco_de_dados

app = Flask(__name__)
MODEL = "gemini-2.0-flash"
BANCO_DE_DADOS = 'bd_glossario.csv'
GLOSSARIO = banco_de_dados.Handler(BANCO_DE_DADOS)

# Variável Constante que guarda os membros do nosso grupo
EQUIPE = [
{"nome": "Felipe Duarte","link_github":"https://github.com/FelipeDoart","link_linkedin":"https://www.linkedin.com/in/felip-duart-483481368/"},
{"nome": "Frankk Antonio","link_github":"https://github.com/FrankkAntonio","link_linkedin":"https://www.linkedin.com/in/frankk-antonio-37526725b/"},
{"nome": "Allan Lucas","link_github":"https://github.com/LukazAllan","link_linkedin":"https://www.linkedin.com/in/allan-ribeiro-8ba407365/"},
{"nome": "Fernando Silva","link_github":"https://github.com/fernandosllnetto","link_linkedin":"https://www.linkedin.com/in/fernando-neto-86a47527a/"}
]

# Configuração da API do Google GenAI
if exists('minha_chave.key'):
    with open('minha_chave.key', 'r') as file:
        API_KEY = file.read().strip()
else:
    # Se a chave não existir, você pode definir uma chave padrão ou lidar com o erro
    raise Exception("Chave API não encontrada. Crie um arquivo 'minha_chave.key' com sua chave API.")

client = genai.Client(api_key=API_KEY)

def request_gemini(query):
    # Exemplo de requisição para o modelo Gemini
    # Aqui você pode personalizar a consulta conforme necessário
    response = client.models.generate_content(
        model=MODEL,
        contents=query
    )
    print(response.text)
    return response.text


@app.route('/')
def ola():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', equipe=EQUIPE)

@app.route('/glossario')
def glossario(alert=""):
    if alert != "":
        return render_template('glossario.html', glossario=GLOSSARIO.get_termos(), alert=alert)
    return render_template('glossario.html', glossario=GLOSSARIO.get_termos())


@app.route('/novos_termos')
def novos_termos():
    return render_template('novos_termos.html')

@app.route('/criar_termo', methods=['POST'])
def criar_termo():
    termo = request.form['termo']
    definicao = request.form['definicao']

    GLOSSARIO.adicionar_termo(termo, definicao)

    return redirect(url_for('glossario'))

@app.route('/remove_termo', methods=["POST"])
def remove_termo():
    try:
        index = int(request.form['index'])
    except TypeError:
        raise TypeError("Não foi possível converter a entra-0da de index para INT base 10")
    
    GLOSSARIO.remover_termo(index) 

    return redirect(url_for('glossario'))

@app.route('/editar_termo', methods=["POST"])
def editar_termo():
    try:
        index = int(request.form['index'])
    except TypeError:
        raise TypeError("Não foi possível converter a entrada de index para INT base 10")
    
    o_termo = GLOSSARIO.get_termo(index)[0]
    a_descricao = GLOSSARIO.get_termo(index)[1]
    return render_template('editar_termo.html', termo=o_termo, descricao=a_descricao, index=index)

@app.route('/alterar_termo', methods=["POST"])
def alterar_termo():
    o_request = list(request.form.items())
    if o_request[0][1] == "":
        return "Index Vazio"
    try:
        index = int(o_request[0][1])
    except TypeError:
        raise TypeError("Não foi possível converter a entrada de index para INT base 10")
    
    termo = o_request[1][1]
    definicao = o_request[2][1]

    GLOSSARIO.atualizar_termo(index, termo, definicao)

    return glossario("Termo alterado com Sucesso!")


@app.route('/gemini', methods=['GET', 'POST'])
def gemini():
    if request.method == 'POST':
        # print(request.form)
        question = request.form['conteudo']
        # print(question)
        resposta  = request.form['conteudo']
        #resposta  = request_gemini(question)
        return render_template('gemini.html', resposta=resposta, question=question)

    return render_template('gemini.html')

if __name__ == "__main__":
    # Ensure debug mode is only enabled during development
    app.run(debug=False)  # Set to True only during development


