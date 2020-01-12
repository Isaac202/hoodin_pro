import json
import requests
import base64
import tempfile


base_url = 'http://35.229.72.245:8080'
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


def get_body():
    return {
        "signatario": "pkcs12",
        "algoritmoHash": "SHA256",
        "perfil": "BASICA",
        "formatoDados": "Base64",
        "formatoAssinatura": "HASH",
        "hashes": [
            "o+55vve0GAC27ZhbWp23umyDMgcCo++TMNC1JC92iaI="
        ]
    }


def get_bry(headers, body, url=service_url):
    return requests.post(
        service_url,
        data=json.dumps(body),
        headers=headers
    )


def get_signature_b64(files_b64: list, method=1):
    headers = get_header()
    body = get_body()
    body['formatoAssinatura'] = get_formato(method)
    body['hashes'] = files_b64
    response = get_bry(headers, body)
    return response.json()


def save_signature(file_b64):
    # data = base64.decodebytes(file_b64.encode('utf-8'))
    binary = base64.decodestring(file_b64)
    file = tempfile.TemporaryFile()
    file.write(binary)
    # arquivo.signature.save("file.p7s", File(file))
    file.close()


# encodedZip = base64.b64encode(zipContents).decode('ascii')

# import base64

# base64_img = 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsTAAA' \
#             'LEwEAmpwYAAAB1klEQVQ4jY2TTUhUURTHf+fy/HrjhNEX2KRGiyIXg8xgSURuokX' \
#             'LxFW0qDTaSQupkHirthK0qF0WQQQR0UCbwCQyw8KCiDbShEYLJQdmpsk3895p4aS' \
#             'v92ass7pcfv/zP+fcc4U6kXKe2pTY3tjSUHjtnFgB0VqchC/SY8/293S23f+6VEj' \
#             '9KKwCoPDNIJdmr598GOZNJKNWTic7tqb27WwNuuwGvVWrAit84fsmMzE1P1+1TiK' \
#             'MVKvYUjdBvzPZXCwXzyhyWNBgVYkgrIow09VJMznpyebWE+Tdn9cEroBSc1JVPS+' \
#             '6moh5Xyjj65vEgBxafGzWetTh+rr1eE/c/TMYg8hlAOvI6JP4KmwLgJ4qD0TIbli' \
#             'TB+sunjkbeLekKsZ6Zc8V027aBRoBRHVoduDiSypmGFG7CrcBEyDHA0ZNfNphC0D' \
#             '6amYa6ANw3YbWD4Pn3oIc+EdL36V3od0A+MaMAXmA8x2Zyn+IQeQeBDfRcUw3B+2' \
#             'PxwZ/EdtTDpCPQLMh9TKx0k3pXipEVlknsf5KoNzGyOe1sz8nvYtTQT6yyvTjIax' \
#             'smHGB9pFx4n3jIEfDePQvCIrnn0J4B/gA5J4XcRfu4JZuRAw3C51OtOjM3l2bMb8' \
#             'Br5eXCsT/w/EAAAAASUVORK5CYII='

# # Decoding Binary Data with Python
# base64_img_bytes = base64_img.encode('utf-8')
# with open('decoded_image', 'wb') as file_to_save:
#     decoded_data = base64.decodebytes(base64_img_bytes)
#     file_to_save.write(decoded_image_data)

# import io
# io.BytesIO()
# import os
# import tempfile
# fp = tempfile.TemporaryFile()
# fp.write(b'Hello world!')
# # Closing automatically deletes the tempfile
# fp.close()


# diretory = '/home/drummerzzz/workspace/python/django/test/hoodid_web'

# with tempfile.NamedTemporaryFile(dir=os.path.dirname(diretory)) as f:
#   f.write('kdkdkdkdkdk')
#   os.link(f.name, diretory)
