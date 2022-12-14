

import django_filters

from .models import DjangoChatterbotStatement

class DjangoChatterbotStatementFilter(django_filters.FilterSet):
    class Meta:
        model = DjangoChatterbotStatement
        fields = ['conversation', 'in_response_to', 'text'  ]