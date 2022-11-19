from django.shortcuts import render
from .models import OrganizationUnit


from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse,reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.

# region OrganizationUnit
class OrganizationUnitListTable(LoginRequiredMixin,ListView): 
    # permission_required = 'organization.view_OrganizationUnit'  
    model = OrganizationUnit
    template_name = 'organization_list_table.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_type'] = self.request.session['view_type']
        return context

    def get(self, request, *args, **kwargs):
        # view_type = request.session.get('view_type', 'table')
        request.session['view_type'] = 'table'
        return super().get(request, *args, **kwargs)

class OrganizationUnitListCard(LoginRequiredMixin,ListView): 
    # permission_required = 'organization.view_OrganizationUnit'  
    model = OrganizationUnit
    template_name = 'organization_list_card.html' 
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

class OrganizationUnitDetail(PermissionRequiredMixin,DetailView):
    permission_required = 'organization.view_OrganizationUnit'  
    model = OrganizationUnit
    template_name = 'organization_detail.html'

class OrganizationUnitCreate(PermissionRequiredMixin,CreateView): 
    permission_required = 'organization.add_OrganizationUnit' 
    model = OrganizationUnit
    template_name = 'organization_create.html'
    fields = ['unit_name' , 'unit_type' , 'parent_unit']
    success_url = reverse_lazy('organization_list')

class OrganizationUnitUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'organization.change_OrganizationUnit' 
    model = OrganizationUnit
    template_name = 'organization_update.html'
    fields = '__all__'
    success_url = reverse_lazy('organization_list')

class OrganizationUnitDelete(PermissionRequiredMixin,DeleteView): 
    permission_required = 'organization.delete_OrganizationUnit'
    model = OrganizationUnit
    template_name = 'organization_confirm_delete.html'
    success_url = reverse_lazy('organization_list')

#endregion