from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils import timezone
from django.http import FileResponse
from reportlab.pdfgen import canvas
import xhtml2pdf.pisa as pisa
import xlwt


from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML


class Render:

    @staticmethod
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            # response = HttpResponse(pdf, content_type='application/pdf')
            response =  HttpResponse(response.getvalue(), content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="cliente.pdf"'
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)

    @staticmethod
    def render_to_pdf(request, queryset, template='tools/pdf.html', description="Relatório de Clientes"):
        today = timezone.now()
        params = {
            'today': today,
            'description': description,
            'request': request,
            'queryset': queryset
        }
        return Render.render( template, params)

    @staticmethod
    def render_to_xls(request, queryset):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="users.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Relatório')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Nome', 'Email', 'Whatsapp', 'Tema', ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = queryset.values_list('name', 'email', 'whatsapp', 'theme__name')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response

    # def html_to_pdf_view(request, clientes, description="Lista de Clientes"):
    #     today = timezone.now()
    #     params = {
    #         'today': today,
    #         'request': request,
    #         'clientes': clientes
    #     }
    #     html_string = render_to_string(
    #         'tools/pdf.html', params)

    #     html = HTML(string=html_string,  encoding="utf-8")
    #     # html = HTML(filename=template)
    #     # html = HTML('http://localhost:8000/')#.write_pdf('/tmp/weasyprint-website.pdf')
    #     html.write_pdf(target='/tmp/mypdf.pdf')

    #     fs = FileSystemStorage('/tmp')
    #     with fs.open('mypdf.pdf') as pdf:
    #         response = HttpResponse(pdf, content_type='application/pdf')
    #         # response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
    #         return response

    #     return response

    # @staticmethod
    # def some_view(request):
    #     from django.template.loader import render_to_string
    #     # Create a file-like buffer to receive PDF data.
    #     buffer = BytesIO()

    #     # Create the PDF object, using the buffer as its "file."
    #     p = canvas.Canvas(buffer)

    #     # Draw things on the PDF. Here's where the PDF generation happens.
    #     # See the ReportLab documentation for the full list of functionality.
    #     string = render_to_string('tools/pdf.html')
    #     print(string)
    #     p.drawString(100, 100, string)
    #     p.dra

    #     # Close the PDF object cleanly, and we're done.
    #     p.showPage()
    #     p.save()

    #     # FileResponse sets the Content-Disposition header so that browsers
    #     # present the option to save the file.
    #     buffer.seek(0)
    #     return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
