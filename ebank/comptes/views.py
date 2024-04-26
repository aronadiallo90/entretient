from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import CompteBancaire
from decimal import Decimal
from django.urls import reverse



@login_required
def compte_list(request):
    comptes = CompteBancaire.objects.filter(user=request.user)
    return render(request, 'comptes/compte_list.html', {'comptes': comptes})

@login_required
def ajouter_compte(request):
    if request.method == 'POST':
        numero_compte = request.POST['numero_compte']
        solde = request.POST['solde']
        CompteBancaire.objects.create(user=request.user, numero_compte=numero_compte, solde=solde)
        return redirect('compte_list')
    return render(request, 'comptes/ajouter_compte.html')


@login_required
def effectuer_operation(request, operation, compte_id):
    compte = CompteBancaire.objects.get(pk=compte_id)
    if request.method == 'POST':
        montant = Decimal(request.POST['montant'])
        if operation == 'depot':
            compte.solde += montant
        elif operation == 'retrait':
            if compte.solde > montant:
                compte.solde -= montant
        compte.save()
        # url_with_id = reverse('afficher_solde', kwargs={'pk': compte_id})
        return redirect('afficher_solde',compte_id)
    return render(request, 'comptes/effectuer_operation.html', {'operation': operation, 'compte': compte})



@login_required
def afficher_solde(request, compte_id):
    compte = CompteBancaire.objects.get(pk=compte_id)
    return render(request, 'comptes/afficher_solde.html', {'compte': compte})
