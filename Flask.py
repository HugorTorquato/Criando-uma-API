# Parte 1

from flask import Flask, jsonify, Request
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import os

    # jsonify e os -> Servem para transformar um array para o formato jason
    #              -> e para acessar as portas do ambiente no Heroku respectivamente

# Parte 2

app = Flask(__name__)

    # Cria um app web usando Flask. Variável app recebe o objeto Flask
    # a variável app vai ser usada para criar a rota e iniciar nosso serviço

# Parte 3

@app.route('/api/v1/filmes', methods=['GET'])
def filmes():
    
    # Parte 3.1
    html_doc = urlopen("http://www.adorocinema.com/filmes/numero-cinemas/").read()
    soup = BeautifulSoup(html_doc, "html.parser")

        # Carrega o HTML do site na variável HTML_DOC e o resultado do BealtifulSoup em soup

    # Parte3.2
    data = []
    for dataBox in soup.find_all("li", class_="mdl"):
        nomeObj = dataBox.find("h2", class_="meta-title").find("a", class_"meta-title-link")
        imgObj  = dataBox.find(class_="thumbnail-img")
        sinopseObj = dataBox.find("div", class_"synopsis").find("content-txt")
        dataObj = dataBox.find("div", class_"meta-body-item meta-body-info").find("span", class_="date")

        # um for para percorrer todos os atributos class igual a mdl. Cada um dos filmes
        # Chama o metodo find da variável dataBox (criada no for), tbm chamado de a tag do DOM onde a informação s encontra
        
        # Parte 3.3
        data.append({'nome': nomeObj.text.strip(),
                    'poster': imgObj.img['src'}].strip(),
                    'sinopse': sinopseObj.text.strip(),
                    'data': dataObj.text.strip()})

            # Joga o objeto montado dentro do array data, será feito várias vezes até o laço chegar ao fim
        

        

    return jsonify({'filmes' : data})


    # @app.rout -> Fala qual o caminho de acesso e qual verbo HTTP será utilizado

    # -> MEU CÓDIGO AQUI -> Uma função que será chamada ao acessar p caminho

# Parte 4

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

    # Definimos alguns parâmetros de ambiente
    # port -> recebe alguma porta disponível ou a 5000 padrão
    # hosto -> 127.0.0.1(localhost) para o Heroku tem de colocar 0.0.0.0, ele seta


#if __name__ == "__main__":
#    app.run(debug=True)
