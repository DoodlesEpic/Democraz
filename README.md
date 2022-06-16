# Democraz Brasil

Devido a frustação com o website do governo brasileiro para a Câmara dos Deputados desenvolvemos esse pequeno website em Python Django para exibir projetos de lei, consumindo diretamente a API de Dados Abertos da Câmara dos Deputados.

## Demonstração

![Print da tela mostrando a lista de PECs no website](https://user-images.githubusercontent.com/37254797/173978013-09c171c1-5319-4305-b948-6ebbb167c0f4.png)

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

## Licença

Todo o programa está englobado na licença GNU Affero General Public License v3, cheque o arquivo LICENSE para detalhes de o que pode ou não fazer com o código.
