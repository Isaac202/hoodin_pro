import os
import tempfile
import zipfile
import requests
from io import BytesIO
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from django.conf import settings
from django.http import HttpResponse
# from django.core.servers.basehttp import FileWrapper


def open_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img


def response(image, qr="code", file_name="qrcode_"):
    response = HttpResponse(content_type="image/png")
    response['Content-Disposition'] = 'attachment; filename={}.png'.format(file_name+qr)
    image.save(response, "PNG")
    return response


def write_code(queryset):
    codigo_promocional = queryset.first()
    bg = 'https://hoodidfile.s3.amazonaws.com/static/imgs/card.png'
    f = os.path.join(settings.BASE_DIR, 'arial.ttf')
    fill_color = '#006cfacf'
    validade = codigo_promocional.data_limite.strftime("%d/%m/%Y")
    valor = ("%.2f" % codigo_promocional.valor).replace('.', ',')
    code = codigo_promocional.qrcode
    img = open_image_from_url(bg)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(f, 25)#, layout_engine=ImageFont.LAYOUT_BASIC)
    font_money = ImageFont.truetype(f, 85)
    draw.text((785, 40), valor, fill=fill_color, font=font_money)
    draw.text((1050, 560), code, fill=fill_color, font=font)
    draw.text((600, 560), validade, fill=fill_color, font=font)
    return response(img, qr=code)


# def send_zipfile(extention=""):
#     """
#     Create a ZIP file on disk and transmit it in chunks of 8KB,
#     without loading the whole file into memory. A similar approach can
#     be used for large dynamic PDF files.
#     """
#     temp = tempfile.TemporaryFile()
#     archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)
#     for index in range(10):
#         filename =  write_code()                 
#         archive.write(filename, 'f{}.{}'.format(index, extention))
#     archive.close()
#     wrapper = FileWrapper(temp)
#     response = HttpResponse(wrapper, content_type='application/zip')
#     response['Content-Disposition'] = 'attachment; filename=test.zip'
#     response['Content-Length'] = temp.tell()
#     temp.seek(0)
#     return response
