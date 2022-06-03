from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

class Currency(models.Model):
    character = models.CharField(max_length=1)
    cur_name=models.CharField(max_length=3,default="USD")

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete = models.PROTECT)
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    desc_full = models.TextField()
    price_USD=models.PositiveSmallIntegerField()
    currency=models.ForeignKey(Currency,default=1, on_delete = models.PROTECT)
    picture1_url = models.URLField(default="")
    picture2_url = models.URLField(default="")
    picture3_url = models.URLField(default="")