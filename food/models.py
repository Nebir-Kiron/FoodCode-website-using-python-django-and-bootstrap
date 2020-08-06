from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(max_length=500)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="https://image.freepik.com/free-vector/fast-food-vector-card-with-text-placeholder_78458-98.jpg")

    def __str__(self):
        return self.item_name
    