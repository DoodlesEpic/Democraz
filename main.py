from flask import Flask, render_template
import requests

app = Flask(__name__)
api_url = "https://dadosabertos.camara.leg.br/api/v2"


@app.route("/")
def main():
    try:
        request_url = api_url + "/proposicoes?itens=30&ordem=ASC&ordenarPor=id"
        response = requests.get(request_url)
        response.raise_for_status()
        data = response.json()

        return render_template("index.html", data=data)
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}", 500
