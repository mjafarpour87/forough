from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# Create your models here.
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,verbose_name=_('Category'))
    def __str__(self):
        return self.name

# The Conversation class is a model that has a foreign key to the Category class
class Conversation(models.Model):
    category =  models.ForeignKey(Category,related_name ='categories', on_delete=models.RESTRICT)
    statement = models.CharField(max_length=200,verbose_name=_('Statement'))
    response = models.CharField(max_length=300,verbose_name=_('Response'))
    train = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.statement