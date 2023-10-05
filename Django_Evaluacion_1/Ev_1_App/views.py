from django.shortcuts import render

# Create your views here.

#datos de usuario
def usuario():
    Nombre = "Diego"
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
    FotosElectro = {"prod1":"tele.jpg", "prod2":"monitor.jpg", "prod3": "mouse.jpg"}
    data = usuario()
    data['title'] = 'Electronica'
    data.update(FotosElectro)
    return render(request, 'templatesApp\productos.html', data)

def renderJuguete(request):
    FotosJuguete = {"prod1":"auto.jpg", "prod2":"muneca.jpg", "prod3":"avion.jpg"}
    data = usuario()
    data['title'] = 'Juguetes'
    data.update(FotosJuguete)
    return render(request, 'templatesApp\productos.html', data)

def renderRopa(request):
    FotosRopa = {"prod1":"polera.jpg", "prod2":"poleron.jpg", "prod3":"pantalon.jpg"}
    data = usuario()
    data['title'] = 'Ropa'
    data.update(FotosRopa)
    return render(request, 'templatesApp\productos.html', data)

def renderDetalles(request,pag,prod):

    #Nombre de los productos Productos en diccionairos que son agrupados dentro de una lista para su uso
    prodElectro = {"prod1":"Tele", "prod2":"Monitor", "prod3": "Mouse"}
    prodJuguete = {"prod1":"Auto", "prod2":"Muñeca", "prod3":"Avión"}
    prodRopa = {"prod1":"Polera", "prod2":"Poleron", "prod3":"Pantalon"}
    productos = [prodElectro,prodJuguete,prodRopa]

    #Detalles de cada Producto
    DetalleElectro = {"prod1":'108" 8K 240hz HDR++1000 3D-HD-Res', "prod2":'24" 360hz QHD 0.01ms Freesync Gsync', "prod3": "Ultra preciso. Increible Mouse. RGB Personalizable. 10gr de peso super ultra ligero"}
    DetalleJuguete = {"prod1":"Auto", "prod2":"Muñeca", "prod3":"Avión"}
    DetalleRopa = {"prod1":"Polera", "prod2":"Poleron", "prod3":"Pantalon"}
    Detalles = [DetalleElectro,DetalleJuguete,DetalleRopa]

    #Precio Productos
    precioElectro = {"prod1":"1.450.000", "prod2":"380.000", "prod3": "80.000"}
    precioJuguete = {"prod1":"5.000", "prod2":"3.000", "prod3":"10.000"}
    precioRopa = {"prod1":"10.000", "prod2":"15.000", "prod3":"45.000"}
    precios = [precioElectro,precioJuguete,precioRopa]

    #Fotos Productos
    FotosElectro = {"prod1":"tele.jpg", "prod2":"monitor.jpg", "prod3": "mouse.jpg"}
    FotosJuguete = {"prod1":"auto.jpg", "prod2":"muneca.jpg", "prod3":"avion.jpg"}
    FotosRopa = {"prod1":"polera.jpg", "prod2":"poleron.jpg", "prod3":"pantalon.jpg"}
    Fotos = [FotosElectro,FotosJuguete,FotosRopa]

    #segun la pagina se le asigna un numero para buscar dentro de las listas
    if pag == "Electronica":
        numpag = 0
    elif pag == "Juguetes":
        numpag = 1
    elif pag == "Ropa":
        numpag = 2

    data = usuario()
    data["pagina"] = pag.lower()
    data["producto"] = productos[numpag][prod]
    data["detalle"] = Detalles[numpag][prod]
    data["precio"] = precios[numpag][prod]
    data["foto"] = Fotos[numpag][prod]
    return render(request, 'templatesApp\detalles.html', data)