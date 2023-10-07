from django.shortcuts import render

# Create your views here.

#datos de usuario
def usuario():
    Nombre = "Diego"
    Foto = "fotoperfil.gif"
    Desc = "Hola, Evaluacion 1 Django!"
    Correo = "Diego@correo.com"
    data = {'UserName':Nombre, 'FotoPerfil': Foto, 'Desc': Desc, 'Correo':Correo}
    return data

#render de templates
def renderUser(request):
    data = usuario()
    return render(request, 'templatesApp\paginausuario.html', data)

def renderIndex(request):
    data = usuario()
    return render(request,'templatesApp\index.html',data)

def renderElectro(request):
    prodElectro = {"prod1":"Tele", "prod2":"Monitor", "prod3": "Mouse"}
    FotosElectro = {"foto1":"tele.jpg", "foto2":"monitor.jpg", "foto3": "mouse.jpg"}
    otros = {'title':'Electronica', 'ico':'bi bi-hdd', 'bgcolor':'bg-info', 'txtcolor':'text-black'}
    
    data = usuario()
    data.update(otros)
    data.update(FotosElectro)
    data.update(prodElectro)
    return render(request, 'templatesApp\productos.html', data)

def renderJuguete(request):
    prodJuguete = {"prod1":"Auto", "prod2":"Muñeca", "prod3":"Avión"}
    FotosJuguete = {"foto1":"auto.jpg", "foto2":"muneca.jpg", "foto3":"avion.jpg"}
    otros = {'title':'Juguetes', 'ico':'bi bi-car-front-fill', 'bgcolor':'bg-warning', 'txtcolor':'text-black'}
    
    data = usuario()
    data.update(otros)
    data.update(FotosJuguete)
    data.update(prodJuguete)
    return render(request, 'templatesApp\productos.html', data)

def renderRopa(request):
    prodRopa = {"prod1":"Polera", "prod2":"Poleron", "prod3":"Pantalon"}
    FotosRopa = {"foto1":"polera.jpg", "foto2":"poleron.jpg", "foto3":"pantalon.jpg"}
    otros = {'title':'Ropa', 'ico':'bi bi-bag-fill', 'bgcolor':'bg-danger', 'txtcolor':'text-light'}
    
    data = usuario()
    data.update(otros)
    data.update(FotosRopa)
    data.update(prodRopa)
    return render(request, 'templatesApp\productos.html', data)

def renderDetalles(request,pag,prod):
    #pag viene desde la url y es el nombre de la pagina Ej: "Electronica"
    #prod viene desde la url y es el nombre de la posicion del producto desde el 1 al 3 Ej: "prod1"

    #Nombre de los productos Productos en diccionairos que son agrupados dentro de una lista para su uso
    prodElectro = {"prod1":"Tele", "prod2":"Monitor", "prod3": "Mouse"}
    prodJuguete = {"prod1":"Auto", "prod2":"Muñeca", "prod3":"Avión"}
    prodRopa = {"prod1":"Polera", "prod2":"Poleron", "prod3":"Pantalon"}
    productos = [prodElectro,prodJuguete,prodRopa]

    #Detalles de cada Producto
    DetalleElectro = {"prod1":'108" 8K 240hz HDR++1000 3D-HD-Res', "prod2":'24" 360hz QHD 0.01ms Freesync Gsync', "prod3": "Ultra preciso. Increible Mouse. RGB Personalizable. 10gr de peso super ultra ligero"}
    DetalleJuguete = {"prod1":"Auto de Juguete ultra veloz, reistente a huracanes. Fabricado en titanio reforzado con coraza de submarino nuclear", "prod2":"Muñeca automata. habla por la noche y se mueve. ¡No hacercar crucifijos ni agua bendita!", "prod3":"Avión volador. vuela muy alto."}
    DetalleRopa = {"prod1":"Polera de fibra nuclear", "prod2":"Poleron reflectante de materia oscura", "prod3":"Pantalon autoajustable. funciones inteligentes. posee compatibilidad con Siri, Alexa y Google Home"}
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

    #segun la pagina (pag) se le asigna un numero para buscar dentro de las listas
    if pag == "Electronica":
        numpag = 0
    elif pag == "Juguetes":
        numpag = 1
    elif pag == "Ropa":
        numpag = 2

    data = usuario()
    data['title'] = 'Detalles'
    data["pagina"] = pag.lower()
    data["producto"] = productos[numpag][prod]
    data["detalle"] = Detalles[numpag][prod]
    data["precio"] = precios[numpag][prod]
    data["foto"] = Fotos[numpag][prod]
    return render(request, 'templatesApp\detalles.html', data)