# Democraz Brasil

Devido a frustação com o website do governo brasileiro para a Câmara dos Deputados desenvolvemos esse pequeno website em Python para exibir projetos de lei, consumindo diretamente a API de Dados Abertos da Câmara dos Deputados.

## Demonstração

![Print da tela mostrando a lista de PECs no website](https://github.com/user-attachments/assets/b7f1306b-3cf0-4b2a-98fa-99e60a4b8da2)

## Configurando o ambiente

Para desenvolver são necessárias algumas bibliotecas para o Python, a forma mais fácil de instalar isso é utilizando o gerenciador de pacotes [uv](https://docs.astral.sh/uv/getting-started/installation/). Instale ele no seu sistema seguindo as instruções do site e, depois de clonar o repositório, rode:

```sh
uv install
```

Posteriormente, para executar o servidor localmente execute:

```sh
uv run python main.py
```

Com isso, o servidor de desenvolvimento deve tornar-se acessível.

## Licença

Todo o programa está englobado na licença GNU Affero General Public License v3. Cheque o arquivo LICENSE para detalhes de o que pode ou não fazer com o código.
