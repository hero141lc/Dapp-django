from email.headerregistry import Address
from venv import create
#from MySQLdb import Date
from django.db import models
import django.utils.timezone as timezone
#from websockets import Data
# Create your models here.
class Token(models.Model):
    decimals = models.IntegerField(default=0,null=True, blank=True)
    name = models.CharField(max_length=50,null=True, blank=True)
    symbol = models.CharField(max_length=50,null=True, blank=True)
    logo_url = models.CharField(max_length=150,null=True, blank=True)
    address = models.CharField(max_length=50,unique=True,primary_key=True)
    update_at = models.DateTimeField(default = timezone.now)
    quote_currency = models.CharField(max_length=20,null=True, blank=True)
    pixiu=models.BooleanField(null=True, blank=True)
    isLp=models.BooleanField(null=True, blank=True)
    pub_date = models.DateTimeField('date published',auto_now = True)
class Lp(models.Model):
    symbol=models.CharField(max_length=50,null=True, blank=True)
    address= models.CharField(max_length=50,unique=True,primary_key=True)
    isLp=models.BooleanField(null=True, blank=True)
class Prices(models.Model):
    Token = models.ForeignKey(Token, on_delete=models.CASCADE)
    date = models.DateTimeField(default = timezone.now)
    price = models.FloatField(default=0,null=True, blank=True)
class daily_bill(models.Model):
    id=models.AutoField(primary_key=True)
    bill_key = models.CharField(max_length=255,null=True, blank=True,db_index = True)
    bill_value=models.JSONField()
    status = models.CharField(max_length=32,null=True, blank=True)
    updated_at =models.DateTimeField(default = timezone.now)
    created_at = models.DateTimeField(auto_now = True)

class Wallet(models.Model):
    address = models.CharField(max_length=50,unique=True,primary_key=True)
    updated_at =models.DateTimeField(default = timezone.now)
    pub_date = models.DateTimeField('date published',auto_now = True)

class Trans(models.Model):
    blockNumber=models.IntegerField(default=0,null=True, blank=True)
    hash=models.CharField(max_length=50,unique=True,primary_key=True)
    blockHash=models.CharField(max_length=50,unique=True)
    fromAddr=models.CharField(max_length=50,unique=True)
    Token=models.ForeignKey(Token, on_delete=models.CASCADE)
    toAddr=models.CharField(max_length=50,unique=True)
    value = models.IntegerField(default=0,null=True, blank=True)
class pair_info(models.Model):
    factory_addr=models.CharField(max_length=128,db_index = True)
    pair_index=models.IntegerField(default=0,null=True, blank=True,db_index = True)
    pair_addr=models.CharField(max_length=128,db_index = True)
    token0_addr=models.CharField(max_length=128,db_index = True)
    token1_addr=models.CharField(max_length=128,db_index = True)
    updated_time =models.DateTimeField(null=True,default = timezone.now)
    created_time =models.DateTimeField(null=True,auto_now = True)
'''
    next_update_at= models.DateTimeField(default = timezone.now)
    quote_currency= models.CharField(max_length=20,null=True, blank=True)
    chain_id= models.IntegerField(default=0,null=True, blank=True)
class TransHash(models.Model):
    block_signed_at=models.DateTimeField(default = timezone.now)
    tx_hash =models.CharField(max_length=50,unique=True,primary_key=True)

class LogEvent(models.Model):
    tx_hash = models.ForeignKey(TransHash, on_delete=models.CASCADE)
'''