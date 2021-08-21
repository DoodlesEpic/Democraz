# Democraz Brasil

Devido a frustação com o website do governo brasileiro para a Câmara dos Deputados desenvolvemos esse pequeno website em Python Django para exibir projetos de lei, consumindo diretamente a API de Dados Abertos da Câmara dos Deputados.

## Demonstração
<<<<<<< HEAD

![Print da tela mostrando a lista de PECs no website](https://user-images.githubusercontent.com/37254797/130305294-de214b0a-c884-45dc-9a36-faa0b459e205.png)
=======
![Print da tela mostrando a lista de PECs no website](https://user-images.githubusercontent.com/37254797/130308506-fc1c6443-5815-4fc5-bd82-8d72940d4018.png)
>>>>>>> ec64c40 (Atualizar print do README)

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
