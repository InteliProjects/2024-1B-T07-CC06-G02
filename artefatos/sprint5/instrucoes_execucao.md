# Guia de Instalação e Execução da Aplicação

&emsp;&emsp;Este documento fornece instruções detalhadas para a preparação do ambiente de desenvolvimento, instalação e execução da aplicação, que é composta por um backend desenvolvido em Python e um frontend desenvolvido em React. Além disso, também cobre a execução do algoritmo isoladamente e a análise de seus resultados.

## Instruções para Preparação do Ambiente de Desenvolvimento

### Ferramentas e Dependências

1. **Ferramentas Essenciais**

    - **Editor de Código:** Use o editor de sua preferência, como VSCode, Sublime Text ou PyCharm.
    - **Git:** Necessário para clonar o repositório do projeto.
    - **Terminal:** Para rodar comandos de instalação e execução.
    - **Python e Node:** Necessários para o backend e frontend, respectivamente.

2. **Dependências do Sistema Operacional**
    - **Sistema Operacional:** O desenvolvimento foi realizado em Windows, mas o projeto é compatível com outros sistemas operacionais que suportem Python e Node.

### Setup do Ambiente

1. **Configuração do Sistema Operacional**

    - Não há configurações específicas de variáveis de ambiente ou permissões de usuário necessárias.

2. **Ambiente Virtual**
    - **Python:** Recomenda-se a criação de um ambiente virtual utilizando `venv`.
        ```sh
        python -m venv venv
        source venv/bin/activate # Linux/Mac
        .\venv\Scripts\activate # Windows
        ```

### Clonagem do Repositório

1. **Clonagem do Repositório**
    - Acesse o GitHub, copie o link do repositório e execute o seguinte comando no terminal:
        ```sh
        git clone <link-do-repositório>
        ```

## Instruções para a Instalação/Implantação da Aplicação

### Backend

1. **Instalação das Dependências**

    - Navegue até o diretório do backend e execute:
        ```sh
        pip install -r requirements.txt
        ```

2. **Início do Servidor**
    - Para iniciar o servidor, execute:
        ```sh
        python app.py
        ```
    - O servidor rodará na porta 5000.

### Frontend

1. **Instalação das Dependências**

    - Navegue até o diretório do frontend e execute:
        ```sh
        npm install
        ```

2. **Início do Servidor de Desenvolvimento**
    - Para iniciar o servidor de desenvolvimento, execute:
        ```sh
        npm start
        ```
    - O servidor rodará na porta 3000.

### Algoritmo de Forma Isolada

1. **Execução do Algoritmo**

    - Certifique-se de que as bibliotecas necessárias estão instaladas:
        ```sh
        pip install pandas scikit-learn haversine networkx numpy tqdm
        ```
    - Para executar o algoritmo, execute:
        ```sh
        python new_algorithm.py
        ```

2. **Formato dos Dados de Entrada**

    - O arquivo CSV de dados deve conter as seguintes colunas: `INDICE`, `LATITUDE`, `LONGITUDE`, `CODIGO_ROTA`, `SEQUENCIA`, `LOGRADOURO`, `NUMERO`.

3. **Arquivo de Resultados**
    - Um arquivo com as rotas resultantes será gerado após a execução.

### Análise de Resultados e Visualização dos Dados em Desenvolvimento

1. _Jupyter Notebook_
    - Utilize Jupyter Notebook para análise de resultados.
    - Conecte o notebook ao kernel Python instalado na máquina.
    - Arquivos disponíveis para análise:
        - new_algorithm_analysis.ipynb: Análise dos resultados do algoritmo.
        - cluster_analysis.ipynb: Análise dos clusters gerados antes da execução do algoritmo.

## Execução e Testes

1. _Testes Automatizados_
    - Utilize Flask-Testing e unittest para rodar os testes.
    - Instale as dependências de teste:
        ```sh
        pip install Flask-Testing unittest
        ```
    - Execute os testes com:
        ```sh
        python test_app.py
        ```

### Documentação e Recursos Adicionais

1. _Documentação_
    - Toda a documentação necessária para a aplicação, algoritmo, testes e análise dos resultados está disponível no repositório do GitHub fornecido pelo Inteli.

Com essas instruções, você deve estar apto a configurar, instalar e executar a aplicação de forma eficiente. Certifique-se de seguir cada etapa cuidadosamente para garantir o correto funcionamento do ambiente de desenvolvimento e da aplicação em si.
