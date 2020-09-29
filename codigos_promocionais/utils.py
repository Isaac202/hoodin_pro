from datetime import date, datetime
from codigos_promocionais.models import Codigos_Promocionais as Promocao
from django.db.models import Q

def check_codigo_promocionanl(codigo):
    promocao = Promocao.objects.filter(
        qrcode=codigo, data_limite__gte=date.today(), resgate=False).filter(Q(id_servico__isnull=True)|Q(id_servico=0))
    return promocao

def check_codigo_promocionanlSer(codigo, servico):
    promocao = Promocao.objects.filter(
        qrcode=codigo, data_limite__gte=date.today(), resgate=False).fielter(id_servico=servico)
    return promocao

def set_codigo_promocional(codigo, cliente):
    promocao = check_codigo_promocionanl(codigo)
    # print(prsomocao)
    # print(p)
    if promocao.exists():
        p = promocao.first()
        promocao.update(
            cnpjcpf=cliente.cnpjcpf,
            nome=cliente.nome,
            email=cliente.id_usuario.username,
            resgate=True,
            data_resgate=datetime.now())
        # print(p,'orijdjdj')
        return p
    else:
        return 0
    return 0

def set_codigo_promocionalSer(codigo, cliente, servico):
    promocao = check_codigo_promocionanlSer(codigo, servico)
    # print(prsomocao)
    # print(p)
    if promocao.exists():
        p = promocao.first()
        promocao.update(
            cnpjcpf=cliente.cnpjcpf,
            nome=cliente.nome,
            email=cliente.id_usuario.username,
            resgate=True,
            data_resgate=datetime.now())
        # print(p,'orijdjdj')
        return p
    return None
