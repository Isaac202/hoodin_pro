from datetime import date, datetime
from codigos_promocionais.models import Codigos_Promocionais as Promocao


def check_codigo_promocionanl(codigo):
    promocao = Promocao.objects.filter(
        qrcode=codigo, data_limite__gte=date.today(), resgate=False)
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
    return None
