from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse('Hola')


'''def entradas(request):
    lista_de_entradas=['Provolone', 'Faina', 'Croquetas', 'Falafel', 'Sopa']
    diccionario={"entrada":lista_de_entradas}
    plantilla=loader.get_template('inicio.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)'''  