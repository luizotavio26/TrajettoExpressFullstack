from flask import Blueprint, request, jsonify
from model import motorista_model
from model.motorista_model import *
from config import db

motoristas_blueprint = Blueprint('motorista', __name__)


@motoristas_blueprint.route("/motoristas", methods=['POST'])
def criar_motoristas():
    """
    Cria um novo motorista.
    ---
    description: Registra um novo motorista no sistema.
    tags:
      - Motoristas
    parameters:
      - in: body
        name: body
        required: true
        description: Dados completos do motorista a ser criado.
        schema:
          type: object
          required:
            - nome
            - cpf
            - rg
            - salario
            - data_nascimento
            - numero_cnh
            - categoria_cnh
            - validade_cnh
            - telefone
            - email
            - endereco
            - cidade
            - uf
            - cep
          properties:
            nome: { type: string, example: "Carlos Silva" }
            cpf: { type: string, example: "12345678900" }
            rg: { type: string, example: "MG1234567" }
            salario: { type: number, example: 3500.50 }
            data_nascimento: { type: string, format: date, example: "1985-05-20" }
            numero_cnh: { type: string, example: "12345678900" }
            categoria_cnh: { type: string, example: "B" }
            validade_cnh: { type: string, format: date, example: "2028-05-20" }
            telefone: { type: string, example: "(11) 99999-9999" }
            email: { type: string, example: "carlos@email.com" }
            endereco: { type: string, example: "Rua A, 123" }
            cidade: { type: string, example: "São Paulo" }
            uf: { type: string, example: "SP" }
            cep: { type: string, example: "01234-567" }
    responses:
      201:
        description: Motorista criado com sucesso.
      400:
        description: Erro de validação dos dados enviados.
      500:
        description: Erro interno do servidor.
    """

    dados = request.get_json()
    try:
        novo_motorista, erro = motorista_model.create_motorista(dados)
        if erro:
            return jsonify({"erro": erro}), 400
        else:
            return jsonify(novo_motorista), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@motoristas_blueprint.route("/motoristas", methods=['GET'])
def listar_motoristas():
    """
    Lista todos os motoristas.
    ---
    description: Retorna todos os motoristas cadastrados no sistema.
    tags:
      - Motoristas
    responses:
      200:
        description: Lista de motoristas retornada com sucesso.
      500:
        description: Erro interno do servidor.
    """
    
    try:
        motoristas,erro = motorista_model.read_todos_motorista()
        return jsonify(motoristas), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500


@motoristas_blueprint.route("/motoristas/<int:id_motorista>", methods=['GET'])
def le_motoristas_id(id_motorista):
    """
    Busca um motorista pelo ID.
    ---
    description: Retorna os dados de um motorista específico pelo ID.
    tags:
      - Motoristas
    parameters:
      - in: path
        name: id_motorista
        required: true
        type: integer
        description: ID do motorista a ser retornado.
    responses:
      200:
        description: Motorista encontrado com sucesso.
      404:
        description: Motorista não encontrado.
      500:
        description: Erro interno do servidor.
    """
    
    try:
        motorista = motorista_model.read_motorista_id(id_motorista)
        return jsonify(motorista), 200
    except MotoristaNaoEncontrado:
        return jsonify({"erro": "Motorista não encontrado"}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 500


@motoristas_blueprint.route("/motoristas/<int:id_motorista>", methods=['PUT'])
def atualizar_motoristas(id_motorista):
    """
    Atualiza um motorista existente.
    ---
    description: Atualiza os dados de um motorista pelo ID.
    tags:
      - Motoristas
    parameters:
      - in: path
        name: id_motorista
        required: true
        type: integer
      - in: body
        name: body
        required: true
        description: Dados a serem atualizados do motorista.
        schema:
          type: object
          properties:
            nome: { type: string }
            cpf: { type: string }
            rg: { type: string }
            salario: { type: number }
            data_nascimento: { type: string, format: date }
            numero_cnh: { type: string }
            categoria_cnh: { type: string }
            validade_cnh: { type: string, format: date }
            telefone: { type: string }
            email: { type: string }
            endereco: { type: string }
            cidade: { type: string }
            uf: { type: string }
            cep: { type: string }
    responses:
      200:
        description: Motorista atualizado com sucesso.
      404:
        description: Motorista não encontrado.
      400:
        description: Erro na requisição.
    """
    
    dados = request.get_json()
    try:
        atualizado = motorista_model.update_motorista(id_motorista, dados)
        if atualizado:
            return jsonify(motorista_model.read_motorista_id(id_motorista)), 200
        else:
            return jsonify({'erro': 'Motorista não encontrado'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 400


@motoristas_blueprint.route("/motoristas/<int:id_motorista>", methods=['DELETE'])
def apagar_motoristas_id(id_motorista):
    """
    Deleta um motorista pelo ID.
    ---
    description: Remove um motorista específico do sistema pelo ID.
    tags:
      - Motoristas
    parameters:
      - in: path
        name: id_motorista
        required: true
        type: integer
    responses:
      200:
        description: Motorista deletado com sucesso.
      404:
        description: Motorista não encontrado.
      400:
        description: Erro na requisição.
    """
    
    try:
        deletado = motorista_model.delete_motorista_id(id_motorista)
        if deletado:
            return jsonify({'mensagem': 'Motorista deletado com sucesso'}), 200
        else:
            return jsonify({'erro': 'Motorista não encontrado'}), 404
    
    except Exception as e:
        return jsonify({'erro': str(e)}), 400


@motoristas_blueprint.route("/motoristas", methods=['DELETE'])
def deletar_motorista():
    """
    Deleta todos os motoristas.
    ---
    description: Remove todos os motoristas cadastrados no sistema.
    tags:
      - Motoristas
    responses:
      200:
        description: Todos os motoristas foram deletados com sucesso.
      400:
        description: Erro ao tentar excluir os motoristas.
      500:
        description: Erro interno do servidor.
    """
       
    try:
        deletado, erro = motorista_model.delete_todos_motoristas()
        if erro:
            return jsonify({'erro': erro}), 400
        return jsonify({'mensagem': 'Todos os motoristas foram deletados com sucesso'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500



