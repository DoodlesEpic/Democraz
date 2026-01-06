from flask import Flask, render_template, request
import requests

app = Flask(__name__)
api_url = "https://dadosabertos.camara.leg.br/api/v2"


@app.route("/")
def main():
    page = request.args.get("pagina", 1)

    try:
        request_url = (
            f"{api_url}/proposicoes?itens=30&ordem=ASC&ordenarPor=id&pagina={page}"
        )
        response = requests.get(request_url)
        response.raise_for_status()
        data = response.json()

        return render_template("index.html", data=data, current_page=int(page))
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}", 500
