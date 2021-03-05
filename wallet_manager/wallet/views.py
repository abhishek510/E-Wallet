from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Balance, TransactionHistory
from . import constants
from decimal import Decimal

# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html')

    
def test(request):
    if request.method == "POST":
        transaction_type = request.POST.get("type")
        transaction_amount = request.POST.get("amount")
        wallet_owner = request.user
        check_balance = Balance.objects.filter(user = wallet_owner)
        if len(check_balance) == 0:
            balance_initial = Balance(user = wallet_owner, amount = constants.MINIMUM_BALANCE)
            balance_initial.save()

        check_balance = check_balance[0]
        if transaction_type == constants.DEBIT:
            if check_balance.amount - Decimal(transaction_amount) >= constants.MINIMUM_BALANCE:
                Balance.objects.filter(user = wallet_owner).update(amount = check_balance.amount - Decimal(transaction_amount))
                transaction = TransactionHistory(user = wallet_owner, amount = Decimal(transaction_amount) * -1)
                transaction.save()
            else:
                return render(request, 'index.html', {'min_balance': True})
        
        if transaction_type == constants.CREDIT:
            Balance.objects.filter(user = wallet_owner).update(amount = check_balance.amount + Decimal(transaction_amount))
            transaction = TransactionHistory(user = wallet_owner, amount = Decimal(transaction_amount))
            transaction.save()

        return render(request, 'index.html', {'alert_flag': True})
    