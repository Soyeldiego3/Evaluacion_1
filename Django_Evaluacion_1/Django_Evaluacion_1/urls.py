"""
URL configuration for Django_Evaluacion_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Ev_1_App import views as ev1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ev1.renderIndex),
    path('electronica/', ev1.renderElectro),
    path('juguetes/', ev1.renderJuguete),
    path('ropa/', ev1.renderRopa),
    path('user/', ev1.renderUser),
    path('detalles/<str:pag>/<str:prod>', ev1.renderDetalles),
]
