# Democraz Brasil

Devido a frustação com o website do governo brasileiro para a Câmara dos Deputados desenvolvemos esse pequeno website em Python para exibir projetos de lei, consumindo diretamente a API de Dados Abertos da Câmara dos Deputados.

## Demonstração

![Print da tela mostrando a lista de PECs no website](https://user-images.githubusercontent.com/37254797/173978013-09c171c1-5319-4305-b948-6ebbb167c0f4.png)

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
