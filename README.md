# Democraz Brasil
Devido a frustação com o website do governo brasileiro para a Câmara dos Deputados desenvolvemos esse pequeno website em Python Django para exibir projetos de lei, consumindo diretamente a API de Dados Abertos da Câmara dos Deputados.

## Demonstração
![0388eacd-a41d-467a-98b1-f747bbd2bf21](https://user-images.githubusercontent.com/37254797/129986291-66f82333-44d5-4616-905e-5e2a15e64671.jpeg)

## Configurando o ambiente
Para desenvolver serão necessárias algumas bibliotecas para o Python (Django e Requests), a forma mais fácil de instalar isso é utilizando [Poetry](https://python-poetry.org/), instale ele no seu sistema seguindo as instruções do site e depois de clonar o repositório rode:
```sh
poetry install
```
Posteriormente para executar o servidor de testes localmente execute:
```sh
poetry run python manage.py runserver
```
O servidor deve iniciar e o link de acesso deve aparecer na janela do terminal.
