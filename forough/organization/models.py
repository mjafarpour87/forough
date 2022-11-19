from pickle import FALSE, TRUE
from django.db import models

from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# Create your models here.


UNIT_TYPE = (
        ('1', 'مرکز اداری'),
        ('2', 'مرکز درمانی'),
    )

class OrganizationUnit(models.Model):
    unit_name = models.CharField(max_length=100,verbose_name=_('Organization or Unit name'))
    unit_type = models.CharField(max_length=2,choices = UNIT_TYPE, verbose_name=_('Type of Organization Unit'))
    parent_unit =  models.ForeignKey('self',related_name ='parent', on_delete=models.RESTRICT,null=True , blank=True)
    deleted = models.BooleanField(default=False,verbose_name=_('Deleted'))

    def __str__(self):
        return self.unit_name

    def get_absolute_url(self): # new
        return reverse('organization_detail', args=[str(self.id)])