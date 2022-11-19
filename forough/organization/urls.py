from django.urls import path

from . import views

urlpatterns = [
 	path('', views.OrganizationUnitListTable.as_view(), name='organization_list'),
	path('view', views.OrganizationUnitListCard.as_view(), name='organization_list_card'),
	path('<int:pk>', views.OrganizationUnitDetail.as_view(), name='organization_detail'),
	path('create', views.OrganizationUnitCreate.as_view(), name='organization_create'),
	path('update/<int:pk>', views.OrganizationUnitUpdate.as_view(), name='organization_update'),
	path('delete/<int:pk>', views.OrganizationUnitDelete.as_view(), name='organization_delete'),
]