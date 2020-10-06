from django.db import models

# Create your models here.
# class Stock(models.Model):
#     StockName = models.CharField(blank=True, max_length=100)
#     CurrentPrice = models.FloatField(null=True,blank=True)
#     def __str__(self):
#         return self.StockName
    
class table(models.Model):
    symbol=models.CharField(max_length=10)
    company_name=models.CharField(max_length=40)
    last_price=models.IntegerField(default=0)
    H_52_wk=models.IntegerField(default=0)
    L_52_wk=models.IntegerField(default=0)
    market_cap=models.IntegerField(default=0)
    # table_text='Hi!stocks'
    # def __str__(self):
    #     return self.table_text