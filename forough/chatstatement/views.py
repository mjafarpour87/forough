from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView 


# Create your views here.


from .models import DjangoChatterbotStatement
from .filters import DjangoChatterbotStatementFilter

# region DjangoChatterbotStatement
class DjangoChatterbotStatementListTable(LoginRequiredMixin,FilterView): 
    permission_required = 'chatstatement.view_DjangoChatterbotStatement' 
    model = DjangoChatterbotStatement
    template_name = 'chstatement/djangochatterbotstatement_list_table.html'
    context_object_name = 'ObjectList'
    paginate_by = 5
    filterset_class = DjangoChatterbotStatementFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_type'] = self.request.session['view_type']
        return context

    def get(self, request, *args, **kwargs):
        request.session['view_type'] = 'table'
        return super().get(request, *args, **kwargs)

    def get_ordering(self):
        ordering = self.request.GET.get('orderby', '')
        order = self.request.GET.get('order', 'asc')
        if ordering != '':
            if order == 'asc':
                ordering = "-" + ordering
            elif order == 'des':
                pass
            else:
                raise "error"
        # validate ordering here
        return ordering

class DjangoChatterbotStatementListCard(LoginRequiredMixin,FilterView): 
    permission_required = 'chatstatement.view_DjangoChatterbotStatement' 
    model = DjangoChatterbotStatement
    template_name = 'chstatement/djangochatterbotstatement_list_card.html' 
    context_object_name = 'ObjectList'
    paginate_by = 8
    filterset_class = DjangoChatterbotStatementFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_type'] = self.request.session['view_type']
        return context

    def get_ordering(self):
        ordering = self.request.GET.get('orderby', '')
        order = self.request.GET.get('order', 'asc')
        if ordering != '':
            if order == 'asc':
                ordering = "-" + ordering
            elif order == 'des':
                pass
            else:
                raise "error"
        # validate ordering here
        return ordering

    def get(self, request, *args, **kwargs):
        request.session['view_type'] = 'card'
        return super().get(request, *args, **kwargs)

class DjangoChatterbotStatementDetail(PermissionRequiredMixin,DetailView):
    permission_required = 'chatstatement.view_DjangoChatterbotStatement'  
    model = DjangoChatterbotStatement
    template_name = 'chstatement/djangochatterbotstatement_detail.html'

class DjangoChatterbotStatementCreate(PermissionRequiredMixin,CreateView): 
    permission_required = 'chatstatement.add_DjangoChatterbotStatement' 
    model = DjangoChatterbotStatement
    template_name = 'chstatement/djangochatterbotstatement_create.html'
    # form_class = DjangoChatterbotStatementForm
    fields =  '__all__'
    success_url = reverse_lazy('djangochatterbotstatement_list')

class DjangoChatterbotStatementUpdate(PermissionRequiredMixin,UpdateView): 
    permission_required = 'chatstatement.change_DjangoChatterbotStatement' 
    model = DjangoChatterbotStatement
    template_name = 'chstatement/djangochatterbotstatement_update.html'
    # form_class = DjangoChatterbotStatementForm
    fields = '__all__'
    success_url = reverse_lazy('djangochatterbotstatement_list')

class DjangoChatterbotStatementDelete(PermissionRequiredMixin,DeleteView): 
    permission_required = 'chatstatement.delete_DjangoChatterbotStatement' 
    model = DjangoChatterbotStatement
    template_name = 'chstatement/djangochatterbotstatement_confirm_delete.html'
    success_url = reverse_lazy('djangochatterbotstatement_list')

#endregion
       