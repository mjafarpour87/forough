
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static #add this
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from users import views

urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('users/', include('users.urls')),
    path('organization/', include('organization.urls')),
    path('corpus/', include('corpus.urls')),
    # path('', views.main_page, name = 'main_page')

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from .views import ChatterBotAppView, ChatterBotApiView


urlpatterns += [
    path('', ChatterBotAppView.as_view(), name='main'),
    path('api/chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),
]