# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    html = f'''
    <html>
        <body>
            <h1>Datazo Consultoria</h1>
            <p>Horário atual { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)