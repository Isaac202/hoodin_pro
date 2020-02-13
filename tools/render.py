from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils import timezone
# from django.http import FileResponse
# from django.template.loader import render_to_string
import xlwt
import os
import pdfkit
# from pyvirtualdisplay import Display
from django_pdfkit import PDFView

class CustomPDFView(PDFView):
    
    context = {}
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.context
    
    
    def render_pdf(self, *args, **kwargs):
        html = self.render_html(*args, **kwargs)
        options = self.get_pdfkit_options()
        wkhtmltopdf_bin = os.environ.get('WKHTMLTOPDF_BIN')
        if wkhtmltopdf_bin:
            kwargs['configuration'] = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_bin)
            
        # d = Display()
        # try:
            # d.start()
        pdf = pdfkit.from_string(html, False, options, **kwargs)
        return pdf
        # finally:
            # d.stop()
    
    def render_html(self, *args, **kwargs):        
        template = get_template(self.template_name)
        context = self.get_context_data(*args, **kwargs)
        html = template.render(context)
        return html
            
    
    def set_context(self, context):
        self.context = context


from django.shortcuts import render

class RenderPDF:
    
    @staticmethod
    def render(path: str, params: dict, *args, **kwargs):
        filename = params['description'] + ".pdf"
        request = params['request']
        return render(request, path, params)
        # pdf_kit = CustomPDFView(template_name=path, filename=filename)
        # pdf_kit.set_context(params)
        # content = pdf_kit.render_pdf(*args, **kwargs)
        # response = HttpResponse(content, content_type='application/pdf')
        # if (not pdf_kit.inline or 'download' in request.GET) and 'inline' not in request.GET:
        #     response['Content-Disposition'] = 'attachment; filename=%s' % filename
        #     response['Content-Length'] = len(content)
        #     return response
        # else:
        #     return HttpResponse("Error Rendering PDF", status=400)

    @staticmethod
    def render_to_pdf(request, queryset, template='tools/pdf.html', description="Relatório de Clientes"):
        today = timezone.now()
        params = {
            'today': today,
            'description': description,
            'request': request,
            'queryset': queryset
        }
        return RenderPDF.render(template, params)


# class Render:
#     @staticmethod
#     def render(path: str, params: dict):
#         template = get_template(path)
#         html = template.render(params)
#         response = BytesIO()
#         pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
#         if not pdf.err:
#             # response = HttpResponse(pdf, content_type='application/pdf')
#             response =  HttpResponse(response.getvalue(), content_type='application/pdf')
#             # response['Content-Disposition'] = 'attachment; filename="cliente.pdf"'
#             return response
#         else:
#             return HttpResponse("Error Rendering PDF", status=400)

#     @staticmethod
#     def render_to_pdf(request, queryset, template='tools/pdf.html', description="Relatório de Clientes"):
#         today = timezone.now()
#         params = {
#             'today': today,
#             'description': description,
#             'request': request,
#             'queryset': queryset
#         }
#         return Render.render( template, params)

#     @staticmethod
#     def render_to_xls(request, queryset):
#         response = HttpResponse(content_type='application/ms-excel')
#         response['Content-Disposition'] = 'attachment; filename="users.xls"'

#         wb = xlwt.Workbook(encoding='utf-8')
#         ws = wb.add_sheet('Relatório')

#         # Sheet header, first row
#         row_num = 0

#         font_style = xlwt.XFStyle()
#         font_style.font.bold = True

#         columns = ['Nome', 'Email', 'Whatsapp', 'Tema', ]

#         for col_num in range(len(columns)):
#             ws.write(row_num, col_num, columns[col_num], font_style)

#         # Sheet body, remaining rows
#         font_style = xlwt.XFStyle()

#         rows = queryset.values_list('name', 'email', 'whatsapp', 'theme__name')
#         for row in rows:
#             row_num += 1
#             for col_num in range(len(row)):
#                 ws.write(row_num, col_num, row[col_num], font_style)

#         wb.save(response)
#         return response
