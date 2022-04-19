from django.db import models

import django.utils.timezone as timezone
# Create your models here.
class Token(models.Model):
    contract_decimals = models.IntegerField(default=0)
    contract_name = models.CharField(max_length=50)
    contract_ticker_symbol = models.CharField(max_length=10)
    logo_url = models.CharField(max_length=150)
    contract_address = models.CharField(max_length=50)
    update_at = models.DateTimeField(default = timezone.now)
    quote_currency = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published',auto_now = True)

class Prices(models.Model):
    Token = models.ForeignKey(Token, on_delete=models.CASCADE)
    date = models.DateTimeField(default = timezone.now)
    price = models.IntegerField(default=0)