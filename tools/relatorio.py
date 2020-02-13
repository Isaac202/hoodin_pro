from reportlab.lib.pagesizes import A4, portrait
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table, TableStyle
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import mm
from datetime import datetime

class Relatorio:
    
    thead = []
    tbody = []
    title = "Relatorio"
    space = " - "
    width = 0
    height = 0
    
    def __init__(self, *args, **kwargs):
        self.width, self.height = A4
        
        
    def mount_table(self, data:list):
        table = Table(data, rowHeights=20)
        table.setStyle(TableStyle([
            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('TEXTCOLOR', (0, 0),(-1, 0), colors.red),
        ]))
        return table
    
    def write(self, canvas):
        data = self.thead + self.tbody
        table = self.mount_table(data)
        table.wrapOn(canvas, self.width, self.height)
        table.drawOn(canvas, 10*mm, 250*mm)
        text = self.title + self.space + datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        canvas.drawString(10*mm, 290*mm ,text)
        canvas.showPage()
        
        return canvas
        
    
    def relatorio(self, buffer):
        canvas = Canvas(buffer, pagesize=portrait(A4))
        self.tbody = self.mount_tbody()
        return self.write(canvas)
    
    def mount_tbody(self):
        """
         essa função deve ser sobrescrita e retornar a lista de dodos filtrados no queryset
        """
        msg = u"""
            função mount_tbody não implementada, essa função deve retornar a lista
            com os dados a serem escritos na tabela
        """
        raise NotImplementedError(msg)