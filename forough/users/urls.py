from django.urls import path,include,re_path as url
from users.views import dashboard, register,set_language

from . import views

urlpatterns = [
    path('', dashboard, name="dashboard"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", register, name="register"),
    
    path('set_language', set_language, name="set_language"),
    
    
]

urlpatterns += [
 	path('list', views.UserListTable.as_view(), name='user_list'),
	path('card', views.UserListCard.as_view(), name='user_list_card'),
	path('<int:pk>', views.UserDetail.as_view(), name='user_detail'),
	path('create', views.UserCreate.as_view(), name='user_create'),
	path('update/<int:pk>', views.UserUpdate.as_view(), name='user_update'),
	path('delete/<int:pk>', views.UserDelete.as_view(), name='user_delete'),
]