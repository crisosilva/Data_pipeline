#Data Pipeline
Projeto de um pipeline de dados que se captura as tendecias do google trends, faz a conexão com um banco do Postgres, verifica se o registro
capturado ja consta na tabela, caso não haja o registro é realizada a inserção do mesmo.


##:Clipboard:Pré requisitos
Para utilizar o projeto será necessário instalar o Python 3 caso não tenha instalado além das bibliotecas utilizadas no projeto
Instalação do Python
Se o seu SO for o linux o Python já estará instalado, caso esteja utilizando o SO Windows o Python pode ser baixado e instalado em:
https://www.python.org/downloads/windows/

Acesse, baixe e siga as orientações de instalação.

Instalação das bibliotecas
Para instalar as bibliotecas utilize os comandos abaixo:

pip install pytrends
pip install psycopg2

:hammer_and_wrench: Construído com
O pipeline de dados foi construido utilizando a linguagem de programação Python a IDE PyCharm e as bilbiotecas pytrends.request.Trendreq, datetime.datetime e psycopg2

Possiveis Problemas
Durante a instalação da biblioteca psycopg2, um erro foi encontrado impossibilitando a instalação da biblioteca pelo gerenciador de pacotes PIP
o problema foi resolvido, utilizando o comando abaixo conforme referenciado no site da biblioteca: https://www.psycopg.org/docs/install.html

'''
$ export PATH=/usr/lib/postgresql/X.Y/bin/:$PATH
'''


:black_nib:Autores
Projeto criado por Cristiano Oliveira

pushpin Versão
Version: 1.0.0

Referências
https://pypi.org/project/pytrends/

