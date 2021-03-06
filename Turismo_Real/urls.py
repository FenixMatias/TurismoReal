"""Turismo_Real URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from Servicio_Turismo_Real.views import *
from user.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Turismo_Real/', include('Servicio_Turismo_Real.urls')),
    path('reportes/', include('reportes.urls')),
    path('user/', include('user.urls')),
    path('', IndexView.as_view(), name='index'),
    path('Login/', LoginFormView.as_view(), name='login'),
    path('Logout/', LogoutRedirectView.as_view(), name='logout'),
    path('Registro/', registro, name="registro"),
    path('ReseteoContraseña/', ResetPasswordView.as_view(), name="reseteocontraseña"),
    path('RecuperarContraseña/<str:token>/', ChangePasswordView.as_view(), name="recuperarcontraseña"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
