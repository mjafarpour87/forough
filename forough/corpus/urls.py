from django.urls import path

from . import views

urlpatterns = [
 	path('', views.CategoryListTable.as_view(), name='category_list'),
	path('view', views.CategoryListCard.as_view(), name='category_list_card'),
	path('<int:pk>', views.CategoryDetail.as_view(), name='category_detail'),
	path('create', views.CategoryCreate.as_view(), name='category_create'),
	path('update/<int:pk>', views.CategoryUpdate.as_view(), name='category_update'),
	path('delete/<int:pk>', views.CategoryDelete.as_view(), name='category_delete'),
]

urlpatterns += [
        path('conversation/list', views.ConversationListTable.as_view(), name='conversation_list'),
        path('conversation/card', views.ConversationListCard.as_view(), name='conversation_list_card'),
        path('conversation/<int:pk>', views.ConversationDetail.as_view(), name='conversation_detail'),
        path('conversation/create', views.ConversationCreate.as_view(), name='conversation_create'),
        path('conversation/update/<int:pk>', views.ConversationUpdate.as_view(), name='conversation_update'),
        path('conversation/delete/<int:pk>', views.ConversationDelete.as_view(), name='conversation_delete'),

        path('conversation/train/<int:pk>', views.ConversationTrain.as_view(), name='conversation_train'),
        path('conversation/createfrom/<int:pk>', views.ConversationCreateFromChatStatment.as_view(), name='conversation_create_from_chatstatment'),
]   