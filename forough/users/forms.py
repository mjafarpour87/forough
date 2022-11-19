from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _

from .models import CustomUser

from django import forms  
from django.contrib.auth import get_user_model  

from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
  
User = get_user_model()  

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)  
    password2 = forms.CharField(label=_('Confirm Password'), widget=forms.PasswordInput)  

    class Meta:
        model = CustomUser
        fields = ("first_name" ,"last_name" , "username", "natinal_code" , "mobile" , "email" , "birth_date" ,"display_name","organization_unit")

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['birth_date'] = JalaliDateField(label=_("Birthdate"), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )

    def clean_email(self):  
        email = self.cleaned_data.get('email')  
        qs = User.objects.filter(email=email)  
        if qs.exists():  
            raise forms.ValidationError("Email is taken")  
        return email  
  
    def clean(self):  
        '''  
        Verify both passwords match.  
        '''  
        cleaned_data = super().clean()  
        password1 = cleaned_data.get("password1")  
        password2 = cleaned_data.get("password2")  
          
        if password1 is not None and password1 != password2:  
            self.add_error("password2", "Your passwords must match")  
        return cleaned_data  
  
    def save(self, commit=True):  
        # Save the provided password in hashed format  
        user = super().save(commit=False)  
        user.set_password(self.cleaned_data["password1"])  
        if commit:  
            user.save()  
        return user        

class CustomUserChangeForm(UserChangeForm):


    class Meta:
        model = User
        fields =  fields = ("first_name" ,"last_name" , "username", "natinal_code" , "mobile" , "email" , "birth_date" ,"display_name","organization_unit","image_avatar")

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['birth_date'] = JalaliDateField(label=_("Birthdate"), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )

    def save(self, commit=True):  
        # Save the provided password in hashed format  
        User = super().save(commit=False)  
        if commit:
            User.save()  
        return User     