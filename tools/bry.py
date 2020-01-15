from registros.models import ArquivoRegistro
from tools.util import remove_exention_file
from django.core.files import File
import json
import requests
import base64
import tempfile

base_url = 'http://35.229.72.245:8080'
# base_url = 'http://localhost:8087'
service_url = base_url + "/fw/v1/cms/pkcs12/assinaturas"


def get_formato(method=1):
    formato_assinatura = ["HASH", "ATTACHED", "DETACHED"]
    return formato_assinatura[method]


def get_header():
    return { 
        "Content-Type": "application/json",
        "pfx": "d2c0KkUySDdlUA==",
        "fw_credencial": "MDE5ODg5ODUwOTkrdWdkZ0R1NlpqWg==",
    }


def get_body(hashes:list):
    return {
        "signatario": "pkcs12",
        "algoritmoHash": "SHA256",
        "perfil": "CARIMBO",
        "formatoDados": "Base64",
        "formatoAssinatura": get_formato(2),
        "hashes": hashes
    }


def get_bry(headers, body, url=service_url):
    return requests.post(
        service_url,
        data=json.dumps(body),
        headers=headers
    )


def get_signature_b64(hashes: list, method=1):
    body = get_body(hashes)
    # body['hashes'] = hashes
    headers = get_header()
    # hashes = []
    # hashes.append(file_b64)
    response = requests.post(
        service_url,
        data=json.dumps(body),
        headers=headers
    )
    return response.json()

        

def signature_files(pks):
    queryset = ArquivoRegistro.objects.filter(pk__in=pks).order_by('id')
    b64s = queryset.values_list('b64', flat=True)
    b64s = list(b64s)
    body = get_body(b64s)
    headers = get_header()
    response = requests.post(
        service_url,
        data=json.dumps(body),
        headers=headers
    ).json()
    try:
        assinaturas = response['assinaturas']
        for index, assinatura in enumerate(assinaturas):
            assinatura = base64.b64decode(assinatura)
            temp = tempfile.TemporaryFile()
            temp.write(assinatura)
            file = queryset[index]
            name = "{}.p7s".format(remove_exention_file(file.name))
            file.signature.save(name, File(temp))
            temp.close()
        return True
    except:
        print(response)
        return False
        
# def signature_save(queryset):
#     for file in queryset:
#         try:
#         response = get_signature_b64(b64)
#         signature = base64.b64decode(response['assinaturas'][0])
#         signature_file = tempfile.TemporaryFile()
#         signature_file.write(signature)
#         name = remove_exention_file(name)
#         file.signature.save("{}.p7s".format(name), File(signature_file))
#         signature_file.close()
#         except:
#             pass