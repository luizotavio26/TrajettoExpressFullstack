from flask import Blueprint, request, jsonify
from model import cadastro_veiculos
from model.cadastro_veiculos import *

cadastro_veiculos_blueprint = Blueprint('cadastro_veiculos', __name__)


@cadastro_veiculos_blueprint.route("/veiculos", methods=['GET'])
def listarVeiculos():
    """
    Lista todos os veículos.
    ---
    description: Retorna todos os veículos cadastrados no sistema.
    tags:
      - Veículos
    responses:
      200:
        description: Lista de veículos retornada com sucesso.
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              placa:
                type: string
                example: "ABC1234"
              modelo:
                type: string
                example: "Volvo FH"
              marca:
                type: string
                example: "Volvo"
              renavan:
                type: string
                example: "12345678901"
              chassi:
                type: string
                example: "9BWZZZ377VT004251"
              cor:
                type: string
                example: "Branco"
              tipo:
                type: string
                example: "Caminhão"
              ano_modelo:
                type: string
                example: "2020"
              ano_fabricacao:
                type: string
                example: "2019"
      500:
        description: Erro interno ao listar veículos.
    """
    
    try:
        veiculos,erro = cadastro_veiculos.getVeiculos()
        return jsonify(veiculos), 200
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'erro': str(e)}), 500
    

@cadastro_veiculos_blueprint.route("/veiculos/<int:id_veiculo>", methods=['GET'])
def listarVeiculoId(id_veiculo):
    """
    Busca um veículo pelo ID.
    ---
    description: Retorna os dados de um veículo específico pelo ID.
    tags:
      - Veículos
    parameters:
      - in: path
        name: id_veiculo
        required: true
        type: integer
        description: ID do veículo a ser retornado.
    responses:
      200:
        description: Veículo encontrado.
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            placa:
              type: string
              example: "ABC-1234"
            modelo:
              type: string
              example: "Volvo FH"
            marca:
              type: string
              example: "Volvo"
            renavan:
              type: string
              example: "12345678901"
            chassi:
              type: string
              example: "9BWZZZ377VT004251"
            cor:
              type: string
              example: "Branco"
            tipo:
              type: string
              example: "Caminhão"
            ano_modelo:
              type: string
              example: "2020"
            ano_fabricacao:
              type: string
              example: "2019"
      404:
        description: Veículo não encontrado.
      500:
        description: Erro interno no servidor.
    """

    
    try:
        veiculos = cadastro_veiculos.getVeiculosId(id_veiculo)
        if veiculos:
            return jsonify(veiculos), 200
        else:
            return jsonify({'erro': 'Veiculo não encontrado'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 500


@cadastro_veiculos_blueprint.route("/veiculos", methods=['POST'])
def cadastrar_veiculo():
    """
    Cria um novo veículo.
    ---
    description: Cadastra um novo veículo no sistema.
    tags:
      - Veículos
    parameters:
      - in: body
        name: body
        required: true
        description: Dados completos do veículo a ser cadastrado.
        schema:
          type: object
          required:
            - placa
            - modelo
            - marca
            - renavan
            - chassi
            - cor
            - tipo
            - ano_modelo
            - ano_fabricacao
          properties:
            placa:
              type: string
              example: "ABC-1234"
            modelo:
              type: string
              example: "Volvo FH"
            marca:
              type: string
              example: "Volvo"
            renavan:
              type: string
              example: "12345678901"
            chassi:
              type: string
              example: "9BWZZZ377VT004251"
            cor:
              type: string
              example: "Branco"
            tipo:
              type: string
              example: "Caminhão"
            ano_modelo:
              type: string
              example: "2020"
            ano_fabricacao:
              type: string
              example: "2019"
    responses:
      201:
        description: Veículo cadastrado com sucesso.
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Veículo Volvo FH cadastrado com sucesso."
      400:
        description: Erro na requisição ou validação dos dados.
    """  
    
    try:
        dados = request.get_json(silent=True)
        mensagem = cadastro_veiculos.postVeiculos(dados)
        return jsonify({"message": mensagem}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 400


@cadastro_veiculos_blueprint.route("/veiculos/<int:id_veiculo>", methods=['PUT'])
def atualizar_veiculos_id(id_veiculo):
    """
    Atualiza um veículo existente.
    ---
    description: Atualiza os dados de um veículo pelo ID.
    tags:
      - Veículos
    parameters:
      - in: path
        name: id_veiculo
        required: true
        type: integer
        description: ID do veículo a ser atualizado.
      - in: body
        name: body
        required: true
        description: Campos a serem atualizados do veículo.
        schema:
          type: object
          properties:
            placa:
              type: string
              example: "XYZ-9876"
            modelo:
              type: string
              example: "Scania R500"
            marca:
              type: string
              example: "Scania"
            renavan:
              type: string
              example: "10987654321"
            chassi:
              type: string
              example: "9BWZZZ377VT004252"
            cor:
              type: string
              example: "Azul"
            tipo:
              type: string
              example: "Caminhão"
            ano_modelo:
              type: string
              example: "2021"
            ano_fabricacao:
              type: string
              example: "2020"
    responses:
      200:
        description: Veículo atualizado com sucesso.
      404:
        description: Veículo não encontrado.
      400:
        description: Erro na requisição.
    """
    
    dados = request.get_json(silent=True)
    try:
        atualizado = cadastro_veiculos.putVeiculoPorId(id_veiculo, dados)
        if atualizado:
            return jsonify({'mensagem': 'Veículo atualizado com sucesso'}), 200
        else:
            return jsonify({'erro': 'Veículo não encontrado'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 400


@cadastro_veiculos_blueprint.route("/veiculos/<int:id_veiculo>", methods=['DELETE'])
def apagar_veiculos_id(id_veiculo):
    """
    Deleta um veículo pelo ID.
    ---
    description: Remove um veículo específico do sistema pelo ID.
    tags:
      - Veículos
    parameters:
      - in: path
        name: id_veiculo
        required: true
        type: integer
        description: ID do veículo a ser removido.
    responses:
      200:
        description: Veículo deletado com sucesso.
      404:
        description: Veículo não encontrado.
      400:
        description: Erro na requisição.
    """

    try:
        deletado = cadastro_veiculos.deleteVeiculoPorId(id_veiculo)
        if deletado:
            return jsonify({'mensagem': 'Veículo deletado com sucesso'}), 200
        else:
            return jsonify({'erro': 'Veículo não encontrado'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 400


