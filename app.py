import csv
from os import write
from os.path import exists
from flask import Flask, render_template, request, url_for, redirect
from google import genai

app = Flask(__name__)
MODEL = "gemini-2.0-flash"

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
    return render_template('sobre.html')

@app.route('/glossario')
def glossario():
    #Abertura do arquivo Glossario.csv
    glossario_termos = []
    with open('bd_glossario.csv', newline='' , encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter =';')

        #Criação de uma lista dos termos adicionando os termos
        for l in reader:
            glossario_termos.append(l)

    return render_template('glossario.html', glossario=glossario_termos)


@app.route('/novos_termos')
def novos_termos():
    return render_template('novos_termos.html')

@app.route('/criar_termo', methods=['POST'])
def criar_termo():

    termo = request.form['termo']
    definicao = request.form['definicao']

    with open('bd_glossario.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([termo, definicao])

    return redirect(url_for('glossario'))

@app.route('/gerar_conteudo', methods=['GET', 'POST'])
def gerar_conteudo():
    if request.method == 'POST':
        print(request.form)
        question = request.form['conteudo'].replace('\n', ' ').replace('+', " ")
        print(question)
        resposta  = request.form + "<br>" + question
        #resposta  = request_gemini(question)
        return render_template('gerar_conteudo.html', resposta=resposta, question=question)

    return render_template('gerar_conteudo.html')

app.run()


