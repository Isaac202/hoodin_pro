from __future__ import absolute_import, unicode_literals
from celery import shared_task, task
from datetime import datetime
from decouple import config
import json
from cieloApi3 import *
import requests
from django.contrib.auth import get_user_model
from compra_credito.models import ComprarCredito
import logging
User = get_user_model()


loogger = logging.getLogger('erro_cielo')
url_prd = config('CIELO_PRD_PUT_POST')
id_cliente = config('MERCHANT_ID')
key_cliente = config('MERCHANT_KEY')
environment = Environment(sandbox=False)
merchant = Merchant(id_cliente, key_cliente)
cielo_ecommerce = CieloEcommerce(merchant, environment)

cod_erro_cielo= {

    '100': 'Campo enviado está vazio ou inválido',
    '101': 'MerchantId Campo enviado está vazio ou inválido',
    '102': 'Pagamento obrigatório Campo enviado está vazio ou inválido',
    '103': 'Payment is so number',
    '104': 'Identidade do cliente é necessária',
    '105': 'Nome do cliente é obrigatório',
    '106': 'ID da transação é obrigatório',
    '107': 'OrderId é inválido ou não existe',
    '108': 'O valor deve ser maior ou igual a zero',
    '110': 'Moeda de pagamento inválida',
    '111': 'País de pagamento é obrigatório',
    '112': 'País de pagamento inválido',
    '113': 'Código de pagamento inválido',
    '114': 'O MerchantId fornecido não está no formato correto',
    '115': 'O MerchantId fornecido não foi encontrado',
    '116': 'Loja bloqueada, entre em contato com o suporte Cielo',
    '117': 'É necessário o titular do cartão de crédito',
    '118': 'Número do cartão de crédito é obrigatório',
    '119': 'É necessário pelo menos um pagamento',
    '120': 'IP bloqueado por questões de segurança ',
    '121': 'O cliente é obrigatório',
    '122': 'MerchantOrderId é obrigatório',
    '123': 'As parcelas devem ser maiores ou iguais a uma',
    '124': 'Cartão de crédito obrigatório',
    '125': 'Data de validade do cartão de crédito é necessária',
    '126': 'Data de validade do cartão de crédito inválida',
    '127': 'Número de cartão de crédito obrigatório',
    '128': 'Numero do cartão superiro de 16 dígitos',
    '129': 'Meio de pagamento não vinculado a uma loja ou Fornecedor inválido',
    '130': 'Não foi possível obter o cartão de crédito',
    '131': 'MerchantKey é obrigatório',
    '132': 'MerchantKey é inválido',
    '133': 'O provedor não é suportado para este tipo de pagamento',
    '134': 'Dado enviado excede o tamanho do campo',
    '135': 'Dado enviado excede o tamanho do campo',
    '136': 'Comprimento do ItemDataName excedido',
    '137': 'Comprimento do ItemDataSKU excedido',
    '138': 'PassengerDataName comprimento excedido',
    '139': 'comprimento PassengerDataStatus excedido',
    '140': 'comprimento PassengerDataEmail excedido',
    '141': 'PassengerDataPhone length excedido',
    '142': 'Duração do TravelDataRoute excedida',
    '143': 'Duração de TravelDataJourneyType excedida',
    '144': 'Comprimento de TravelLegDataDestination excedido',
    '145': 'Comprimento TravelLegDataOrigin excedido',
    '146': 'Comprimento do código de segurança excedido',
    '147': 'Endereço Rua excedida',
    '148': 'Comprimento do número do endereço excedido',
    '149': 'Comprimento do complemento de endereço excedido',
    '150': 'Endereço ZipCode length exced',
    '151': 'Endereço Cidade excedida',
    '152': 'Endereço Estado excedido',
    '153': 'Endereço do país excedido',
    '154': 'Endereço comprimento do distrito excedido',
    '155': 'Comprimento do nome do cliente excedido',
    '156': 'Comprimento da identidade do cliente excedido',
    '157': 'Comprimento do tipo de identidade do cliente excedido',
    '158': 'Comprimento do email do cliente excedido',
    '159': 'Comprimento do nome ExtraData excedido',
    '160': 'Comprimento do Valor ExtraData excedido',
    '161': 'Comprimento das instruções do boleto excedido',
    '162': 'Comprimento da demonstração demonstrativa do boleto excedido',
    '163': 'URL de retorno não é válido',
    '166': 'AuthorizeNow is required',
    '167': 'Antifraude não vinculado ao cadastro do lojista',
    '168': 'Recorrência não encontrada',
    '169': 'Recorrência não está ativa. Execução paralizada ',
    '170': 'Cartão protegido não vinculado ao cadastro do lojista',
    '171': 'Falha no processamento do pedido - Entre em contato com o suporte Cielo',
    '172': 'Falha na validação das credenciais enviadas',
    '173': 'Meio de pagamento não vinculado ao cadastro do lojista',
    '174': 'Campo enviado está vazio ou inválido',
    '175': 'EAN é obrigatório',
    '176': 'Moeda de pagamento não é suportada',
    '177': 'Número do cartão inválido',
    '178': 'EAN é inválido',
    '179': 'O número máximo de parcelas permitidas para pagamentos recorrentes é 1',
    '180': 'O PaymentToken fornecido com o cartão não foi encontrado',
    '181': 'O MerchantIdJustClick não está configurado',
    '182': 'Marca é obrigatória Bandeira do cartão não enviado',
    '183': 'Data de nascimento inválida ou futura',
    '184': 'Falha no formado da requisição. Verificar o código enviado ',
    '185': 'Bandeira não suportada pela API Cielo',
    '186': 'Meio de pagamento sem suporte ou comando enviado',
    '187': 'ExtraData Collection contém um ou mais nomes duplicados',
    '188': 'CPF inválido',
    '189': 'Avs com comprimento de rua excedido',
    '190': 'Avs com comprimento de número excedido',
    '191': 'Avs com comprimento de distrito excedido',
    '192': 'Avs com CEP inválido',
    '193': 'O valor da divisão deve ser maior que zero',
    '194': 'É necessário estabelecimento dividido',
    '195': 'O PlataformId é obrigatório',
    '196': 'DeliveryAddress is required',
    '197': 'Rua é necessária',
    '198': 'Number is required',
    '199': 'ZipCode é obrigatório',
    '200': 'Cidade é necessária',
    '201': 'Estado é obrigatório',
    '202': 'Distrito é obrigatório',
    '203': 'Nome do item do carrinho é obrigatório',
    '204': 'Quantidade do item do carrinho é necessária',
    '205': 'Tipo de item de carrinho é obrigatório',
    '206': 'comprimento do nome do item do carrinho excedido',
    '207': 'comprimento da descrição do item do carrinho excedido',
    '208': 'comprimento do sku do item do carrinho excedido',
    '209': 'comprimento do sku do destinatário da remessa excedido',
    '210': 'Os dados de remessa não podem ser nulos',
    '211': 'WalletKey é inválido',
    '212': 'Configuração da carteira do comerciante não encontrada',
    '213': 'Número do cartão de crédito inválido',
    '214': 'O titular do cartão de crédito deve ter apenas letras',
    '215': 'Agência é necessária na credencial do Boleto',
    '216': 'O endereço IP do cliente é inválido',
    '300': 'MerchantId não foi encontrado',
    '301': 'IP de solicitação não é permitido',
    '302': 'MerchantOrderId enviado está duplicado',
    '303': 'OrderId enviado não existe',
    '304': 'Identidade do cliente é necessária',
    '306': 'O comerciante está bloqueado. O comerciante está bloqueado',
    '307': 'Transação não encontrada',
    '308': 'Transação não disponível para captura',
    '309': 'Transação não disponível para anular',
    '310': 'O método de pagamento não suporta esta operação',
    '311': 'O reembolso não está ativado para este comerciante',
    '312': 'Transação não disponível para reembolso',
    '313': 'Pagamento recorrente não encontrado',
    '314': 'Integração inválida',
    '315': 'Não é possível alterar a PróximaRecorrência com pagamento pendente',
    '316': 'Não é possível definir NextRecurrency para data passada',
    '317': 'Dia de recorrência inválido',
    '318': 'Nenhuma transação encontrada',
    '319': 'Recorrência inteligente não está ativada',
    '320': 'Não é possível atualizar a afiliação porque essa recorrência não foi salva',
    '321': 'Não é possível definir EndDate para antes da próxima recorrência',
    '322': 'Zero Dollar Auth não está ativado',
    '323': 'Consulta de Lixeira não está ativada',
}

@task
def comprar_credito(id_compra, cliente, numero_cartao, seguranca, bandeira, validade, valor, qtd_parcela):
    x = ''
    msg_retorno = ''
    codigo_transacao = ''
    codigo_pagamento = '0'

    try:
        sale = Sale(id_compra)
        sale.customer = Customer(cliente)
        credit_card = CreditCard(seguranca, bandeira)
        credit_card.expiration_date = validade
        credit_card.security_code = seguranca
        credit_card.card_number = numero_cartao
        credit_card.holder = cliente
        sale.payment = Payment(valor)
        sale.payment.credit_card = credit_card
        sale.payment.installments = qtd_parcela

        response_create_sale = cielo_ecommerce.create_sale(sale)
        x = json.dumps(response_create_sale, indent=3, sort_keys=True)
        payment_id = sale.payment.payment_id
        print(x)

        if payment_id is not None:
            codigo_pagamento = payment_id

        resultado = json.loads(x)
        codigo_transacao = resultado["Payment"]["Tid"]
        msg_retorno = resultado["Payment"]["ReturnMessage"]


    except Exception as e:
        msg = str(e)
        pesquisa=msg
        p =pesquisa[7:12]
        p = p.replace('[','')
        p =p.replace(']', '')
        codigo = p
        msg_retorno= str(cod_erro_cielo.get(codigo,0))
        return (msg_retorno, '0', '0')


    return (msg_retorno, codigo_transacao, codigo_pagamento)

@task
def gerar_token_cartao(cliente, numero_cartao, seguranca, bandeira, validade):
    token_cartao = ''
    try:
        credit_card = CreditCard(seguranca, bandeira)
        credit_card.expiration_date = validade
        credit_card.security_code = seguranca
        credit_card.card_number = numero_cartao
        credit_card.holder = cliente
        credit_card.customer_name = cliente
        cielo_ecommerce = CieloEcommerce(merchant, environment)
        response_create_card_token = cielo_ecommerce.create_card_token(credit_card)
        print(json.dumps(response_create_card_token, indent=2))
        new_card_token = credit_card.card_token
        print('cartao Token:', new_card_token)
        token_cartao = new_card_token

    except KeyError as e:
        print(e)

    return token_cartao


@task
def cancelar_compra(id_pagamento, valor):
    response_cancel_sale = cielo_ecommerce.cancel_sale(id_pagamento, valor)
    canelamento = json.dumps(response_cancel_sale, indent=3, sort_keys=True)
    print('cacelamento ta ok')
    print(canelamento)
    return canelamento

#TODO Testa com Marto cancelamento





