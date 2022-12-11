

# # Django’s cache framework
# # https://docs.djangoproject.com/en/4.1/topics/cache/
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'unique-snowflake',
#     }
#     ,'select2': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'unique-snowflake',
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#         }
#     }
# }

# # Tell select2 which cache configuration to use:
# SELECT2_CACHE_BACKEND = "select2"