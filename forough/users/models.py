
from importlib.metadata import requires
from django.utils.timezone import now
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# from ..main.fx import is_valid_national_code
import re

from organization.models import OrganizationUnit

def is_valid_national_code(value):
    if not re.search(r'^\d{10}$', value): return False
    check = int(value[9])
    s = sum(int(value[x]) * (10 - x) for x in range(9)) % 11
    return check == s if s < 2 else check + s == 11

def national_code_validator(value):
    if not is_valid_national_code(value):
        raise ValidationError(
            _('%(value)s is not a national code'),
            params={'value': value},
        )


def user_directory_path(instance, filename):

    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}_{1}'.format(instance.id, filename)
        
class CustomUser(AbstractUser):
    natinal_code = models.CharField(unique=True,max_length=10, verbose_name= "Natinal ID of person",validators=[national_code_validator],blank= True,null=True)
    birth_date = models.DateField(verbose_name= _("Birthdate"),blank= True,null=True )
    mobile = models.CharField(verbose_name= _("Mobile Phone"), max_length=20,blank=False,null=True, default=None , help_text=_(
            "Required. Incorrect formatting may result in undelivered messages or a message being sent to an incorrect handset."
        ),)
    failed_password_count = models.IntegerField(default=0)
    last_password_changedate = models.DateTimeField(default=now )
    display_name =  models.CharField(verbose_name= _("Display Name"), max_length=60, blank= True)
    image_avatar = models.ImageField(verbose_name= _("Profile Image") , upload_to = user_directory_path , blank= True)
    organization_unit = models.ForeignKey(OrganizationUnit,verbose_name= _("Organization Unit") , related_name ='organization', on_delete=models.RESTRICT,null=True , blank=True)


    def __str__(self):
        return self.username

    def get_absolute_url(self): # new
        return reverse('user_detail', args=[str(self.id)])
    



