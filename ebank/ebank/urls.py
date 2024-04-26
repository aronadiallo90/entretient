"""
URL configuration for ebank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth.views import LoginView
import authentication.views
import comptes.views


urlpatterns = [
    path('admin/', admin.site.urls),
     
    path('login/',LoginView.as_view(template_name = 'authentication/login.html') , name='login'),
    path('logout/',authentication.views.logout_user, name='logout'),
    path('signup/',authentication.views.signup_page, name='signup'),


     path('', comptes.views.compte_list, name='compte_list'),
    path('comptes/ajouter/', comptes.views.ajouter_compte, name='ajouter_compte'),
    path('comptes/<int:compte_id>/depot/', lambda request, compte_id: comptes.views.effectuer_operation(request, 'depot', compte_id), name='depot'),
    path('comptes/<int:compte_id>/retrait/', lambda request, compte_id: comptes.views.effectuer_operation(request, 'retrait', compte_id), name='retrait'),
    path('comptes/<int:compte_id>/solde/', comptes.views.afficher_solde, name='afficher_solde'),
    path('retrait_impossible/', comptes.views.retrait_impossible, name='retrait_impossible'),  # Ajoutez un chemin pour accepter le paramètre compte_id
]
