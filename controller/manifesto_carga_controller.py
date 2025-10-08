from flask import Blueprint, request, jsonify
from model import manifesto_carga_model
from model.manifesto_carga_model import CargaNaoEncontrada

manifesto_cargas_blueprint = Blueprint('manifesto_carga', __name__)

		
@manifesto_cargas_blueprint.route('/cargas', methods=['POST'])
def cria_cargas():
    """
    Cria uma nova carga.
    ---
    description: Registra uma nova carga no sistema.
    tags:
      - Manifesto
    parameters:
      - in: body
        name: body
        required: true
        description: Dados da carga a ser criada.
        schema:
          type: object
          required:
            - tipo_carga
            - peso_carga
            - motorista_id
            - cliente_id
            - veiculo_id
            - origem_carga
            - destino_carga
            - valor_km
            - distancia
          properties:
            tipo_carga:
              type: string
              example: "Frágil"
            peso_carga:
              type: number
              example: 150.5
            motorista_id:
              type: integer
              example: 1
            cliente_id:
              type: integer
              example: 2
            veiculo_id:
              type: integer
              example: 3
            origem_carga:
              type: string
              example: "São Paulo"
            destino_carga:
              type: string
              example: "Rio de Janeiro"
            valor_km:
              type: number
              example: 2.5
            distancia:
              type: number
              example: 200.0
    responses:
      200:
        description: Carga criada com sucesso.
      400:
        description: Erro de validação dos dados enviados.
      500:
        description: Erro interno do servidor.
    """

    
    dados = request.get_json()
    try:
        novo_carga, erro = manifesto_carga_model.create_carga(dados)
        if erro:
            return jsonify({'erro': erro}), 400
        return jsonify(novo_carga), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500
 

@manifesto_cargas_blueprint.route('/cargas', methods=['GET'])
def le_cargas():
    """
    Lista todas as cargas.
    ---
    description: Retorna todas as cargas registradas no sistema.
    tags:
      - Manifesto
    responses:
      200:
        description: Lista de cargas retornada com sucesso.
      500:
        description: Erro interno do servidor.
    """
    
    try:
        cargas,erro = manifesto_carga_model.read_todas_cargas()
        return jsonify(cargas), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500


@manifesto_cargas_blueprint.route('/cargas/<int:id_cargas>', methods =['GET'])
def le_cargas_id(id_cargas):
    """
    Busca uma carga pelo ID.
    ---
    description: Retorna os dados de uma carga específica pelo ID.
    tags:
      - Manifesto
    parameters:
      - in: path
        name: id_cargas
        required: true
        type: integer
        description: ID da carga a ser retornada.
    responses:
      200:
        description: Carga encontrada com sucesso.
      404:
        description: Carga não encontrada.
      500:
        description: Erro interno do servidor.
    """
    
    try:
        carga = manifesto_carga_model.read_cargas_id(id_cargas)
        return jsonify(carga), 200
    except CargaNaoEncontrada:
        return jsonify({'erro': 'Carga não encontrada'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 500


@manifesto_cargas_blueprint.route('/cargas/<int:id_cargas>', methods=['PUT'])
def atualiza_cargas(id_cargas):
    """
    Atualiza uma carga existente.
    ---
    description: Atualiza os dados de uma carga pelo ID.
    tags:
      - Manifesto
    parameters:
      - in: path
        name: id_cargas
        required: true
        type: integer
        description: ID da carga a ser atualizada.
      - in: body
        name: body
        required: true
        description: Dados a serem atualizados da carga.
        schema:
          type: object
          properties:
            tipo_carga:
              type: string
            peso_carga:
              type: number
            informacoes_motorista:
              type: integer
            informacoes_cliente:
              type: integer
            informacoes_veiculo:
              type: integer
            origem_carga:
              type: string
            destino_carga:
              type: string
            valor_frete:
              type: number
            valor_km:
              type: number
            distancia:
              type: number
    responses:
      200:
        description: Carga atualizada com sucesso.
      404:
        description: Carga não encontrada.
      400:
        description: Erro na requisição.
    """
    
    dados = request.get_json()
    try:
        atualizado = manifesto_carga_model.update_carga(id_cargas, dados)
        if atualizado:
            return jsonify(manifesto_carga_model.read_cargas_id(id_cargas)), 200
        else:
            return jsonify({'erro': 'Carga não encontrada'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 400
                

@manifesto_cargas_blueprint.route('/cargas/<int:id_cargas>', methods = ['DELETE'])
def deleta_cargas_id(id_cargas):
    """
    Deleta uma carga pelo ID.
    ---
    description: Remove uma carga específica do sistema pelo ID.
    tags:
      - Manifesto
    parameters:
      - in: path
        name: id_cargas
        required: true
        type: integer
        description: ID da carga a ser removida.
    responses:
      200:
        description: Carga deletada com sucesso.
      404:
        description: Carga não encontrada.
      400:
        description: Erro na requisição.
    """
    
    try:
        deletado = manifesto_carga_model.delete_carga_id(id_cargas)
        if deletado:
            return jsonify({'mensagem': 'Carga deletada com sucesso'}), 200
        else:
            return jsonify({'erro': 'Carga não encontrada'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

    
@manifesto_cargas_blueprint.route('/cargas', methods = ['DELETE'])
def deleta_cargas():
    """
    Deleta todas as cargas.
    ---
    description: Remove todas as cargas registradas no sistema.
    tags:
      - Manifesto
    responses:
      200:
        description: Todas as cargas foram deletadas com sucesso.
      400:
        description: Erro ao tentar excluir as cargas.
      500:
        description: Erro interno do servidor.
    """
    
    try:
        deletado, erro = manifesto_carga_model.delete_todas_cargas()
        if erro:
            return jsonify({'erro': erro}), 400
        return jsonify({'mensagem': 'Todos as cargas foram deletados com sucesso'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500