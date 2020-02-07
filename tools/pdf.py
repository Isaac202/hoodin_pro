import io
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from codigos_promocionais.actions import open_image_from_url
from django.conf import settings
import os


def get_canvas(buffer, context):
    texto = u'''
        CERTIFICO que, às {} horas do dia {}, {},
        inscrito(a) no CPF/MF sob o número {}, residente {}, {} N° {},
        {} na cidade de {}, bairro de {}, estado {}, com CEP {}, 
        obteve registro da sua declaração de autoria da obra intelectual intitulada {}, na categoria {}.
        O presente registro foi  assinado  pelo titular deste  certificado, e está associado a
        uma chave digital fornecida pelo Instituto Nacional de Tecnologia da
        Informação (ITI), através de  uma ACT (Autoridade de Carimbo de Tempo) utilizada
        para garantir data e hora da assinatura digital com base nos dados fornecidos pelo
        Observatório Nacional, cuja autoridade foi conferida pela Administração Pública.
        A chave digital foi gerada através do  sistema online da
        HoodID Registros Online Ltda. Tendo esta declaração de  autoria 
        de  obra intelectual garantia de autenticidade, integridade e validade jurídica,
        nos termos do artigo 1°; da  Medida Provisória n°; 2.200-2, de 24 de agosto de 2001.
        Por ser esta declaração a mais absoluta expressão da verdade, a HoodID Registros Online
        emite o presente certificado que subscreve nesta cidade do Recife - PE.
        '''.format(
                context['hora'], context['data'], context['nome'],
                context['cnpjcpf'], context['pais'], context['endereco'],
                context['numero'], context['complemento'], context['cidade'],
                context['bairro'], context['estado'], context['cep'],
                context['resume'], context['servico']
                # context['code'], 
        )
    c = canvas.Canvas(buffer, pagesize=landscape(A4))
    # Estilo para o texto
    estilo = ParagraphStyle(name='Normal', alignment=TA_JUSTIFY,
                            fontSize=14, leading=20, fontName="Times-Roman")
    
    cabecalho = ParagraphStyle(name='Bold', alignment=TA_CENTER,
                        fontSize=16, leading=20, fontName="Times-Roman")

    items = []
    items.append(Paragraph(texto, estilo))
    bg = r'' + os.path.join(settings.BASE_DIR, 'static', 'imgs', 'fundo.jpg')
    # Imagem
    title =[Paragraph(u'CERTIFICADO DE REGISTRO N° {}\n'.format(context['code']),cabecalho)]

    c.drawInlineImage(bg, 0, 0, 298*mm, 210*mm)

    items = []
    items.append(Paragraph(texto, estilo))

    # cria o titulo do certificado
    t = Frame(20*mm, 38*mm, 255*mm, 125*mm, showBoundary=0)
    t.addFromList(title, c)
    
    # Cria um frame com o texto
    f = Frame(26*mm, 26*mm, 255*mm, 125*mm, showBoundary=0)
    f.addFromList(items, c)
    return c
    # c.save()
