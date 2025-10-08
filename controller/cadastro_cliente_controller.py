from flask import Blueprint, request, jsonify
from model import cadastro_cliente_model
from model.cadastro_cliente_model import *

cadastro_clientes_blueprint = Blueprint('cadastro_clientes', __name__)


@cadastro_clientes_blueprint.route("/clientes", methods=['GET'])
def listarClientes():
    """
    Lista todos os clientes.
    ---
    description: Retorna todos os clientes cadastrados no sistema.
    tags:
      - Clientes
    responses:
      200:
        description: Lista de clientes retornada com sucesso.
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              cnpj:
                type: string
                example: "12345678000199"
              razao_social:
                type: string
                example: "Empresa Exemplo LTDA"
              email:
                type: string
                example: "contato@empresa.com"
              senha:
                type: string
                example: "senha123"
              telefone:
                type: string
                example: "(11) 99999-9999"
              cep:
                type: string
                example: "01234-567"
              logradouro:
                type: string
                example: "Rua das Flores"
              numero:
                type: string
                example: "123"
              complemento:
                type: string
                example: "Sala 1"
              bairro:
                type: string
                example: "Centro"
              cidade:
                type: string
                example: "São Paulo"
              estado:
                type: string
                example: "SP"
      500:
        description: Erro interno ao listar clientes.
    """
    
    try:
        clientes = cadastro_cliente_model.getClientes()
        return jsonify(clientes), 200
    except Exception as e:
        print(f"Erro ao listar clientes: {e}") 
        return jsonify({'erro': str(e)}), 500
    

@cadastro_clientes_blueprint.route("/clientes/<int:id_cliente>", methods=['GET'])
def listarClienteId(id_cliente):
    """
    Busca um cliente pelo ID.
    ---
    description: Retorna os dados de um cliente específico pelo ID.
    tags:
      - Clientes
    parameters:
      - in: path
        name: id_cliente
        required: true
        type: integer
        description: ID do cliente a ser retornado.
    responses:
      200:
        description: Cliente encontrado.
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            cnpj:
              type: string
              example: "12345678000199"
            razao_social:
              type: string
              example: "Empresa Exemplo LTDA"
            email:
              type: string
              example: "contato@empresa.com"
            senha:
              type: string
              example: "senha123"
            telefone:
              type: string
              example: "(11) 99999-9999"
            cep:
              type: string
              example: "01234-567"
            logradouro:
              type: string
              example: "Rua das Flores"
            numero:
              type: string
              example: "123"
            complemento:
              type: string
              example: "Sala 1"
            bairro:
              type: string
              example: "Centro"
            cidade:
              type: string
              example: "São Paulo"
            estado:
              type: string
              example: "SP"
      404:
        description: Cliente não encontrado.
      500:
        description: Erro interno no servidor.
    """

    try:
        cliente = cadastro_cliente_model.getClienteId(id_cliente)
        if cliente:
            return jsonify(cliente), 200
        else:
            return jsonify({'erro': 'Usuário não encontrado'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 500


@cadastro_clientes_blueprint.route("/clientes", methods=['POST'])
def cadastrarClientes():
    """
    Cria um novo cliente.
    ---
    description: Cria um novo registro de cliente no sistema.
    tags:
      - Clientes
    parameters:
      - in: body
        name: body
        required: true
        description: Dados completos do cliente a ser cadastrado.
        schema:
          type: object
          required:
            - cnpj
            - razao_social
            - email
            - senha
            - telefone
            - cep
            - logradouro
            - numero
            - bairro
            - cidade
            - estado
          properties:
            cnpj:
              type: string
              example: "12345678000199"
            razao_social:
              type: string
              example: "Empresa Exemplo LTDA"
            email:
              type: string
              example: "contato@empresa.com"
            senha:
              type: string
              example: "senha123"
            telefone:
              type: string
              example: "(11) 99999-9999"
            cep:
              type: string
              example: "01234-567"
            logradouro:
              type: string
              example: "Rua das Flores"
            numero:
              type: string
              example: "123"
            complemento:
              type: string
              example: "Sala 1"
            bairro:
              type: string
              example: "Centro"
            cidade:
              type: string
              example: "São Paulo"
            estado:
              type: string
              example: "SP"
    responses:
      201:
        description: Cliente criado com sucesso.
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Cliente cadastrado com sucesso"
            statusDB:
              type: string
              example: "1"
      400:
        description: Erro de validação dos dados enviados.
    """

    dados = request.get_json(silent=True)   
    r, erro = cadastro_cliente_model.postClientes(dados)
    if erro:
        return jsonify({'erro': erro}), 400
        
    return jsonify({"message":"Usuário cadastrado com sucesso", "statusDB" : r}), 201


@cadastro_clientes_blueprint.route("/clientes/<int:id_clientes>", methods=['PUT'])
def atualizarClientesId(id_clientes):
    """
    Atualiza um cliente existente.
    ---
    description: Atualiza os dados de um cliente pelo ID.
    tags:
      - Clientes
    parameters:
      - in: path
        name: id_cliente
        required: true
        type: integer
        description: ID do cliente a ser atualizado.
      - in: body
        name: body
        required: true
        description: Campos a serem atualizados do cliente.
        schema:
          type: object
          properties:
            cnpj:
              type: string
              example: "12345678000199"
            razao_social:
              type: string
              example: "Nova Empresa LTDA"
            email:
              type: string
              example: "novoemail@empresa.com"
            senha:
              type: string
              example: "novaSenha123"
            telefone:
              type: string
              example: "(11) 98888-8888"
            cep:
              type: string
              example: "01234-567"
            logradouro:
              type: string
              example: "Rua Nova"
            numero:
              type: string
              example: "456"
            complemento:
              type: string
              example: "Sala 2"
            bairro:
              type: string
              example: "Centro"
            cidade:
              type: string
              example: "São Paulo"
            estado:
              type: string
              example: "SP"
    responses:
      200:
        description: Cliente atualizado com sucesso.
      404:
        description: Cliente não encontrado.
      400:
        description: Erro na requisição.
    """
    
    dados = request.get_json(silent=True)
    try:
        atualizado = cadastro_cliente_model.putClientePorId(id_clientes, dados)
        if atualizado:
            return jsonify({'mensagem': 'Carga atualizada com sucesso'}), 200
        else:
            return jsonify({'erro': 'Carga não encontrada'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 400


@cadastro_clientes_blueprint.route("/clientes/<int:id_clientes>", methods=['DELETE'])
def apagarClientesId(id_clientes):
    """
    Deleta um cliente pelo ID.
    ---
    description: Remove um cliente específico do sistema pelo ID.
    tags:
      - Clientes
    parameters:
      - in: path
        name: id_cliente
        required: true
        type: integer
        description: ID do cliente a ser removido.
    responses:
      200:
        description: Cliente deletado com sucesso.
      404:
        description: Cliente não encontrado.
      400:
        description: Erro na requisição.
    """
    
    try:
        deletado = cadastro_cliente_model.deleteClientePorId(id_clientes)
        if deletado:
            return jsonify({'mensagem': 'Carga deletada com sucesso'}), 200
        else:
            return jsonify({'erro': 'Carga não encontrada'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 400


@cadastro_clientes_blueprint.route("/clientes", methods=['DELETE'])
def apagarTodosClientes():
    """
    Deleta todos os clientes.
    ---
    description: Remove todos os clientes cadastrados no sistema.
    tags:
      - Clientes
    responses:
      200:
        description: Todos os clientes foram removidos com sucesso.
        schema:
          type: object
          properties:
            mensagem:
              type: string
              example: "Todos os clientes foram removidos"
      400:
        description: Erro ao tentar excluir os clientes.
    """
    
    try:
        resposta,erro = cadastro_cliente_model.deleteTodosClientes()
        return jsonify(resposta), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 400