from django.db import models
from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class FoodCategory(BaseModel):
    name = models.CharField(max_length=200)
    description= models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

class Food(BaseModel):
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price= models.IntegerField()

    def __str__(self):
        return f'{self.name}'


class Order(BaseModel):
    foods = models.ManyToManyField(Food)
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.customer}'

