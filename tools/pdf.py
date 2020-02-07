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


justify = ParagraphStyle(name='Normal', alignment=TA_JUSTIFY,
                        fontSize=14, leading=20, fontName="Times-Roman")
    
center = ParagraphStyle(name='Bold', alignment=TA_CENTER,
                    fontSize=16, leading=20, fontName="Times-Roman")

def get_bg():
    return r'' + os.path.join(settings.BASE_DIR, 'static', 'imgs', 'fundo.jpg')    

def get_text(registro):
    return u'''
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
                registro.data.strftime('%H:%M:%S'), registro.data.strftime("%d/%m/%Y"),
                registro.id_cliente.nome.upper(), registro.id_cliente.pais,
                registro.id_cliente.cnpjcpf, registro.id_cliente.endereco,
                registro.id_cliente.numero, registro.id_cliente.complemento or "",
                registro.id_cliente.cidade.upper(), registro.id_cliente.bairro.upper(),
                registro.id_cliente.estado.upper(), registro.id_cliente.cep,
                registro.arquivo.resume, registro.codservico.nome
        )

def get_canvas(buffer, registro):
    c = canvas.Canvas(buffer, pagesize=landscape(A4))
    texto = get_text(registro)
    
    items = []
    items.append(Paragraph(texto, justify))
    bg = get_bg()
    
    title =[Paragraph(u'CERTIFICADO DE REGISTRO N° {}\n'.format(registro.arquivo.code),center)]
    c.drawInlineImage(bg, 0, 0, 298*mm, 210*mm)

    items = []
    items.append(Paragraph(texto, justify))

    # cria o titulo do certificado
    t = Frame(20*mm, 38*mm, 255*mm, 125*mm, showBoundary=0)
    t.addFromList(title, c)
    # Cria um frame com o texto
    f = Frame(26*mm, 26*mm, 255*mm, 125*mm, showBoundary=0)
    f.addFromList(items, c)
    c.showPage()
    
    
    c_autores = []
    coautores = registro.arquivo.coautores_set.all()
    if coautores:
        cont = coautores.count()
        for i in range(0, cont):
            salt = 10
            index = (i+1) * salt
            if index < cont:
                c_autores.append(coautores[index-salt: index])
            else:
                c_autores.append(coautores[index-salt:cont])
                break
        for coautor_list in c_autores:
            lista = []
            c.drawInlineImage(bg, 0, 0, 298*mm, 210*mm)
            for pessoa in coautor_list:
                autor = u'Nome: {} Documento Identificação:{} {}%'.format(pessoa.nome, pessoa.documento, pessoa.percentual_obra)
                lista.append(Paragraph(autor, center))
                
            # cria o titulo do certificado
            new_title = Frame(20*mm, 38*mm, 255*mm, 125*mm, showBoundary=0)
            title = [Paragraph(u'CERTIFICADO DE REGISTRO N° {}\n'.format(registro.arquivo.code),center)]
            new_title.addFromList(title, c)
            new_frame = Frame(26*mm, 26*mm, 255*mm, 125*mm, showBoundary=0)
            new_frame.addFromList(lista, c)
            c.showPage()
    
    return c
    
