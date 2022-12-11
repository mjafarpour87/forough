
# User Authentication config
LOGIN_URL = '/users/accounts/login'
LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "dashboard"
AUTH_USER_MODEL = "django_cuser.CustomUser"  