# Tech-learn

Projeto desenvolvido para a disciplina 251-cc-grupo1, com o objetivo de facilitar o aprendizado de conceitos de Python e programação, integrando recursos de glossário, colaboração em equipe e interação com IA generativa.

## 👥 Equipe

- Allan Lucas ([GitHub](https://github.com/LukazAllan) | [LinkedIn](https://www.linkedin.com/in/allan-ribeiro-8ba407365/))
- Felipe Duarte ([GitHub](https://github.com/FelipeDoart) | [LinkedIn](https://www.linkedin.com/in/felip-duart-483481368/))
- Frankk Antonio ([GitHub](https://github.com/FrankkAntonio) | [LinkedIn](https://www.linkedin.com/in/frankk-antonio-37526725b/))
- Fernando Silva ([GitHub](https://github.com/fernandosllnetto) | [LinkedIn](https://www.linkedin.com/in/fernando-neto-86a47527a/))

## 🚀 Tecnologias Utilizadas

- **Python 3.11.2**
- **Flask 3.1.1** — Framework web
- **Google Gemini (google-genai==1.18.0)** — Integração com IA generativa
- **Bootstrap 5** — Estilização responsiva
- **CSV** — Armazenamento dos termos do glossário

## 📚 Funcionalidades

- **Glossário Dinâmico:** Consulte, adicione, edite e remova termos e definições sobre Python e programação.
- **Interação com IA:** Faça perguntas diretamente ao Google Gemini e obtenha respostas inteligentes.
- **Página Sobre:** Conheça os colaboradores do projeto, com links para GitHub e LinkedIn.
- **Interface Responsiva:** Layout moderno e adaptável para diferentes dispositivos.
- **Persistência de Dados:** Todos os termos são salvos em um arquivo CSV, garantindo fácil manutenção e portabilidade.

## 🏁 Como Executar

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/seu-usuario/tech-learn.git
   cd tech-learn
   ```

2. **Crie e ative um ambiente virtual:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Adicione sua chave da API Gemini:**
   - Crie um arquivo chamado `minha_chave.key` na raiz do projeto e cole sua chave da API.

5. **Execute o servidor Flask:**
   ```sh
   python app.py
   ```

6. **Acesse no navegador:**
   ```
   http://127.0.0.1:5000/
   ```

## 📁 Estrutura de Pastas

```
.
├── app.py
├── banco_de_dados.py
├── bd_glossario.csv
├── requirements.txt
├── static/
│   ├── css/
│   └── imagens/
├── templates/
│   ├── modelo.html
│   ├── glossario.html
│   ├── gemini.html
│   ├── sobre.html
│   └── ...
└── ...
```

## 📝 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido por [Allan Lucas](https://github.com/LukazAllan), [Felipe Duarte](https://github.com/FelipeDoart), [Frankk Antonio](https://github.com/FrankkAntonio) e [Fernando Silva](https://github.com/fernandosllnetto).
