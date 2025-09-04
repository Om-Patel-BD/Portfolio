import os
from django.core.wsgi import get_wsgi_application

# Tell Django where settings are
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myportfolio.settings")

# Get WSGI app (works with Whitenoise for static files)
application = get_wsgi_application()

# Vercel expects a function named 'handler'
def handler(event, context):
    return application(event, context)
