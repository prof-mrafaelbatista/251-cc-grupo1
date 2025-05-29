import csv
from os import write

from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)

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

app.run()


