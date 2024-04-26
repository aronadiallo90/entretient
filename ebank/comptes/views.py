from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import CompteBancaire
from decimal import Decimal
from django.urls import reverse
from django.contrib import messages



@login_required
def compte_list(request):
    # comptes = CompteBancaire.objects.filter(user=request.user)
    comptes = CompteBancaire.objects.all()
    numero_compte_recherche = request.GET.get('numero_compte_recherche', '')
    if numero_compte_recherche:
        comptes = comptes.filter(numero_compte__icontains=numero_compte_recherche)
    return render(request, 'comptes/compte_list.html', {'comptes': comptes})

@login_required
def ajouter_compte(request):
    if request.method == 'POST':
        numero_compte = request.POST['numero_compte']
        solde = request.POST['solde']
        if CompteBancaire.objects.filter(numero_compte=numero_compte).exists():
            # Si le compte existe déjà, affichez un message d'erreur
            messages.error(request, f"Le compte avec le numéro {numero_compte} existe déjà.")
            # Redirigez l'utilisateur vers une page appropriée, par exemple, la page d'accueil
            
        else:

            CompteBancaire.objects.create(user=request.user, numero_compte=numero_compte, solde=solde)
        return redirect('compte_list')
    return render(request, 'comptes/ajouter_compte.html')


@login_required
def effectuer_operation(request, operation, compte_id):
    compte = CompteBancaire.objects.get(pk=compte_id)
    if request.method == 'POST':
        montant = request.POST['montant'].replace(' ', '')
        montant = Decimal(montant)  # Convertissez en décimal après avoir nettoyé
       
        if operation == 'depot':
            compte.solde += montant
        elif operation == 'retrait':
            if compte.solde > montant:
                compte.solde -= montant
            else:
                # Rediriger vers la page de retrait impossible avec l'ID du compte
                return redirect('retrait_impossible')
        compte.save()
        # url_with_id = reverse('afficher_solde', kwargs={'pk': compte_id})
        return redirect('afficher_solde',compte_id)
    return render(request, 'comptes/effectuer_operation.html', {'operation': operation, 'compte': compte})



@login_required
def afficher_solde(request, compte_id):
    compte = CompteBancaire.objects.get(pk=compte_id)
    return render(request, 'comptes/afficher_solde.html', {'compte': compte})


def retrait_impossible(request):
    return render(request, 'comptes/retrait_impossible.html')

