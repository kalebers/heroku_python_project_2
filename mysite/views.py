from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    #data_atual = date.today()
    #return HttpResponse(data_atual)
    return render(request, "index.html")

def page2(request):

    return render(request, "page2.html")

def page3(request):

    html = '''
    <html>
        <head><title>Página 3</title></head>
        <body>
            <h1>Python no Heroku - SOCPS</h1>
            <h2>Págna 3</h2>
            <a href="../">index</a>
        </body>
    </html>
    '''
    return HttpResponse(html)

def page4(request):
    return render(request, "page4.html")


def page5(request):

    html = '''
    <html>
        <head><title>Pagina 5</title></head>
        <body>
            <h1><?php echo "Horario;"?></h1>
            <h2>Págna5</h2>
            <a href="../page2">page2</a>
            <a href="../page4">page4</a>
        </body>
    </html>
    '''
    return HttpResponse(html)

            #<h1><?php echo "Horario".date("j,n,Y");?></h1>
