from django.urls import path
from . import views


urlpatterns = [
        path('chstatement/list', views.DjangoChatterbotStatementListTable.as_view(), name='djangochatterbotstatement_list'),
        path('chstatement/card', views.DjangoChatterbotStatementListCard.as_view(), name='djangochatterbotstatement_list_card'),
        path('chstatement/<int:pk>', views.DjangoChatterbotStatementDetail.as_view(), name='djangochatterbotstatement_detail'),
        path('chstatement/create', views.DjangoChatterbotStatementCreate.as_view(), name='djangochatterbotstatement_create'),
        path('chstatement/update/<int:pk>', views.DjangoChatterbotStatementUpdate.as_view(), name='djangochatterbotstatement_update'),
        path('chstatement/delete/<int:pk>', views.DjangoChatterbotStatementDelete.as_view(), name='djangochatterbotstatement_delete'),
]    