**Versão do python utilizada:** 3.8.2

**Versão do pip utilizada:** 20.0.2

**Configuração inicial no Windows 10**
1. Clone o repositório
2. Crie uma pasta com o nome venv dentro do repositório
3. Abra o terminal dentro do repositório
4. Crie o ambiente virtual com o comando `python -m venv \venv`
5. Ative o ambiente virtual criado com o comando `.\venv\Scripts\activate`
6. No terminal, vai aparecer (venv) antes do comando. Isso significa que o ambiente virtual está ativado
7. Verifique a versão do pip com o comando
`pip --version`
8. Atualize o pip se for necessário com o comando `python -m pip install --upgrade pip`
9. Instale as dependências do projeto (arquivo requirements.txt) com o comando `pip install -r requirements.txt`
10. Instale também o driver de conexão com o banco de dados MySQL. Para isso, baixe o arquivo _mysqlclient‑1.4.6‑cp38‑cp38‑win32.whl_ do site https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python e instale com o comando `pip install mysqlclient-1.4.6-cp38-cp38-win32.whl
`
11. Crie o banco de dados no seu servidor MySQL e edite as configurações de acesso no arquivo _settings.py_

Certifique-se de ativar o ambiente virtual antes de utilizar o projeto