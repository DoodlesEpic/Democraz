from flask import Flask, render_template, request
import requests

app = Flask(__name__)
api_url = "https://dadosabertos.camara.leg.br/api/v2"


@app.route("/")
def main():
    page = request.args.get("pagina", 1)

    try:
        # 1. Fetch the list of legislations
        list_url = (
            f"{api_url}/proposicoes?itens=30&ordem=ASC&ordenarPor=id&pagina={page}"
        )

        # Using a session for better performance with multiple requests
        with requests.Session() as session:
            response = session.get(list_url)
            response.raise_for_status()
            raw_data = response.json()

            legislations = raw_data.get("dados", [])

            enriched_data = []
            for legislation in legislations:
                detail_url = f"{api_url}/proposicoes/{legislation['id']}"
                detail_resp = session.get(detail_url)

                if detail_resp.status_code == 200:
                    extra_info = detail_resp.json().get("dados", {})
                    legislation.update(extra_info)

                enriched_data.append(legislation)

        return render_template("index.html", data=enriched_data, current_page=int(page))

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}", 500
