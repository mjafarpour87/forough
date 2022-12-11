from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse,reverse_lazy
from .models import Category,Conversation


from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ListTrainer

# region Conversation
class ConversationListTable(LoginRequiredMixin,ListView): 
    # permission_required = 'conversation.view_Conversation'  
    model = Conversation
    template_name = 'conversation_list_table.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_type'] = self.request.session['view_type']
        return context

    def get(self, request, *args, **kwargs):
        # view_type = request.session.get('view_type', 'table')
        request.session['view_type'] = 'table'
        return super().get(request, *args, **kwargs)

class ConversationListCard(LoginRequiredMixin,ListView): 
    # permission_required = 'conversation.view_Conversation'  
    model = Conversation
    template_name = 'conversation_list_card.html' 
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

class ConversationDetail(PermissionRequiredMixin,DetailView):
    permission_required = 'conversation.view_Conversation'  
    model = Conversation
    template_name = 'conversation_detail.html'

class ConversationCreate(PermissionRequiredMixin,CreateView): 
    permission_required = 'conversation.add_Conversation' 
    model = Conversation
    template_name = 'conversation_create.html'
    fields = '__all__'
    success_url = reverse_lazy('conversation_list')

class ConversationUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'conversation.change_Conversation' 
    model = Conversation
    template_name = 'conversation_update.html'
    fields = '__all__'
    success_url = reverse_lazy('conversation_list')

class ConversationDelete(PermissionRequiredMixin,DeleteView): 
    permission_required = 'conversation.delete_Conversation'
    model = Conversation
    template_name = 'conversation_confirm_delete.html'
    success_url = reverse_lazy('conversation_list')

class ConversationTrain(PermissionRequiredMixin,DetailView):
    permission_required = 'conversation.view_Conversation'  
    model = Conversation
    template_name = 'conversation_train.html'
   

    # override context data
    def get_context_data(self, *args, **kwargs):
        context = super(ConversationTrain,
                self).get_context_data(*args, **kwargs)
        # add extra field


        chatterbot = ChatBot(**settings.CHATTERBOT)
        trainer = ListTrainer(chatterbot)

        c = Conversation.objects.first()
        c.train = 1
        try:

            trainer.train([
                c.statement,
                c.response,
            ])
            c.save()
        except:
            context["category_msg"] = "MISC"
        print(context)
        return context


from chatstatement.models import DjangoChatterbotStatement
class ConversationCreateFromChatStatment(PermissionRequiredMixin,CreateView): 
    permission_required = 'conversation.add_Conversation' 
    model = Conversation
    template_name = 'conversation_create_from_chatstatment.html'
    fields = ["category" ,"statement" , "response"]
    success_url = reverse_lazy('djangochatterbotstatement_list')

    def get_initial(self):
        chatstatment_id = self.kwargs.get('pk')
        o = DjangoChatterbotStatement.objects.filter(id = chatstatment_id).values()
        return {
            'statement': o[0]['in_response_to'] ,
            'response' : o[0]['text'],
        }





#endregion


# region Category
class CategoryListTable(LoginRequiredMixin,ListView): 
    # permission_required = 'category.view_Category'  
    model = Category
    template_name = 'category_list_table.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_type'] = self.request.session['view_type']
        return context

    def get(self, request, *args, **kwargs):
        # view_type = request.session.get('view_type', 'table')
        request.session['view_type'] = 'table'
        return super().get(request, *args, **kwargs)

class CategoryListCard(LoginRequiredMixin,ListView): 
    # permission_required = 'category.view_Category'  
    model = Category
    template_name = 'category_list_card.html' 
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

class CategoryDetail(PermissionRequiredMixin,DetailView):
    permission_required = 'category.view_Category'  
    model = Category
    template_name = 'category_detail.html'

class CategoryCreate(PermissionRequiredMixin,CreateView): 
    permission_required = 'category.add_Category' 
    model = Category
    template_name = 'category_create.html'
    fields = '__all__'
    success_url = reverse_lazy('category_list')

class CategoryUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'category.change_Category' 
    model = Category
    template_name = 'category_update.html'
    fields = '__all__'
    success_url = reverse_lazy('category_list')

class CategoryDelete(PermissionRequiredMixin,DeleteView): 
    permission_required = 'category.delete_Category'
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

#endregion
