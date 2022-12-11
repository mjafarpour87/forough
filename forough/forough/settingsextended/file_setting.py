from ..settings import BASE_DIR, DEBUG

# Static files (CSS, JavaScript, Images)
if not DEBUG: 
    # STATIC_ROOT is useless during development, it's only required for deployment.
    STATIC_ROOT = BASE_DIR / 'static'
else:
    STATICFILES_DIRS = [
                        BASE_DIR / "static",
                        ]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'