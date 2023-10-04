from django.shortcuts import render

# Create your views here.
def usuario():
    Nombre = "Epico"
    Foto = "fotoperfil.gif"
    data = {'UserName':Nombre, 'FotoPerfil': Foto}
    return data

def renderIndex(request):
    data = usuario()
    return render(request,'templatesApp\index.html',data)

def renderUser(request):
    data = usuario()
    return render(request, 'templatesApp\paginausuario.html', data)


def renderElectro(request):
    data = usuario()
    data['title'] = 'Electronica'
    return render(request, 'templatesApp\productos.html', data)

def renderJuguete(request):
    data = usuario()
    data['title'] = 'Juguetes'
    return render(request, 'templatesApp\productos.html', data)

def renderRopa(request):
    data = usuario()
    data['title'] = 'Ropa'
    return render(request, 'templatesApp\productos.html', data)

def renderDetalles(request,pag,prod):
    paginas = ["electronica", "juguetes", "ropa"]
    productos = [{"prod1":"AAA","prod2":"BBB","prod3":"CCC"},{"prod1":"AAA","prod2":"BBB","prod3":"CCC"},{"prod1":"AAA","prod2":"BBB","prod3":"CCC"}]
    data = usuario()
    data["pagina"] = paginas[pag]
    data["producto"] = productos[pag][prod]
    return render(request, 'templatesApp\detalles.html', data)