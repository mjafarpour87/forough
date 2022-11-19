from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
# from requests import request
from users.forms import CustomUserCreationForm,CustomUserChangeForm
from django.http import HttpResponseRedirect

from django.utils import translation

from django.conf import settings
from django.conf.locale import LANG_INFO

from .models import CustomUser

from django.contrib.auth.mixins import PermissionRequiredMixin

import logging
# logging.basicConfig(level=logging.INFO)
# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
def dashboard(request):
    logger.error('this is dashboard request '+str(request))
    return render(request, "users/dashboard.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )

    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))

def set_language(request):
    
    logger.debug('language selected is : '+ translation.get_language())
    if request.method == 'POST':
        la = request.POST["language"]
        logger.debug('language selected is : ' + str(la))
        request.session['language_id'] = la
        translation.activate(la)
        request.LANGUAGE_CODE = translation.get_language()
    if request.GET.__contains__('language_id'):  # Set language in Session variable
        # Redirect to home
        request.session['language_id'] = request.GET['language_id']
    #return HttpResponseRedirect('/')
    return render(request, "users/dashboard.html")

def main_page(request):


    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # request.session[settings.LANGUAGE_SESSION_KEY] = 'fa'

    request.session['language_id'] = 'fa'

    context = {
        'num_visits': num_visits,
        'language_id' :  request.session['language_id']
    }
    # context =  request.session.keys()
    return render(request, "main_page.html", context=context)



from .models import CustomUser as User
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse,reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# region user CRUD
class UserListTable(LoginRequiredMixin,ListView): 
    model = User
    template_name = 'crud/user_list_table.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_type'] = self.request.session['view_type']
        return context

    def get(self, request, *args, **kwargs):
        # view_type = request.session.get('view_type', 'table')
        request.session['view_type'] = 'table'
        return super().get(request, *args, **kwargs)

class UserListCard(LoginRequiredMixin,ListView): 
    model = User
    template_name = 'crud/user_list_card.html' 
    context_object_name = 'ObjectList'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_type'] = self.request.session['view_type']
        context['r'] = 0
        return context

    def get(self, request, *args, **kwargs):
        # view_type = request.session.get('view_type', 'card')
        request.session['view_type'] = 'card'
        return super().get(request, *args, **kwargs)

class UserDetail(DetailView): 
    model = User
    template_name = 'crud/user_detail.html'

class UserCreate(CreateView): 
    model = CustomUser
    template_name = 'crud/user_create.html'
    form_class  = CustomUserCreationForm
    # fields = '__all__'
    success_url = reverse_lazy('user_list')



class UserUpdate(UpdateView): 
    model = CustomUser
    template_name = 'crud/user_update.html'
    form_class  = CustomUserChangeForm
    # fields = [ 'display_name' , 'first_name' , 'last_name' , 'email' , 'mobile' , 'natinal_code' , 'birth_date']
    success_url = reverse_lazy('user_list')

    # def get_object(self):
    #     return CustomUser.objects.get(username=self.request.CustomUser.username)


    def post(self, request, *args, **kwargs):
        form = CustomUserChangeForm(request.POST, request.FILES)

        if "cancel" in request.POST:
            object = self.get_object()
            url = object.get_absolute_url()
            return HttpResponseRedirect(url)
        else:
            return super(UserUpdate, self).post(request, *args, **kwargs)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('user_list'))
        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class UserDelete(PermissionRequiredMixin,DeleteView): 
    permission_required = 'users.delete_user'
    model = CustomUser
    template_name = 'crud/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

#endregion
