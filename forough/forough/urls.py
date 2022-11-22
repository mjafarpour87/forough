
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static #add this
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _


handler404 = 'django_cuser.views.handler404'
handler500 = 'django_cuser.views.handler500'
handler403 = 'django_cuser.views.handler403'
# handler400 = 'django_cuser.views.bad_request'


urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('users/', include('django_cuser.urls')),
    path('corpus/', include('corpus.urls')),
    # path('', views.main_page, name = 'main_page')

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from .views import ChatterBotAppView, ChatterBotApiView, page_chat


urlpatterns += [
    path('', page_chat.as_view(), name='page_chat'),
    path('api/chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),
]