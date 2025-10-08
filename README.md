🚚 **Sistema de Gerenciamento Logístico**


📌 **Visão Geral do Projeto**

Nosso projeto consiste no desenvolvimento de um Sistema de Gerenciamento Logístico, que permitirá otimizar processos, organizar dados e melhorar a eficiência de operações logísticas.

Durante toda a construção, utilizaremos Docker para criar, implantar e executar aplicações em containers, garantindo isolamento, portabilidade e eficiência no ambiente de desenvolvimento.


```
👥 Participantes

Ana Beatriz        RA:2401228

Luiz Otávio        RA:2401300

Murillo Rodrigues  RA:2400338

Uatila Santos      RA:2400250
```


🎯 **Objetivo**

Criar um sistema completo, com front-end, back-end e banco de dados, garantindo integração eficiente entre as camadas.

--------------------------------------------------------------


🛠️ **Tecnologias Utilizadas**

    - Python

    - Flask

    - Render

    - Docker

    - Swagger



-----------------------------------------------------------


⚙️ **Back-End**

A API será construída com:

Python → Linguagem principal pela simplicidade e flexibilidade
Flask → Microframework que oferece rapidez, escalabilidade e facilidade para construção de APIs REST


🗄 **Banco de Dados**

O banco será implementado com:

Postgress → Armazenamento seguro e eficiente
Suporte a APIs Postgress para melhor desempenho, segurança e integração padronizada


🐳 **Containerização**

Todo o projeto será conteinerizado com Docker, garantindo:
Isolamento do ambiente
Portabilidade
Facilidade de implantação

------------------------------------------------------------

🚀 **Como rodar o projeto**

▶️ **Como Executar a API localmente**

1.  Clone o repositório

    ```bash
    git clone https://github.com/luizotavio26/TrajettoExpressFullstack.git
    ```

2.  Crie um ambiente virtual (opcional, mas recomendado)

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    ```

3.  Instale as dependências

    ```bash
    pip install -r requirements.txt
    ```

4.  Execute a API

    ```bash
    python app.py
    ```

    A aplicação estará disponível em: 📍 http://localhost:5036

---

🐳 **Como Executar a API com Docker**

1.  Clone o repositório

    ```bash
    git clone https://github.com/luizotavio26/TrajettoExpressFullstack.git
    ```

2.  Construa a imagem Docker
    ```bash
    docker build -t manifesto-carga-api .
    ```

3.  Execute o container
    ```bash
    docker run -d -p 5036:5036 manifesto-carga-api
    ```

-----------------------------------------------------------

📌 **Diagrama de Deployment**

![Imagem Diagrama](https://github.com/user-attachments/assets/59aa53a0-aa70-406a-af29-11617cdd4fe1)



# Descrição dos Atributos do Banco de Dados

## 1. Tabela **clientes**

| Atributo      | Tipo            | Descrição                                                                                 |
|---------------|-----------------|-------------------------------------------------------------------------------------------|
| `id`          | Integer (PK)    | Identificador único de cada cliente no sistema.                                          |
| `cnpj`        | String(14)      | Cadastro Nacional da Pessoa Jurídica, único e obrigatório.                               |
| `razao_social`| String(100)     | Nome empresarial oficial do cliente, único e obrigatório.                               |
| `email`       | String(100)     | Endereço de e-mail para contato, único e obrigatório.                                   |
| `senha`       | String(128)     | Senha criptografada para autenticação do cliente.                                       |
| `telefone`    | String(20)      | Número de telefone para contato, único e obrigatório.                                   |
| `cep`         | String(9)       | Código de Endereçamento Postal do endereço.                                             |
| `logradouro`  | String(100)     | Nome da rua, avenida ou logradouro.                                                     |
| `numero`      | String(10)      | Número do imóvel/endereço.                                                              |
| `complemento` | String(50)      | Informações adicionais do endereço (opcional).                                         |
| `bairro`      | String(100)     | Bairro onde o cliente está localizado.                                                  |
| `cidade`      | String(100)     | Cidade do cliente.                                                                      |
| `estado`      | String(2)       | Unidade federativa (UF) do cliente, ex: SP, RJ.                                        |

---

## 2. Tabela **veiculos**

| Atributo       | Tipo           | Descrição                                                                               |
|----------------|----------------|-----------------------------------------------------------------------------------------|
| `id`           | Integer (PK)   | Identificador único de cada veículo.                                                   |
| `placa`        | String(7)      | Placa do veículo para identificação.                                                  |
| `modelo`       | String(50)     | Modelo do veículo.                                                                      |
| `marca`        | String(50)     | Marca do veículo.                                                                       |
| `renavan`      | String(11)     | Registro Nacional de Veículos Automotores.                                             |
| `chassi`       | String(17)     | Número do chassi do veículo, identificador único.                                     |
| `cor`          | String(50)     | Cor do veículo.                                                                         |
| `tipo`         | String(50)     | Tipo do veículo (ex: caminhão, van).                                                   |
| `ano_modelo`   | String(4)      | Ano do modelo do veículo.                                                              |
| `ano_fabricacao`| String(4)     | Ano de fabricação do veículo.                                                          |

---

## 3. Tabela **motoristas**

| Atributo         | Tipo           | Descrição                                                                                 |
|------------------|----------------|-------------------------------------------------------------------------------------------|
| `id`             | Integer (PK)   | Identificador único do motorista.                                                        |
| `nome`           | String(150)    | Nome completo do motorista.                                                              |
| `cpf`            | String(15)     | Cadastro de Pessoa Física, documento de identificação do motorista.                      |
| `rg`             | String(15)     | Registro Geral, documento de identidade.                                                 |
| `salario`        | Float          | Remuneração do motorista.                                                                |
| `data_nascimento`| Date           | Data de nascimento do motorista.                                                        |
| `numero_cnh`     | String(20)     | Número da Carteira Nacional de Habilitação (CNH).                                        |
| `categoria_cnh`  | String(10)     | Categoria da CNH, definindo os tipos de veículos que pode conduzir.                      |
| `validade_cnh`   | Date           | Data de validade da CNH.                                                                 |
| `telefone`       | String(20)     | Número de telefone para contato.                                                         |
| `email`          | String(100)    | Endereço de e-mail do motorista.                                                        |
| `endereco`       | String(100)    | Endereço residencial.                                                                    |
| `cidade`         | String(50)     | Cidade do motorista.                                                                     |
| `uf`             | String(50)     | Unidade federativa (UF) do endereço do motorista.                                        |
| `cep`            | String(50)     | Código postal do endereço.                                                               |

---

## 4. Tabela **manifesto_carga**

| Atributo             | Tipo           | Descrição                                                                                |
|----------------------|----------------|------------------------------------------------------------------------------------------|
| `id`                 | Integer (PK)   | Identificador único do manifesto de carga.                                              |
| `tipo_carga`         | String(50)     | Descrição do tipo de carga transportada.                                               |
| `peso_carga`         | Float          | Peso total da carga em quilogramas.                                                    |
| `origem_carga`       | String(200)    | Local de origem da carga.                                                               |
| `destino_carga`      | String(200)    | Local de destino da carga.                                                              |
| `valor_frete`        | Float          | Valor total do frete cobrado pelo transporte.                                           |
| `valor_km`           | Float          | Valor cobrado por quilômetro rodado.                                                   |
| `distancia`          | Float          | Distância total percorrida em quilômetros.                                             |
| `motorista_id`       | Integer (FK)   | Referência ao motorista responsável pelo transporte.                                   |
| `cliente_id`         | Integer (FK)   | Referência ao cliente dono da carga.                                                   |
| `veiculo_id`         | Integer (FK)   | Referência ao veículo utilizado no transporte.                                         |