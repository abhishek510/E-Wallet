from django.db import models
from users.models import WalletUser
# Create your models here.

class Balance(models.Model):
    user = models.ForeignKey(WalletUser, on_delete = models.CASCADE, unique = True)
    amount = models.DecimalField(max_digits = 10, decimal_places =2)

class TransactionHistory(models.Model):
    user = models.ForeignKey(WalletUser, on_delete = models.CASCADE)
    amount = models.DecimalField(max_digits = 10, decimal_places =2)
    created_at = models.DateTimeField(auto_now_add = True)